import random
random.seed(0)

"""
p(S|O) = 0.95
p(S) = 0.27
p(O) = 0.1

100: of them, 10 use opioids
   of those 10, 10 smoke

100: of them, 27 smoke
   of those 27, we know 10 use opioids
   the remainder (17) smoke but don't use opioids

p(S|O) + p(S|~O) = p(S)
p(O)

p(A|O) and p(A|S): p(A|O,~S) p(A|O,S), p(A|~O,S)

p(O)
p(A|O)
p(S|O,~A) p(S|O,A), p(S|~O,A)

p(S|O) = 95%
p(s)=9.9%
p(o)= 1.4%

p(s)-p(s|o)= p(s|~o)
.0

231: of them

534: of them 129 opioid
  of those 37 alcohol

534: of them 229 alcohol
  of those 229: 37  opioid
  the remained (100) smoke but dont use opioids= 18.7%

534: of them 129 opioid
  of those, 108 smoke

534: of them 121 smoke
  108 use opioids
13/121= 0.108 smoke but no opioid
"""



# returns True with probability p 
def sample_probability(p):
  return random.uniform(0,1) < p

# Should probSeizureGivenSSRI be higher?probSeizureGivenAbusesOpioids
class MaybeEpilepticBaby():
  def __init__(self,  
               probSmokingBeforePregnancy=.099, 
               probSmokingFirstTrimesterGivenBefore=0.751, 
               probSmokingSecondTrimesterGivenFirst=0.861, 
               probPretermGivenBefore=0.123,
               probPretermGivenFirst=0.134, 
               probPretermGivenSecond=0.139, 
               probAbusesOpioid=0.014, 
               probOpioidNASGivenAbuse=0.75, 
               probOpioidNASControl=0, 
               probAlcohol=0.045, # alcohol ABUSE 
               probFASDgivenAlcohol=0.077, 
               probSSRI=.09, 
               probPreTermControl=0.105, 
               probSeizureGivenPreTerm=0.07, 
               probSeizureGivenOpioidNAS=0.065, 
               probSeizureGivenFASD=0.177, 
               probSeizureGivenSSRI=0.033, 
               probSeizureControl=0.002,
               probSmokesGivenOpioid=.837, # from paper
               probAlcoholGivenOpioid=.287, # from paper
               probOpioidGivenSmokes=0.13, # from paper
               probOpioidGivenAlcohol=0.159 # from paper
               ):

    # P(A|~B) = P(~B|A)P(A) / P(~B)
    # P(A|~B) = (1 - P(B|A))P(A) / P(~B)

    # because P(~B|A) = 1 - P(B|A)

    # calculable parameters
    probSmokesGivenNoOpioid=(1 - probOpioidGivenSmokes)*probSmokingBeforePregnancy/(1-probAbusesOpioid) 
    probAlcoholGivenNoOpioid=(1 - probOpioidGivenAlcohol)*probAlcohol/(1-probAbusesOpioid)

    self.motherAbusesOpioid = sample_probability(probAbusesOpioid)
    # self.motherAlcohol = sample_probability(probAlcohol)
    self.motherSSRI = sample_probability(probSSRI)
   # self.smokingBeforePregnancy = sample_probability(probSmokingBeforePregnancy) #DELETE ME
  
    if self.motherAbusesOpioid:
      self.smokingBeforePregnancy = sample_probability(probSmokesGivenOpioid)
    else:
      self.smokingBeforePregnancy = sample_probability(probSmokesGivenNoOpioid) #not fixed
    
    if self.motherAbusesOpioid:
      self.motherAlcohol = sample_probability(probAlcoholGivenOpioid) #not fixed
    else:
      self.motherAlcohol = sample_probability(probAlcoholGivenNoOpioid) #not fixed

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
#NEW
   
    # NOTE: control should be BELOW observed population incidence, since the observed incidence includes babies with risk factors
    # NOTE: assumes that all factors ADD to each other (additive model)
    # If no primary factor, prob = control. Otherwise, equals sum.
    probSeizure = probSeizureControl * ~(self.isPreterm or self.hasOpioidNAS or self.hasFASD or self.motherSSRI) + probSeizureGivenPreTerm*self.isPreterm + probSeizureGivenOpioidNAS*self.hasOpioidNAS + probSeizureGivenFASD*self.hasFASD + probSeizureGivenSSRI*self.motherSSRI

    self.hasSeizure = sample_probability(probSeizure)

  def __str__(self):
      return 'MaybeEpilepticBaby' 


  
