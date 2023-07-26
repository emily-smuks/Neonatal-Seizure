import random
random.seed(0)
class Baby():
  def __init__(self, probSmokes, probEpilepsyGivenSmokes, probEpilepsyGivenNonSmokes):
    self.motherSmokes = random.choice(range(27)) < probSmokes
    if self.motherSmokes:
      self.hasEpilepsy = random.choice(range(17.7)) < probEpilepsyGivenSmokes
    else:
      self.hasEpilepsy = random.choice(range(.23)) < probEpilepsyGivenNonSmokes
  def __str__(self):
    return 'Baby'
  def __init__ (self, probOpioid, probEpilepsyGivenOpioid, probEpilepsyGivenNonOpioid): 
    self.Opioid = random.choice(range(7)) < probOpioid
    if self.Opioid:
      self.hasEpilepsy =  random.choice(range(2)) < probEpilepsyGivenOpioid
    else:
      self.hasEpilepsy =  random.choice (range(100)) < probEpilepsyGivenNonOpioid 
  def __str__(self):
      return 'Baby'
  
bb = Baby(probOpioid = 0.1 , probEpilepsyGivenOpioid = 0.1 , probEpilepsyGivenNonOpioid = 0.1 )

import random
CoinFlip = random.choice([True, False])
CoinFlips =  [random.choice([True, False])for x in range(100)]
