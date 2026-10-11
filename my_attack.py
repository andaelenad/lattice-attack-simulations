from estimator import *

print("--- SIMULATING ATTACK ON ML-KEM-512 ---")
# These are the exact mathematical parameters of NIST's ML-KEM-512
ml_kem_512 = LWE.Parameters(
    n = 512,
    q = 3329,
    Xs = ND.CenteredBinomial(3),
    Xe = ND.CenteredBinomial(3),
    m = 512,
    tag = "ML-KEM-512"
)

# Run the estimator to calculate the required BKZ Block Size (Beta)
results = LWE.estimate.rough(ml_kem_512)

print("\nRESULTS:")
for attack, data in results.items():
    print(f"Attack Type: {attack}")
    print(f"  -> Required BKZ Block Size (Beta): {data.get('beta')}")
    print(f"  -> Computational Cost (log2): 2^{data.get('rop')}\n")
