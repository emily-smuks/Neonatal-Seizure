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
  def __init__(self, probSmokes=0.0722, probEpilepsyGivenPreTerm=0.07, probSmokingBeforePregnancy=.099, probSmokingPastBefore=0.138, probSmokingFirstTrimester=0.074, probSmokingPastFirst=0.064, probSmokingSecondTrimester=0.064, probPretermGivenBefore=0.123, probPretermGivenFirst=0.134, probPretermGivenSecond=0.138, probOpioid=0.07, probAbusesOpioid=0.014, probNASGivenAbuse=0.75, probEpilepsyGivenOpioidNAS=0.065, probAlcohol=0.303, probFASDgivenAlcohol=0.077, probPretermGivenFASD=0.184, probEpilepsyGivenFASD=0.177, probSSRI=.09, probNASGivenSSRI=0.33, probPreTermControl=0.105, probEpilepsyControl=0.002, probEpilepsyGivenOpioidNAS=0.065, probFASDControl=0.0003):
    self.motherSmokes = sample_probability(probSmokes)
    self.motherOpioid = sample_probability(probOpioid)
    self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
    
    if self.motherOpioid:
      self.isNASWithOpioids = sample_probability(probNASGivenOpioid)
    else:
      self.isNAS = sample_probability(NASControl)
    if self.isNASWithOpioids:
      self.hasEpilepsy = sample_probability(probEpilepsyGivenOpioidNAS)
    else:
      self.hasEpilepsy = sample_probability(EpilepsyControl)

     
    

    if self.motherAlcohol:
      self.isFASD = sample_probability(probFASDgivenAlcohol) # is preterm a subset of FASD or vice versa? Does FASD impact probability of preterm?
    else:
      self.isFASD = False
    if self.isFASD:
      self.isPreTerm = sample_probability(probPretermGivenFASD)
    else: 
      self.isPreterm = False


    if self.motherSSRI:
      self.isNASGivenSSRI = sample_probability(probNASGivenSSRI)
    else:
      self.hasEpilepsy = sample_probability(probEpilepsyControl)
    if self.isNASGivenSSRI:
      self.hasEpilepsy = sample_probability(probEpilepsyGivenSSRINAS)
    else:
       self.hasEpilepsy = sample_probability(probEpilepsyControl)
    

    if self.motherSmokes:
      self.smokingBeforePregnancy = sample_probability(probSmokingBeforePregnancy)
    else:
      self.smokingAtOtherTime = sample_probability(probSmokingPastBefore)

    if self.smokingAtOtherTime:
      self.smokingFirstTrimester = sample_probability(probSmokingFirstTrimester)
    else:
      self.smokingPastFirst = sample_probability(probSmokingPastFirst)
    if self.smokingPastFirst:
      self.smokingSecondTrimester = sample_probability(probSmokingSecondTrimester)
    else:
      self.smokingPastSecond = False

    if self.smokingBeforePregnancy:
      self.isPreterm = sample_probability(probEpilepsyGivenBefore)
    elif self.smokingFirstTrimester:
      self.isPreterm = sample_probability(probEpilepsyGivenFirst)
    elif self.smokingSecondTrimester:
      self.isPreterm = sample_probability(probEpilepsyGivenSecond)
    else:
      self.isPreterm = sample_probability(probPreTermControl)





    if self.isPreterm:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenPreTerm)
    else:
        self.hasEpilepsy = sample_probability(probEpilepsyControl)
    
    
    

    # does probEpilepsyGivenAbusesOpioid intersect with prob epilepsy given NAS?
    probEpilepsy = probEpilepsyControl*not (self.isPreTerm or self.motherAbusesOpioids or self.isFASD or self.motherSSRI) + \
      probEpilepsyGivenPreTerm*self.isPreTerm + \
      probEpilepsyGivenAbusesOpioids*self.motherAbusesOpioids + \
      probEpilepsyGivenFASD*self.isFASD + \
      probEpilepsyGivenSSRI*self.motherSSRI + \
        # is there difference between SSRI NAS and Opioid NAS?
      probEpilepsyGivenSmokes*self.motherSmokes

    self.hasEpilepsy = sample_probability(probEpilepsy)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  

