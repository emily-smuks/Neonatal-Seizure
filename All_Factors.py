import random
random.seed(0)

# returns True with probability p 
def sample_probability(p):
  return random.uniform(0,1) < p

# Should probEpilepsyGivenSSRI be higher?probEpilepsyGivenAbusesOpioids
class Baby():
  def __init__(self, probEpilepsyGivenPreTerm=0.07, probSmokingBeforePregnancy=.099, probSmokingFirstTrimesterGivenBefore=0.751,probSmokingSecondTrimesterGivenFirst=0.861, probPretermGivenBefore=0.123,probPretermGivenFirst=0.134, probPretermGivenSecond=0.139, probAbusesOpioid=0.014, probOpioidNASGivenAbuse=0.75, probOpioidNASControl=0, probEpilepsyGivenOpioidNAS=0.065, probAlcohol=0.303, probFASDgivenAlcohol=0.077, probEpilepsyGivenFASD=0.177, probSSRI=.09, probPreTermControl=0.105, probEpilepsyControl=0.002):

    # haven't seen data on seizures due to simple opioid use,
    # so only include opioid abuse
    self.motherAbusesOpioid = sample_probability(probAbusesOpioid)
    self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
    
    if self.motherAbusesOpioid:
      self.hasOpioidNAS = sample_probability(probOpioidNASGivenAbuse)
    else:
      self.hasOpioidNAS = sample_probability(probOpioidNASControl)

    if self.motherAlcohol:
      self.hasFASD = sample_probability(probFASDgivenAlcohol)
    else:
      self.hasFASD = False
    
    self.smokingBeforePregnancy = sample_probability(probSmokingBeforePregnancy)
    if self.smokingBeforePregnancy:
      self.smokingFirstTrimester = sample_probability(probSmokingFirstTrimesterGivenBefore)
    if self.smokingFirstTrimester:
      self.smokingSecondTrimester = sample_probability(probSmokingSecondTrimesterGivenFirst)

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
    probEpilepsy = probEpilepsyControl*not (self.isPreTerm or self.hasOpioidNAS or self.hasFASD or self.motherSSRI) + \
      probEpilepsyGivenPreTerm*self.isPreTerm + \
      probEpilepsyGivenOpioidNAS*self.hasOpioidNAS + \
      probEpilepsyGivenFASD*self.hasFASD + \
      probEpilepsyGivenSSRI*self.motherSSRI

    self.hasEpilepsy = sample_probability(probEpilepsy)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  

