import random
import pandas as pd

n_samples = 1000000 # Amount of sim neonates
rowlist = ['N' + str(i) for i in range(n_samples)] # Creating a list of names for sim neonates
columnlist = ['P(Alcohol)', 'Alcohol', 'P(FASD | Alcohol)', 'FASD | Alcohol', 'P(NS | FASD)', 'P(Opiods)', 'Opiods', 'P(NOWS | Opiods)', 'NOWS | Opiods', 'P(NS | NOWS)', 'P(Smoker)', 'Smoker', 'P(NS | Smoker)', 'P(SSRI)', 'SSRI', 'P(NS | SSRI)', 'P(NS)', 'NS']

def prob(list_prob, min_value, max_value, n_samples): # Determines a probability for a condition between a range for each neonate
    for _ in range(n_samples):
        list_prob.append(random.uniform(min_value, max_value))

def detcond(list_condition, list_prob): # Determines whether the neonate suffers from a condition
    for j in list_prob:
        if j >= random.uniform(0, 1):
            list_condition.append(True)
        else:
            list_condition.append(False)

def probgiven(list_prob, list_condition, min_value, max_value): # Finds the probability given a factor
    for k in list_condition:
        if k == True:
            list_prob.append(float(random.uniform(min_value, max_value)))
        elif k == False:
            list_prob.append(0.0)
        else:
            print('An error occured')

def reeval(list_prob, list_condition_correlated, list_condition, min_value_t, max_value_t, min_value_f, max_value_f, n_samples): # Reevaluates a probability given a new circumstance
    for l in range(n_samples):
        if list_condition_correlated[l] == True:
            if list_condition[l] == False:
                list_prob[l] += random.uniform(min_value_t, max_value_t) # using prob given that the condition is true
            elif list_condition[l] == True:
                continue # since the condition is already true, no need to reevaluate
            else:
                print('An error occured')
        elif list_condition_correlated[l] == False:
            if list_condition[l] == False:
                list_prob[l] += random.uniform(min_value_f, max_value_f) # using prob given that the condition is false
            elif list_condition[l] == True: 
                continue # since the condition is already true, no need to reevaluate
        else:
            print('An error occured')
            
def reeval_detcond_final_probability(list_condition, list_prob):
    for m in range(n_samples):
        if list_prob[m] > 1:
            list_prob[m] = 1
        if list_prob[m] >= random.uniform(0, 1):
            list_condition[m] = True
        else:
            continue

# Determining probabilities and which have drinking mothers
probalcohol = []
prob(probalcohol, 0.011, 0.192, n_samples)
hasalcohol = []
detcond(hasalcohol, probalcohol)

# Determining probabilities and which mothers consume opiods
probopiods = []
prob(probopiods, 0.00059, 0.099, n_samples)
hasopiods = []
detcond(hasopiods, probopiods)

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

# Reevaluating probabilities as the factors are correlated with each other

# Reevaluating alcohol
reeval(probalcohol, hasopiods, hasalcohol, 0.517, 0.801, 0.02976, 0.13851, n_samples)
reeval(probalcohol, hassmoker, hasalcohol, 0.138, 0.633, 0.01098, 0.02925, n_samples)
reeval(probalcohol, hasSSRI, hasalcohol, 0.065, 0.504, 0.02980, 0.20053, n_samples)

# Reevaluating opiods
reeval(probopiods, hasalcohol, hasopiods, 0.02773, 0.413, 0.00996, 0.02771, n_samples)
reeval(probopiods, hassmoker, hasopiods, 0.0074, 0.3443, 0.02487, 0.00575, n_samples)
reeval(probopiods, hasSSRI, hasopiods, 0.02159, 0.4505, 0.01813, 0.09338, n_samples)

# Reevaluating smoking
reeval(probsmoker, hasalcohol, hassmoker, 0.592, 0.95, 0.03558, 0.02044, n_samples)
reeval(probsmoker, hasopiods, hassmoker, 0.88, 0.95, 0.03263, 0.03307, n_samples)
reeval(probsmoker, hasSSRI, hassmoker, 0.207, 0.299, 0.03922, 0.26981, n_samples)

# Reevaluating SSRI
reeval(probSSRI, hasalcohol, hasSSRI, 0.01654, 0.13388, 0.00964, 0.05839, n_samples)
reeval(probSSRI, hasopiods, hasSSRI, 0.1025, 0.2303, 0.00800, 0.05742, n_samples)
reeval(probSSRI, hassmoker, hasSSRI, 0.02368, 0.1915, 0.00822, 0.06819, n_samples)


# Determining final probability and outcome:
reeval_detcond_final_probability(hasalcohol, probalcohol)
reeval_detcond_final_probability(hasopiods, probopiods)
reeval_detcond_final_probability(hassmoker, probsmoker)
reeval_detcond_final_probability(hasSSRI, probSSRI)


# Determining probabilities and which suffer from FASD
probFASD = []
probgiven(probFASD, hasalcohol, 0.00106, 0.11322)
hasFASD = []
detcond(hasFASD, probFASD)

# Determining probabilities and which suffer from NOWS
probNOWS = []
probgiven(probNOWS, hasopiods, 0.002, 0.0233)
hasNOWS = []
detcond(hasNOWS, probNOWS)

# Determining final probabilities of NS from different conditions
probNS_FASD = []
probgiven(probNS_FASD, hasFASD, 0.03, 0.21)
probNS_NOWS = []
probgiven(probNS_NOWS, hasNOWS, 0.021, 0.11)
probNS_smoker = []
probgiven(probNS_smoker, hassmoker, 0.0123, 0.044)
probNS_SSRI = []
probgiven(probNS_SSRI, hasSSRI, 0.01, 0.093)


# Running calculations for final probability of NS
probNS = []
for n in range(n_samples):
    probNS.append(random.uniform(0.00081, 0.005) * (not (hasFASD[n] or hasNOWS[n] or hassmoker[n] or hasSSRI[n])) + probNS_FASD[n] + probNS_NOWS[n] + probNS_smoker[n] + probNS_SSRI[n])

# Determining which will suffer from NS
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

df.to_excel('Simulated Neonates FINAL v2.xlsx')
