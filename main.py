import random
import pandas as pd

n_samples = 10 # Amount of sim neonates
rowlist = ['N' + str(i) for i in range(n_samples)] # Creating a list of names for sim neonates
columnlist = ['P(Alcohol)', 'Alcohol', 'P(FASD | Alcohol)', 'FASD | Alcohol', 'P(NS | FASD)', 'P(Opiods)', 'Opiods', 'P(NOWS | Opiods)', 'NOWS | Opiods', 'P(NS | NOWS)', 'P(Smoker)', 'Smoker', 'P(NS | Smoker)', 'P(SSRI)', 'SSRI', 'P(NS | SSRI)', 'P(NS)', 'NS']

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
probgiven(probFASD, hasalcohol, 0.00106, 0.11322, 0.0, 0.0)
hasFASD = []
detcond(hasFASD, probFASD)

# Determining probabilities and which mothers consume opiods
probopiods = []
prob(probopiods, 0.00059, 0.099, n_samples)
hasopiods = []
detcond(hasopiods, probopiods)

# Determining probabilities and which suffer from NOWS
probNOWS = []
probgiven(probNOWS, hasopiods, 0.002, 0.0233, 0.0, 0.0)
hasNOWS = []
detcond(hasNOWS, probNOWS)

# Determining probabilities and which smoke
probsmoker = []
prob(probsmoker, 0.07, 0.253, n_samples)
hassmoker = []
detcond(hassmoker, probsmoker)

# Determining probabilities and which take SSRI
probSSRI = []
prob(probSSRI, 0.0028, 0.051, n_samples)
hasSSRI = []
detcond(hasSSRI, probSSRI)

# Determining final probabilities and which suffer from NS
probNS_FASD = []
probgiven(probNS_FASD, hasFASD, 0.03, 0.21, 0.0, 0.0)
probNS_NOWS = []
probgiven(probNS_NOWS, hasNOWS, 0.03, 0.21, 0.0, 0.0)
probNS_smoker = []
probgiven(probNS_smoker, hassmoker, 0.0123, 0.044, 0.0, 0.0)
probNS_SSRI = []
probgiven(probNS_SSRI, hasSSRI, 0.01, 0.093, 0.0, 0.0)

probNS = []
for l in range(n_samples):
    probNS.append(random.uniform(0.00081, 0.005) * ~(hasFASD[l] or hasNOWS[l] or hassmoker[l] or hasSSRI[l]) + probNS_FASD[l] * hasFASD[l] + probNS_NOWS[l] * hasNOWS[l] + probNS_smoker[l] * hassmoker[l] + probNS_SSRI[l] * hasSSRI[l])

hasNS = []
detcond(hasNS, probNS)

# Creating dataframe
df = pd.DataFrame(columns = list(columnlist), index = rowlist)
df[columnlist[0]] = probalcohol
df[columnlist[1]] = hasalcohol
df[columnlist[2]] = probFASD
df[columnlist[3]] = hasFASD
df[columnlist[4]] = probNS_FASD
df[columnlist[5]] = probopiods
df[columnlist[6]] = hasopiods
df[columnlist[7]] = probNOWS
df[columnlist[8]] = hasNOWS
df[columnlist[9]] = probNS_NOWS
df[columnlist[10]] = probsmoker
df[columnlist[11]] = hassmoker
df[columnlist[12]] = probNS_smoker
df[columnlist[13]] = probSSRI
df[columnlist[14]] = hasSSRI
df[columnlist[15]] = probNS_SSRI
df[columnlist[16]] = probNS
df[columnlist[17]] = hasNS

print(df)

# df.to_excel('Simulated Neonates.xlsx')