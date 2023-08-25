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
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")



experiment_number = 2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.035, #changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 #changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
print(f"[Experiment #{experiment_number}] AND I halved the probability of seizure due to preterm (in theory I should have found this as a plausible change from some paper)")


experiment_number = 3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.035, #changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.01, #changed
                        probSeizureControl=0.000 #changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
print(f"[Experiment #{experiment_number}] AND I halved the probability of seizure due to preterm (in theory I should have found this as a plausible change from some paper)")
print(f"[Experiment #{experiment_number}] AND I dramatically reduced the effect of SSRIs, since that paper had a very low N so the probability was questionable")

experiment_number = 4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.03, # changed
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
print(f"[Experiment #{experiment_number}] AND I decreased the preterm-control sine it seems likely that the other factors contribute to a lot of the preterm births")

experiment_number = 5
n_seizing[experiment_number], n_preterm[experiment_number] = test_babies_and_preterm(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.0, # changed
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] Proportion babies preterm: {n_preterm[experiment_number]}/{n_samples} ({n_preterm[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
print(f"[Experiment #{experiment_number}] AND I ELIMINATE the preterm-control sine it seems likely that the other factors contribute to a lot of the preterm births")
print(f"[Experiment #{experiment_number}] but the tiny proportion of preterm (1% vs 10% expected) births suggests this is an unrealistic change")


#-----------------mychanges----------------#

experiment_number = 1.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=0, # changed
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0, # changed
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0, #changed
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0, #changed
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134, #changed
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0, #changed
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0, # changed
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0, # changed
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.10
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0, # changed
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0, # changed
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0, #changed
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.13
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=0, #changed
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.14
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0, # changed
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.15
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0, #changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.16
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0, #changed
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.17
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0, #changed
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 1.18
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0, #changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.093, # changed
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.74, #changed
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.855, # changed
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303, 
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.0768, # changed
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.0879, # changed
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0,
                        probAlcohol=0.102, # changed
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.55, # changed
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.8
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.071, # changed
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.9
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.08, #changed
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.11
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.02, # changed
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 2.12
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09, 
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.01, #changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.247, #changed
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.94, # changed
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 3.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.11, # changed
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")


experiment_number = 3.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.132, # changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.0015, # changed
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.3
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.085, # changed
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.4
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.03, # changed
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.5
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.085, # changed
                        probFASDgivenAlcohol=0.024, # changed
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.6
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.03, # changed
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 4.7
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.0138, # changed
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 5.1
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.0015, # changed
                        probOpioidNASGivenAbuse=0.0029, # changed
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")

experiment_number = 5.2
n_seizing[experiment_number] = test_babies(n_samples,
                        probSmokingBeforePregnancy=.099,
                        probSmokingFirstTrimesterGivenBefore=0.751,
                        probSmokingSecondTrimesterGivenFirst=0.861,
                        probPretermGivenBefore=0.123,
                        probPretermGivenFirst=0.134,
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.03, # changed
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.07,
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
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
                        probPretermGivenSecond=0.139,
                        probAbusesOpioid=0.014,
                        probOpioidNASGivenAbuse=0.75,
                        probOpioidNASControl=0.0088,
                        probAlcohol=0.303,
                        probFASDgivenAlcohol=0.077,
                        probSSRI=.09,
                        probPreTermControl=0.105,
                        probSeizureGivenPreTerm=0.057, # changed
                        probSeizureGivenOpioidNAS=0.065,
                        probSeizureGivenFASD=0.177,
                        probSeizureGivenSSRI=0.033,
                        probSeizureControl=0.000 # changed
                        )
print(f"[Experiment #{experiment_number}] Proportion babies epileptic: {n_seizing[experiment_number]}/{n_samples} ({n_seizing[experiment_number]/n_samples})")
print(f"[Experiment #{experiment_number}] In this experiment I made probSeizureControl 0")
