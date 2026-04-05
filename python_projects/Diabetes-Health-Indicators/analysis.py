import kagglehub 


# Download the Data
#kagglehub.dataset_download("alexteboul/diabetes-health-indicators-dataset",output_dir='./data',force_download=True)

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np


# Read the data
data = pd.read_csv("/home/edward/repos/Data-Analysis/python_projects/Diabetes-Health-Indicators/data/diabetes_012_health_indicators_BRFSS2015.csv")

#%%
"""Checking the integrity of the data"""

print(data.head(),'\n')

print(data.info(),'\n')

print(data.shape,'\n')

"""Integrity checked. No missing values detected"""


#%%

"""Add an ID column for each patient"""
data.insert(0,column='PatientID',value=range(1,len(data) + 1))


# Test the new DataFrame
print("ID inserted",'\n')


print(data.head(),'\n')

print(data.info(),'\n')

print(data.shape,'\n')


""" Add a column to change the data types of Diabetes_012 from 0,1,2 to : Diabetic for having diabetes, 
and Healthy for healthy people. This is useful for simplifying the analysis
"""

data["Diabetes_yes_no"] = data["Diabetes_012"].apply(lambda x: "Diabetic" if x > 0 else "Healthy")


print(data.head())



#%%
"""
Get the mean of health factors that are associated with Diabetes, in order to gain insights
on te distribution and effects of health factors on the occurence of Diabetes

"""
diabetes_health_factors_mean = pd.pivot_table(data=data,index='Diabetes_yes_no',values=['HighBP',"HighChol","BMI",'HeartDiseaseorAttack'],aggfunc='mean')


print(diabetes_health_factors_mean,'\n')
#%%

"""Get the mean of other, non health-lifestyle-related factors to see if there is a correlation between """

diabetes_health_lifestyle_mean1 = pd.pivot_table(data=data,index="Diabetes_yes_no",\
                                                values=["PhysActivity","PhysHlth","MentHlth","GenHlth","DiffWalk"],aggfunc='mean')


# Make 2 tables for display convenience
diabetes_health_lifestyle_mean2 = pd.pivot_table(data=data,index="Diabetes_yes_no",\
                                                values=["Smoker","HvyAlcoholConsump",'Fruits','Veggies'],aggfunc='mean')

print(diabetes_health_lifestyle_mean1,'\n')
print(diabetes_health_lifestyle_mean2,'\n')


  
         
"""Evaluate each factor and suggest a mechanism to quantify the risk of developing diabetes"""

"""After observing different health- and lifestyle-factors that can be associated with Diabetes,
The following variables seem to stand out the most:

BMI
HeartDiseaseorAttack
HighBP
HighChol

DiffWalk
PhysActivity

Smoker
Fruits
Veggies
"""

"""Suggested Risk-Caculation Method: Each factor in the above should contribute,according to its values, to an incremental variable
called "Risk-Factor", and depending on the result of the Risk-Factor variable we can quantify
the risk of a person developing diabetes in the future, based on their current life style and health-related issues. 
"""

# Copy the patients' data table with the wanted columns to a new dataframe

columns_to_copy = ["PatientID","BMI","HeartDiseaseorAttack","HighBP","HighChol",\
                   "DiffWalk","PhysActivity","Smoker","Fruits","Veggies"]

patients_risk_matrix = data[columns_to_copy].copy()



# Initiate the Risk_Factor column  
patients_risk_matrix["Risk_Factor"] = 0


def calculate_risk(row):
   if( row['BMI'] > 31):
       row["Risk_Factor"] += 1
      
      
   if (row["HeartDiseaseorAttack"] > 0.2 ):
       row["Risk_Factor"] += 1
   if (row["HighBP"] > 0):
       row["Risk_Factor"] += 1
   if (row["HighCol"] > 1):
       row["Risk_Factor"] += 1


   if (row["HighCol"] > 1):
       row["Risk_Factor"] += 1
        
       
    




patients_risk_matrix["Risk_Factor"] =