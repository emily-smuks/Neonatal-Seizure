import random
random.seed(0)
class FairRoulette():
  def __init__(self):
    self.pockets = []
    for i in range (1,37):
      self.pockets.append(i)
    self.ball = None
    self.pocketOdds = len(self.pockets) - 1
  def spin(self):
    self.ball = random.choice(self.pockets)
  def betPocket(self, pocket, amt):
    if str(pocket) == str(self.ball):
      return amt*self.pocketOdds
    else: return - amt
  def __str__(self):
    return 'Fair Roulette'

# returns True with probability p 
def sample_probability(p):
  return random.uniform(0,1) < p

# Should probEpilepsyGivenSSRI be higher?probEpilepsyGivenAbusesOpioids
class Baby():
  def __init__(self, probEpilepsyGivenPreTerm=0.07, probSmokingBeforePregnancy=.099, probSmokingFirstTrimesterGivenBefore=0.751,probSmokingSecondTrimesterGivenFirst=0.861, probPretermGivenBefore=0.123,probPretermGivenFirst=0.134, probPretermGivenSecond=0.139, probAbusesOpioid=0.014, probOpioidNASGivenAbuse=0.75, probOpioidNASControl=0, probEpilepsyGivenOpioidNAS=0.065, probAlcohol=0.303, probFASDgivenAlcohol=0.077, probEpilepsyGivenFASD=0.177, probSSRI=.09, probPreTermControl=0.105, probEpilepsyControl=0.002):

    # haven't seen data on seizures due to simple opioid use
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

    if self.isPreterm:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenPreTerm)
    else:
        self.hasEpilepsy = sample_probability(probEpilepsyControl)

    # NOTE: assumes that all factors ADD to each other (additive model)
    probEpilepsy = probEpilepsyControl*not (self.isPreTerm or self.motherAbusesOpioids or self.hasFASD or self.motherSSRI) + \
      probEpilepsyGivenPreTerm*self.isPreTerm + \
      probEpilepsyGivenAbusesOpioids*self.motherAbusesOpioids + \
      probEpilepsyGivenFASD*self.hasFASD + \
      probEpilepsyGivenSSRI*self.motherSSRI + \
        # is there difference between SSRI NAS and Opioid NAS?
      probEpilepsyGivenSmokes*self.motherSmokes

    self.hasEpilepsy = sample_probability(probEpilepsy)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  

