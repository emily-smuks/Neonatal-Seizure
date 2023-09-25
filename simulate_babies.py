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

experiment_number = 1.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

#-----------------mychanges----------------#

experiment_number = 1.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 1.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")

experiment_number = 1.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probOpioidNASGivenAbuse 0 and probSeizureControl 0")

experiment_number = 1.10
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASControl=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probOpioidNASControl 0 and probSeizureControl 0")

experiment_number = 1.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol 0 and probSeizureControl 0")

experiment_number = 1.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probFASDgivenAlcohol=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probFASDgivenAlcohol 0 and probSeizureControl 0")

experiment_number = 1.13
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0 and probSeizureControl 0")

experiment_number = 1.14
n_seizing[experiment_number] = test_babies(n_samples,
                        probPreTermControl=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probPreTermControl 0 and probSeizureControl 0")

experiment_number = 1.15
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenPreTerm 0 and probSeizureControl 0")

experiment_number = 1.16
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenOpioidNAS 0 and probSeizureControl 0")

experiment_number = 1.17
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenFASD=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenFASD 0 and probSeizureControl 0")

experiment_number = 1.18
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenSSRI 0 and probSeizureControl 0")


experiment_number = 2.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.102, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol 0.102 and probSeizureControl 0")

experiment_number = 2.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.55, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probOpioidNASGivenAbuse 0.55 and probSeizureControl 0")

experiment_number = 2.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probFASDgivenAlcohol=0.071, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probFASDgivenAlcohol 0.071 and probSeizureControl 0")

experiment_number = 2.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.08, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 2.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0.02, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenOpioidNAS 0.02 and probSeizureControl 0")

experiment_number = 2.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0.01, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenPreTerm 0.01 and probSeizureControl 0")

experiment_number = 3.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.94, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probOpioidNASGivenAbuse 0.94 and probSeizureControl 0")

experiment_number = 3.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenOpioidNAS=0.11, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenOpioidNAS 0.11 and probSeizureControl 0")


experiment_number = 3.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenPreTerm=0.132, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenPreTerm 0.132 and probSeizureControl 0")

experiment_number = 4.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0015, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0.0015 and probSeizureControl 0")

experiment_number = 4.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probOpioidNASGivenAbuse 0.0029 and probSeizureControl 0")

experiment_number = 4.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.085, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol 0.085 and probSeizureControl 0")

experiment_number = 4.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenFASD=0.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenFASD 0.03 and probSeizureControl 0")

experiment_number = 4.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.085, # changed
                        probFASDgivenAlcohol=0.024, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol 0.085, probFASDgivenAlcohol 0.024, and probSeizureControl 0")

experiment_number = 4.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.03 and probSeizureControl 0")

experiment_number = 4.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSeizureGivenSSRI=0.0138, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureGivenSSRI 0.0138 and probSeizureControl 0")

experiment_number = 5.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0015, # changed
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0.0015, probOpioidNASGivenAbuse 0.0029, and probSeizureControl 0")

experiment_number = 5.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.03, # changed
                        probSeizureGivenSSRI=0.0138, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.03, probSeizureGivenSSRI 0.0138, and probSeizureControl 0")

# experimenting on probalcohol
experiment_number = 6.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.098, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.102, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.064, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.20, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.225, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.587, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.06, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")

experiment_number = 6.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probAlcohol=0.71, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAlcohol else and probSeizureControl 0")


# experimenting on probSmoking

experiment_number = 7.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.102, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.123, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.21, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.245, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.28, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.152, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.072, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.15, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )

experiment_number = 7.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingDuringPregnancy=0.3, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSmokingBeforePregnancy 0 and probSeizureControl 0" )


# probAbusesOpioids

experiment_number = 8.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.07, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0015, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.00314, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.051, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.01, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0004, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")


experiment_number = 8.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probAbusesOpioid=0.0039, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probAbusesOpioid 0 and probSeizureControl 0")

#prob motherSmokes second trimester bc that would include all the other trimesters. 
# CANNOT do third trimester bc of variance in gestation, not as stable and causes uncertainty in literature. 

#probSSRI

experiment_number = 11.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0 and probSeizureControl 0")

experiment_number = 11.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.03, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.03 and probSeizureControl 0")

experiment_number = 11.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=0.023, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0 and probSeizureControl 0")

experiment_number = 11.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.08, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.42
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.1, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.028, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.102, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.023, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.050, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.0007, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")

experiment_number = 11.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSSRI=.013, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSSRI 0.08 and probSeizureControl 0")
