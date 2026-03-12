import subprocess
import re
import csv
import time

def extract_metrics(line):
    """Parses raw tegrastats output using regex to isolate SoC metrics."""
    power_match = re.search(r'VDD_IN (\d+)mW', line)
    gpu_match = re.search(r'GR3D_FREQ (\d+)%', line)
    temp_match = re.search(r'tj@([\d.]+)C', line)

    return {
        "timestamp": time.time(),
        "power_mw": int(power_match.group(1)) if power_match else 0,
        "gpu_load_pct": int(gpu_match.group(1)) if gpu_match else 0,
        "temp_c": float(temp_match.group(1)) if temp_match else 0
    }

if __name__ == "__main__":
    print("--- SoC Telemetry Profiler Active ---")
    try:
        # bufsize=1 ensures real-time data flow without kernel buffering
        process = subprocess.Popen(
            ['tegrastats', '--interval', '500'], 
            stdout=subprocess.PIPE, text=True, bufsize=1
        )

        with open('validation_log.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "power_mw", "gpu_load_pct", "temp_c"])
            writer.writeheader()
            
            for line in iter(process.stdout.readline, ''):
                data = extract_metrics(line)
                print(f"Telemetry -> Power: {data['power_mw']}mW | Temp: {data['temp_c']}C")
                writer.writerow(data)
                f.flush() # Force write to disk for data persistence

    except KeyboardInterrupt:
        print("\nSession Terminated. Data saved to validation_log.csv")
        process.terminate()
