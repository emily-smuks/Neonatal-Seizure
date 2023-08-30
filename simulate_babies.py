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

experiment_number = 1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

#-----------------mychanges----------------#

experiment_number = 1.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingFirstTrimesterGivenBefore=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingSecondTrimesterGivenFirst=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probPretermGivenBefore=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probPretermGivenFirst=0.134, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probPretermGivenSecond=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.10
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASControl=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probFASDgivenAlcohol=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.13
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.14
n_seizing[experiment_number] = test_babies(n_samples,
                        probPreTermControl=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.15
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.16
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.17
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenFASD=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.18
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.093, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingFirstTrimesterGivenBefore=0.74, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingSecondTrimesterGivenFirst=0.855, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probPretermGivenBefore=0.0768, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probPretermGivenFirst=0.0879, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.102, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.55, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probFASDgivenAlcohol=0.071, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.08, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0.02, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0.01, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.247, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.94, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0.11, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")


experiment_number = 3.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0.132, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0015, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.085, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenFASD=0.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.085, # changed
                        probFASDgivenAlcohol=0.024, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenSSRI=0.0138, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 5.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0015, # changed
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 5.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.03, # changed
                        probSeizureGivenSSRI=0.0138, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 5.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.093, # changed
                        probSmokingFirstTrimesterGivenBefore=0.07, # changed
                        probSmokingSecondTrimesterGivenFirst=0.855, # changed
                        probPretermGivenBefore=0.0768, # changed
                        probPretermGivenFirst=0.0879, # changed
                        probSeizureGivenPreTerm=0.057, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
