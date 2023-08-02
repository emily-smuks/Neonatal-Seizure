import random
random.seed(0)

# returns True with probability p 
def sample_probability(p):
  return random.uniform(0,1) < p

# Should probSeizureGivenSSRI be higher?probSeizureGivenAbusesOpioids
class MaybeEpilepticBaby():
  def __init__(self,  probSmokingBeforePregnancy=.099, probSmokingFirstTrimesterGivenBefore=0.751,probSmokingSecondTrimesterGivenFirst=0.861, probPretermGivenBefore=0.123,probPretermGivenFirst=0.134, probPretermGivenSecond=0.139, probAbusesOpioid=0.014, probOpioidNASGivenAbuse=0.75, probOpioidNASControl=0,  probAlcohol=0.303, probFASDgivenAlcohol=0.077,  probSSRI=.09, probPreTermControl=0.105, probSeizureGivenPreTerm=0.07, probSeizureGivenOpioidNAS=0.065, probSeizureGivenFASD=0.177, probSeizureGivenSSRI=0.033, probSeizureControl=0.002):

    # haven't seen data on seizures due to simple opioid use,
    # so only include opioid abuse
    self.motherAbusesOpioid = sample_probability(probAbusesOpioid)
    self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
    self.smokingBeforePregnancy = sample_probability(probSmokingBeforePregnancy)
    
    if self.motherAbusesOpioid:
      self.hasOpioidNAS = sample_probability(probOpioidNASGivenAbuse)
    else:
      self.hasOpioidNAS = sample_probability(probOpioidNASControl)

    if self.motherAlcohol:
      self.hasFASD = sample_probability(probFASDgivenAlcohol)
    else:
      self.hasFASD = False
    
    if self.smokingBeforePregnancy:
      self.smokingFirstTrimester = sample_probability(probSmokingFirstTrimesterGivenBefore)
    else:
      self.smokingFirstTrimester = False
    if self.smokingFirstTrimester:
      self.smokingSecondTrimester = sample_probability(probSmokingSecondTrimesterGivenFirst)
    else:
      self.smokingSecondTrimester = False

    if self.smokingSecondTrimester:
      self.isPreterm = sample_probability(probPretermGivenSecond)
    elif self.smokingFirstTrimester:
      self.isPreterm = sample_probability(probPretermGivenFirst)
    elif self.smokingBeforePregnancy:
      self.isPreterm = sample_probability(probPretermGivenBefore)
    else:
      self.isPreterm = sample_probability(probPreTermControl)

    # NOTE: control should be BELOW observed population incidence, since the observed incidence includes babies with risk factors
    # NOTE: assumes that all factors ADD to each other (additive model)
    # If no primary factor, prob = control. Otherwise, equals sum.
    probSeizure = probSeizureControl * ~(self.isPreterm or self.hasOpioidNAS or self.hasFASD or self.motherSSRI) + probSeizureGivenPreTerm*self.isPreterm + probSeizureGivenOpioidNAS*self.hasOpioidNAS + probSeizureGivenFASD*self.hasFASD + probSeizureGivenSSRI*self.motherSSRI

    self.hasSeizure = sample_probability(probSeizure)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  

