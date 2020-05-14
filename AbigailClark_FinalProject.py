#Abigail Clark
#EE551 WS Final Project
#I pledge my honor that I have abided by the Stevens Honor System

#Import libraries
import numpy as np
import pandas as pd
import plotly.express as px

#read in data
dataframe = pd.read_csv('C:/Users/StevensUser/Documents/Python/CPAP_Data_CSV.csv')

#reformat columns
dataframe = dataframe.rename(columns={'snorring': 'Snoring'})
dataframe['CP Compliant'] = dataframe['CP non compliance =1'].apply(lambda x: 'yes' if x == 0 else 'no')
dataframe['Number of Patients'] = dataframe['CP non compliance =1'].apply(lambda x: 1 if x==1 else 1)
dataframe['BMIRange'] = dataframe['BMI'].apply(lambda x: 'Normal(18.5-24.9)' if x<=24.9
                                                    else('Overweight(25-29.9)' if x<=29.9
                                                         else 'Obese(>=30)'))
dataframe['Sex'] = dataframe['sex (male=1)'].apply(lambda x: 'male' if x== 1 else 'female')
dataframe['Humidification'] = dataframe['humidification (yes=1)'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Hypertension'] = dataframe['Hypertension'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Diabetes'] = dataframe['Diabetes (yes=1)'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Cerebrovascular disease'] = dataframe['Cerebrovascular disease'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Cardiovascular disease'] = dataframe['Cardiovascular disease'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Pulmonary disease'] = dataframe['Pulmonary disease'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Hypnotika'] = dataframe['Hypnotika'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Nycturi']  = dataframe['Nycturi '].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Smoking'] = dataframe['Smoking'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Snoring'] = dataframe['Snoring'].apply(lambda x: 'yes' if x==1 else 'no')
dataframe['Interrupted Breathing'] = dataframe['interupted breathing'].apply(lambda x: 'yes' if x==1 else 'no')

dataframe = dataframe.drop(['CP non compliance =1', 'sex (male=1)', 'humidification (yes=1)', 'Diabetes (yes=1)', 'interupted breathing', 'Nycturi ', 'AHI with CPAP',
                            'nights with CPAP (%)', 'Average CPAP use per night with CPAP (hours)'],1)

#drop null dataset rows
dataframe = dataframe.dropna()
dataframe.info()

fig = px.bar(dataframe, x = "Sex", y = "Number of Patients",
             color = "CP Compliant", barmode = "group", facet_row = "BMIRange",
             facet_col = "Smoking")
fig.show()

fig1 = px.histogram(dataframe, x="BMI", y="Number of Patients",
                    color = "CP Compliant")
fig1.show()

fig2 = px.histogram(dataframe, x="Sex", y="BMI", histfunc = "avg",
                    color = "CP Compliant",
                    barmode = "group",
                    facet_row = "Smoking",
                    facet_col = "Hypertension")
fig2.show()

