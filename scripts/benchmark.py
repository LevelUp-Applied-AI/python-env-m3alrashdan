#!/usr/bin/env python3
"""
Benchmark script for AI.SPIRE Pre-Work.
DO NOT MODIFY THIS FILE.
"""

import platform
import time
import numpy as np
import pandas as pd
from scipy import linalg


def section(title: str):
    print("=" * 50)
    print(title)
    print("=" * 50)


def benchmark_numpy():
    section("NUMPY BENCHMARK")
    a = np.random.rand(2000, 2000)
    start = time.time()
    b = a @ a
    end = time.time()
    print(f"Matrix multiply (2000x2000): {end - start:.4f} seconds")


def benchmark_pandas():
    section("PANDAS BENCHMARK")
    df = pd.DataFrame({
        "a": np.random.rand(3_000_000),
        "b": np.random.rand(3_000_000)
    })
    start = time.time()
    df["c"] = df["a"] + df["b"]
    end = time.time()
    print(f"Vectorized addition (3M rows): {end - start:.4f} seconds")


def benchmark_scipy():
    section("SCIPY BENCHMARK")
    a = np.random.rand(1000, 1000)
    start = time.time()
    linalg.inv(a)
    end = time.time()
    print(f"Matrix inverse (1000x1000): {end - start:.4f} seconds")


def print_system_info():
    section("SYSTEM INFORMATION")
    print(f"OS:\t{platform.system()} {platform.release()}")
    print(f"Python:\t{platform.python_version()}")
    print(f"Machine:\t{platform.machine()}")
    print()


if __name__ == "__main__":
    print_system_info()
    benchmark_numpy()
    benchmark_pandas()
    benchmark_scipy()