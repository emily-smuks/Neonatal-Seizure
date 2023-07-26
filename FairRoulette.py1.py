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

class Baby():
  def __init__(self, probSmokes, probPreTermGivenSmokes, probEpilepsyGivenPreTerm, probOpioid, probAbusesOpioid, probEpilepsyGivenAbusesOpioids, probAlcohol, probFASDgivenAlcohol, probEpilepsyGivenFASD, probSSRI, probNASGivenSSRI, probEpilepsyGivenNAS, probPreTermControl, probEpilepsyControl, probFASDControl, probNASControl):
    self.motherSmokes = sample_probability(probSmokes)
    self.motherOpioid = sample_probability(probOpioid)
    self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
    if self.motherOpioid:
      self.motherAbusesOpioids = sample_probability(probAbusesOpioid)
    else:
      self.motherAbusesOpioids = False
    if self.motherSmokes:
      self.isPreTerm = sample_probability(probPreTermGivenSmokes)
    else:
      self.isPreTerm = sample_probability(probPreTermControl)
    if self.motherAlcohol:
      self.isFASD = sample_probability(probFASDgivenAlcohol)
    else:
      self.isFASD = False
    if self.motherSSRI:
        self.NAS = sample_probability(probNASGivenSSRI)
    else:
        self.NAS = sample_probability(probNASControl)
    

    probEpilepsy = probEpilepsyControl*(not (self.isPreTerm or self.motherAbusesOpioids or self.isFASD or self.NAS)) + \
      probEpilepsyGivenPreTerm*self.isPreTerm + \
      probEpilepsyGivenAbusesOpioids*self.motherAbusesOpioids + \
      probEpilepsyGivenFASD*self.isFASD + \
      probEpilepsyGivenNAS*self.NAS
    self.hasEpilepsy = sample_probability(probEpilepsy)

  def __str__(self):
      return 'MaybeEpilepticBaby'
  