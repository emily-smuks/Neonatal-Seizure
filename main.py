import random
import pandas as pd

n_samples = 10 # Amount of sim neonates
rowlist = ['N' + str(i) for i in range(n_samples)] # Creating a list of names for sim neonates
columnlist = ['P(Alcohol)', 'Alcohol', 'P(FASD | Alcohol)', 'FASD | Alcohol', 'P(NS | FASD)', 'NS | FASD', 'P(Opiods)', 'Opiods', 'P(NAS | Opiods)', 'NAS | Opiods', 'P(NS | NAS)', 'NS | NAS', 'P(Smoker)', 'Smoker', 'P(NS | Smoker)', 'NS | Smoker', 'P(SSRI)', 'SSRI', 'P(NS | SSRI)', 'NS | SSRI']

def prob(list, min, max, n_samples): # Func to determine a probability for a condition between a range for each neonate
    for _ in range(n_samples):
        list.append(random.uniform(min, max))
    return list

def detcond(list_condition, list): # Func to determine whether the neonate suffers from a condition
    for j in list:
        if j >= random.uniform(0, 1):
            list_condition.append(True)
        else:
            list_condition.append(False)
    return list_condition

def probgiven(list_prob, list_condition, min, max, mindefault, maxdefault):
    for k in list_condition:
        if k == True:
            list_prob.append(random.uniform(min, max))
        elif k == False:
            list_prob.append(random.uniform(mindefault, maxdefault)) # Adds range of control probability, excluding given condition
        else:
            print('An error occured')
    return list_prob

# Determining probabilities and which have drinking mothers
probalcohol = []
prob(probalcohol, 0.011, 0.192, n_samples)
hasalcohol = []
detcond(hasalcohol, probalcohol)

# Determining probabilities and which suffer from FASD
probFASD = []
probgiven(probFASD, hasalcohol, 0.00106, 0.11322, 0, 0)
hasFASD = []
detcond(hasFASD, probFASD)

# Determining probabilities and which will suffer from NS as a result of FASD
probNS_FASD = []
probgiven(probNS_FASD, hasFASD, 0.03, 0.21, 0.00081, 0.005)
hasNS_FASD = []
detcond(hasNS_FASD, probNS_FASD)

# Determining probabilities and which mothers consume opiods
probopiods = []
prob(probopiods, 0.00059, 0.099, n_samples)
hasopiods = []
detcond(hasopiods, probopiods)

# Determining probabilities and which suffer from NAS
probNAS = []
prob(probNAS, 0.002, 0.0233, n_samples)
hasNAS = []
detcond(hasNAS, probNAS)

# Determining probabilites and which will suffer from NS as a result of NAS
probNS_NAS = []
probgiven(probNS_NAS, hasNAS, 0.03, 0.21, 0.00081, 0.005)
hasNS_NAS = []
detcond(hasNS_FASD, probNS_FASD)

# Determining probabilities and which smoke
probsmoker = []
prob(probsmoker, 0.07, 0.253, n_samples)
hassmoker = []
detcond(hassmoker, probsmoker)

# Determining probabilities and which will suffer from NS as a result of smoking
probNS_smoker = []
probgiven(probNS_smoker, hassmoker, 0.0123, 0.044, 0.00081, 0.005)
hasNS_smoker = []
detcond(hasNS_smoker, probNS_smoker)

# Determining probabilities and which take SSRI
probSSRI = []
prob(probSSRI, 0.0028, 0.051, n_samples)
hasSSRI = []
detcond(hasSSRI, probSSRI)

# Determining probabilities and which will suffer from NS as a result of SSRI
probNS_SSRI = []
probgiven(probNS_SSRI, hasSSRI, 0.01, 0.093, 0.00081, 0.005)
hasNS_SSRI = []
detcond(hasNS_SSRI, probNS_SSRI)

# Creating dataframe
df = pd.DataFrame(list(zip(probalcohol, hasalcohol, probFASD, hasFASD, probNS_FASD, hasNS_FASD, probopiods, hasopiods, probNAS, hasNAS, probNS_NAS, hasNS_NAS, probsmoker, hassmoker, probNS_smoker, hasNS_smoker, probSSRI, hasSSRI, probNS_SSRI, hasNS_SSRI)), columns = columnlist, index = rowlist)

