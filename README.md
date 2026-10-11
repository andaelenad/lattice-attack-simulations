
# Lattice-Based Cryptography: ML-KEM Attack Simulations & Empirical Profiling

This repository contains the empirical data, source code, and experimental frameworks developed for my undergraduate thesis on Post-Quantum Cryptography (PQC). The research evaluates the NIST-standardized Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM / FIPS 203).

## Research Objectives
1. **Empirical Profiling:** Benchmarking the exact execution latency and peak memory footprint (heap/stack allocation) of the official ML-KEM-512 reference implementation.
2. **Cryptanalytic Simulation:** Modeling the computational complexity, required BKZ block sizes ($\beta$), and hardware limits of Primal (uSVP) and Dual Hybrid lattice reduction attacks.

---

##  System Requirements & Environment

To accurately reproduce these experiments, the environment must strictly mirror the testing conditions utilized in the thesis.

### Hardware Baseline
* **CPU:** Intel Core i5 (10th Gen Ice Lake or newer recommended for AVX2/AVX-512 hardware acceleration)
* **RAM:** Minimum 8.00 GB (Serves as the physical baseline for the thermodynamic and memory limit proofs)
* **OS:** Windows Subsystem for Linux (WSL 2) - Ubuntu 24.04 LTS

### Software Toolchain & Dependencies
* **C/C++ Environment:** `gcc`, `make` (for compiling NIST KAT binaries)
* **Memory Profiler:** `valgrind` (specifically the Massif heap profiler tool)
* **Mathematics & Scripting:** Python 3.11, `conda`, `SageMath`
* **Cryptanalytic Libraries:** `lattice-estimator` (by Martin Albrecht et al.)

---

##  Installation & Setup Guide

Execute the following commands in your Linux/WSL terminal to prepare the experimental environment from scratch.

### 1. Install Base Linux Packages (For Performance Profiling)
Update your package manager and install the C compiler and memory profiling tools required for Experiment 1:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential gcc make valgrind -y

```

### 2. Configure the Cryptanalytic Environment (SageMath)

Because SageMath relies on complex mathematical dependencies, it must be installed within an isolated Conda environment.

```bash
# Install Miniconda (Skip if Anaconda/Miniconda is already installed)
mkdir -p ~/miniconda3
wget [https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
source ~/miniconda3/bin/activate

# Create the dedicated cryptographic environment and install SageMath
conda create -n crypto_env -c conda-forge sagemath python=3.11 -y
conda activate crypto_env

```

### 3. Install the Lattice Estimator

With the `crypto_env` activated, install the Lattice Estimator directly from its official repository to ensure the latest cryptanalytic models are used:

```bash
pip install git+[https://github.com/malb/lattice-estimator.git](https://github.com/malb/lattice-estimator.git)

```

---

##  Running the Experiments

### Experiment 1: Performance Profiling (ML-KEM-512)

This test measures the CPU execution time and RAM footprint for 100 deterministic cryptographic lifecycles (Key Generation, Encapsulation, Decapsulation) using the official NIST Known Answer Tests (KAT).

```bash
# 1. Measure execution latency (POSIX Timer)
time ./nistkat/PQCgenKAT_kem512

# 2. Profile peak memory allocation using Valgrind Massif
valgrind --tool=massif ./nistkat/PQCgenKAT_kem512

# 3. Read the generated memory graph
ms_print massif.out.* | head -n 30

```

**Results Verified:** Execution latency of `0.080s` and a peak memory footprint of `349.7 KB`.

### Experiment 2: BKZ Attack Cost Simulation

This script models the mathematical parameters of ML-KEM-512 ($n=512, q=3329, \eta=3$) to calculate the required BKZ Block Size ($\beta$) needed to compromise the system.

```bash
# Ensure the cryptography environment is active
conda activate crypto_env

# Execute the simulation
sage --python my_attack.py

```

**Results Verified (Primal Attack - uSVP):**

* Required BKZ Block Size ($\beta$): `406`
* Computational Cost: `$\approx 2^{118.6}$ operations`

> **Note on Hardware Limits:** As discussed in the thesis, executing a Sieving algorithm with $\beta=406$ requires approximately $3.3 \times 10^{35}$ bytes of RAM (300 Billion Yottabytes). This vastly exceeds the thermodynamic limits of conventional computing, proving ML-KEM-512's real-world security.

---

## References

* **NIST FIPS 203:** Module-Lattice-Based Key-Encapsulation Mechanism Standard (August 2024).
* **Lattice Estimator:** Albrecht, M. R., et al. *"Estimate all the {LWE, NTRU} schemes!"*

```

```
