import pandas as pd
from scipy.stats import pearsonr
import plotly.express as px
import matplotlib

df = pd.read_excel('/Users/dchavre/Documents/VS Code/Python/Projects/Neonatal-Seizure/Simulated Neonates.xlsx')

# Making dataframes for each risk factor
df_alcohol = df[['P(Alcohol)', 'Alcohol', 'P(FASD | Alcohol)', 'FASD | Alcohol', 'P(NS | FASD)', 'P(NS)', 'NS']]
df_opiods = df[['P(Opiods)', 'Opiods', 'P(NOWS | Opiods)', 'NOWS | Opiods', 'P(NS | NOWS)', 'P(NS)', 'NS']]
df_smoker = df[['P(Smoker)', 'Smoker', 'P(NS | Smoker)', 'P(NS)', 'NS']]
df_SSRI = df[['P(SSRI)', 'SSRI', 'P(NS | SSRI)', 'P(NS)', 'NS']]

# Sorting and filtering

# Calculating p-value and sorting by p-value
correlation_coefficient, p_value = pearsonr(df_alcohol['P(Alcohol)'], df_alcohol['P(NS)'])
df_alcohol['p-value'] = p_value
correlation_coefficient, p_value = pearsonr(df_opiods['P(Opiods)'], df_opiods['P(NS)'])
df_opiods['p-value'] = p_value
correlation_coefficient, p_value = pearsonr(df_smoker['P(Smoker)'], df_smoker['P(NS)'])
df_smoker['p-value'] = p_value
correlation_coefficient, p_value  = pearsonr(df_SSRI['P(SSRI)'], df_SSRI['P(NS)'])
df_SSRI['p-value'] = p_value

for index, row in df_alcohol.iterrows():
    df_alcohol = df_alcohol.drop(df_alcohol[df_alcohol['p-value'] >= 0.05].index)
for index, row in df_opiods.iterrows():
    df_opiods = df_opiods.drop(df_opiods[df_opiods['p-value'] >= 0.05].index)
for index, row in df_smoker.iterrows():
    df_smoker = df_smoker.drop(df_smoker[df_smoker['p-value'] >= 0.05].index)
for index, row in df_SSRI.iterrows():
    df_SSRI = df_SSRI.drop(df_SSRI[df_SSRI['p-value'] >= 0.05].index)


fig1 = px.scatter(df_alcohol, x = 'P(Alcohol)', y = 'P(NS)', color = 'NS')
fig1.show()