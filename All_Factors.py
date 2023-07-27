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

# Should probEpilepsyGivenSSRI be higher?
class Baby():
  def __init__(self, probSmokes=0.0722, probPreTermGivenSmokes=0.093, probEpilepsyGivenSmokes=0.00042, probEpilepsyGivenPreTerm=0.07, probOpioid=0.07, probAbusesOpioid=0.2, probNASGivenAbuse=0.75, probEpilepsyGivenAbusesOpioids=0.06, probAlcohol=0.27, probFASDgivenAlcohol=0.194, probPretermGivenFASD=.184, probEpilepsyGivenFASD=0.177, probSSRI=0.09, probFirstTrimesterSSRI=0.64, probSecondTrimesterSSRI=0.35, probThirdTrimesterSSRI=0.34, probEpilepsyGivenFirstTrimesterSSRI, probEpilepsyGivenSecondTrimesterSSRI, probEpilepsyGivenThirdTrimesterSSRI, probEpilepsyGivenSSRI=0.007, probPreTermControl=0.12, probEpilepsyControl=0.003 ,  probFASDControl, probNASControl):
    self.motherSmokes = sample_probability(probSmokes)
    self.motherOpioid = sample_probability(probOpioid)
    self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
    
    if self.motherOpioid:
      self.motherAbusesOpioids = sample_probability(probAbusesOpioid)
    else:
      self.motherAbusesOpioids = False
    
    if self.motherAlcohol:
      self.isFASD = sample_probability(probFASDgivenAlcohol) # is preterm a subset of FASD or vice versa? Does FASD impact probability of preterm?
    else:
      self.isFASD = False
    if self.isFASD:
        self.isPreTerm = sample_probability(probPretermGivenFASD)
    else: 
        self.isPreterm = False

    if self.motherSSRI:
       self.firstTrimester = sample_probability(probFirstTrimesterSSRI)
    elif not self.firstTrimester: 
        self.secondTrimester = sample_probability(probSecondTrimesterSSRI)
    elif not self.firstTrimester or not self.secondTrimester: 
        self.thirdTrimester = sample_probability(probThirdTrimesterSSRI)
    else: 
        self.hasEpilepsy = sample_probability(probEpilepsyControl)

    if self.firstTrimester:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenFirstTrimesterSSRI)
    elif self.secondTrimester:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenSecondTrimesterSSRI)
    elif self.thirdTrimester:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenThirdTrimesterSSRI)
    else: 
        self.hasEpilepsy = sample_probability(probEpilepsyControl)
    
  
   
       
    
    

       
    
    if self.isPreterm:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenPreTerm)
    elif self.motherSmokes:
        self.hasEpilepsy = sample_probability(probEpilepsyGivenSmokes) 
    elif self.motherAbusesOpioids: 
      self.hasEpilepsy = sample_probability(probEpilepsyGivenAbusesOpioids)
    else:
        self.hasEpilepsy = sample_probability(probEpilepsyControl)
    
    
    

    # does probEpilepsyGivenAbusesOpioid intersect with prob epilepsy given NAS?
    probEpilepsy = probEpilepsyControl*not (self.isPreTerm or self.motherAbusesOpioids or self.isFASD or self.motherSSRI) + \
      probEpilepsyGivenPreTerm*self.isPreTerm + \
      probEpilepsyGivenAbusesOpioids*self.motherAbusesOpioids + \
      probEpilepsyGivenFASD*self.isFASD + \
      probEpilepsyGivenSSRI*self.motherSSRI # is there difference between SSRI NAS and Opioid NAS?
    self.hasEpilepsy = sample_probability(probEpilepsy)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  

