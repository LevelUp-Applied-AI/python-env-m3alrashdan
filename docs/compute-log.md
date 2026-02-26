==================================================
SYSTEM INFORMATION
==================================================
OS:         Windows 10
Version:    10.0.26200
Machine:    AMD64
Processor:  AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD
Python:     3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)]

Benchmark 1 — sum(range(5,000,000))
  Result:  12,499,997,500,000
  Time:    0.2540 seconds

Benchmark 2 — list comprehension (n=1,000,000)
  First 5: [0, 1, 4, 9, 16]
  Time:    0.0904 seconds

Benchmark 3 — string join (n=100,000)
  Length:  588,889 characters
  Time:    0.0200 seconds

==================================================
SUMMARY
==================================================
  sum benchmark:    0.2540s
  list benchmark:   0.0904s
  string benchmark: 0.0200s

## RAM

Total RAM: 16 GB