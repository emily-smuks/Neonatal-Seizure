from MaybeEpilepticBaby import MaybeEpilepticBaby, sample_probability

n_samples = 10000

def test_babies(n_babies, **kwargs):
    n_seizing = 0
    for _ in range(n_babies):
        meb = MaybeEpilepticBaby(**kwargs)
        n_seizing += meb.hasSeizure
    return n_seizing

def test_babies_and_preterm(n_babies, **kwargs):
    n_seizing = 0
    n_preterm = 0
    for _ in range(n_babies):
        meb = MaybeEpilepticBaby(**kwargs)
        n_seizing += meb.hasSeizure
        n_preterm += meb.isPreterm
    return (n_seizing, n_preterm)

n_seizing_with_defaults = test_babies(n_samples)
print(f"Proportion babies epileptic: {n_seizing_with_defaults}/{n_samples} ({n_seizing_with_defaults/n_samples})")
print(f"If this proportion is above 0.001-0.005ish, then it's too high! Our assumptions must be wrong. The point of the paper is to write about which ones.")

n_seizing = {}
n_preterm = {}

experiment_number = 2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.55,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.08,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.01, #changed
                        probSeizureGivenOpioidNAS=0.02,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 #changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
print(f"[Experiment #{experiment_number}] AND I halved the probability of seizure due to preterm (in theory I should have found this as a plausible change from some paper)")

