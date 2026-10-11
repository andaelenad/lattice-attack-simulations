# Lattice Attack Simulations & ML-KEM Profiling

This repository contains the original experimental code and empirical data generated for my undergraduate thesis on lattice-based cryptography. 

The project evaluates the NIST-standardized Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM / FIPS 203) by benchmarking its physical performance on consumer hardware and simulating the theoretical computational cost of Primal and Dual Hybrid attacks.

## Experiment 1: Performance and Memory Profiling
To prove the physical viability of ML-KEM-512, I compiled and profiled the official NIST Known Answer Tests (KAT) reference implementation.

**Tools Used:** GCC, Valgrind Massif, POSIX Timers  
**Environment:** WSL Ubuntu on Intel Core i5 (Ice Lake, AVX2/AVX-512 supported)  

### Execution
```bash
# Measure execution latency for 100 cryptographic lifecycles
time ./nistkat/PQCgenKAT_kem512

# Measure peak RAM allocation
valgrind --tool=massif ./nistkat/PQCgenKAT_kem512
ms_print massif.out.* | head -n 30
