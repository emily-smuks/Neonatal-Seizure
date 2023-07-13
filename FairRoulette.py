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
  
class Baby():
  def __init__(self, probSmokes, probEpilepsyGivenSmokes, probEpilepsyGivenNonSmokes):
    self.motherSmokes = random.choice(range(100)) < probSmokes
    if self.motherSmokes:
      self.hasEpilepsy = random.choice(range(100)) < probEpilepsyGivenSmokes
    else:
      self.hasEpilepsy = random.choice(range(100)) < probEpilepsyGivenNonSmokes
  def __str__(self):
    return 'MaybeEpilepticBaby'
    