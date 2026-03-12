# SoC Characterization and Telemetry Suite
## Executive Summary
This project is a hardware in the loop (HIL) validation suite designed to characterize the Power, Performance, and Thermal (PPT) profile of the Orin Nano SoC. By leveraging unbuffered kernel telemetry, the suite quantifies the "Power-per-instruction" cost of synthetic workloads, providing efficiency insights of silicon architecture.

## Telemetry Profiler
+ Low latency: Implements unbuffered reading to prevent telemetry hanging
+ Regex processing: Dynamically parses tegrastats output to isolate VDD_IN (Power Draw) and tj (Junction Temperature)
+ Deterministic logging: Synchronizes hardware rails with software timestamps in a structured CSV format

## Synthetic Workload Generator
+ The goal here is to maximize transistor switching activity to observe dynamic power delta. Opted for pure math synthetic mode.

## Test:
+ Goal: See how much power the Jetson uses when it's just sitting vs. during stress tests

### **Experimental Results**
| State | Avg Power (mW) | Peak Power (mW) | Temp (°C) |
| :--- | :--- | :--- | :--- |
| **Idle Baseline** | 3,766 | 3,806 | 44.5 |
| **Active Load** | 5,350 | 5,576 | 45.6 |
| **DELTA** | **+1,584 (42%)** | **Transient: 1.7W** | **+1.1°C** |

---

### **Engineering Insights**
* **Switching Activity:** Observed a 42% jump in VDD_IN draw during synthetic math loads, indicating responsive power-gating on the ARM cores.
* **Thermal Slope:** Minimal junction temperature rise suggests efficient thermal dissipation for burst-mode workloads.
* **Transient Captures:** Captured a peak transient of 5.5W, providing a baseline for analyzing voltage rail stability (IR drop).

---

### **Technical Stack**
* **Telemetry:** Non-blocking kernel interface via `tegrastats`.
* **Processing:** Python-based Regex extraction for deterministic logging.
* **Workload:** High-entropy synthetic ALU saturation.
