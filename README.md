# SoC Characterization and Telemetry Suite
## Executive Summary
This project is a hardware in the loop (HIL) validation suite designed to characterize the Power, Performance, and Thermal (PPT) profile of the Orin Nano SoC. By leveraging unbuffered kernel telemetry, the suite quantifies the "Power-per-instruction" cost of synthetic workloads, providing efficiency insights of silicon architecture.

## Telemetry Profiler
+ Low latency: Implements unbuffered reading to prevent telemetry hanging
+ Regex processing: Dynamically parses tegrastats output to isolate VDD_IN (Power Draw) and tj (Junction Temperature)
+ Deterministic logging: Synchronizes hardware rails with software timestamps in a structured CSV format

## Synthetic Workload Generator
+ The goal here is to maximize transistor switching activity to observe dynamic power delta. Opted for pure math synthetic mode.

## Test 1: Baseline 
+ Goal: See how much power the Jetson uses when it's just sitting
