import random
import pandas as pd

n_samples = 10 # Amount of sim neonates
rowlist = ['N' + str(i) for i in range(n_samples)] # Creating a list of names for sim neonates
columnlist = ['Prob FASD', 'Prob NAS']

def prob(list, min, max, n_samples): # Func to determine a probability for a condition between a range for each neonate
    for _ in range(n_samples):
        list.append(random.uniform(min, max))
    return list

def detcond(list_condition, list): # Func to determine whether the neonate suffers from a condition
    for j in list:
        if j >= random.uniform(0, 1):
            list_condition.append(1)
        else:
            list_condition.append(0)
    return list_condition

def probgiven(list_prob, list_condition, min, max):
    for k in list_condition:
        if k == 1:
            list_prob.append(random.uniform(min, max))
        elif k == 0:
            continue
        else:
            print('An error occured')
    return list_prob

# Determining probabilities and which suffer from FASD
probFASD = []
prob(probFASD, 0.00106, 0.11322, n_samples)
hasFASD = []
detcond(hasFASD, probFASD)

# Determining probabilities and which will suffer from NS as a result of FASD
probNS_FASD = []
probgiven(probNS_FASD, hasFASD, 0.03, 0.21)
hasNS_FASD = []
detcond(hasNS_FASD, probNS_FASD)

# Determining probabilities and which suffer from NAS
probNAS = []
prob(probNAS, 0.002, 0.0233, n_samples)
hasNAS = []
detcond(hasNAS, probNAS)

# Determining probabilites and which will suffer from NS as a result of NAS
probNS_NAS = []
probgiven(probNS_NAS, hasNAS, 0.03, 0.21)
hasNS_NAS = []
detcond(hasNS_FASD, probNS_FASD)


