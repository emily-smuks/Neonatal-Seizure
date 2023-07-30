from MaybeEpilepticBaby import MaybeEpilepticBaby, sample_probability

n_samples = 5000
n_seizing = 0
for _ in range(n_samples):
    meb = MaybeEpilepticBaby()
    n_seizing += meb.hasSeizure

print(f"Proportion babies epileptic: {n_seizing}/{n_samples} ({n_seizing/n_samples})")
