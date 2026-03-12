import time
import random

def run_synthetic_load(duration_sec=60):
    """Saturates ARM v8.2 cores with high-entropy arithmetic to measure dynamic power."""
    print(f"--- Triggering {duration_sec}s Synthetic Workload ---")
    start_time = time.time()
    
    while (time.time() - start_time) < duration_sec:
        # High-density floating point operations to trigger switching activity
        _ = [random.random() * random.random() for _ in range(100000)]
        
        elapsed = int(time.time() - start_time)
        if elapsed % 10 == 0 and elapsed > 0:
            print(f"Workload Status: {elapsed}s / {duration_sec}s")

if __name__ == "__main__":
    try:
        run_synthetic_load()
    except KeyboardInterrupt:
        print("\nWorkload Interrupted.")
