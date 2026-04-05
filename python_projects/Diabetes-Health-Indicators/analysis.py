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
data.insert(0,column='patientID',value=range(1,len(data) + 1))


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


  
         
"""Evaluate """
