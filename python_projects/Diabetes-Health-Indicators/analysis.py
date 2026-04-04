import kagglehub 


# Download the Data
#kagglehub.dataset_download("alexteboul/diabetes-health-indicators-dataset",output_dir='./data',force_download=True)

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np


# Read the data
data = pd.read_csv("/home/edward/repos/Data-Analysis/python_projects/Diabetes-Health-Indicators/data/diabetes_012_health_indicators_BRFSS2015.csv")


"""Checking the integrity of the data"""

print(data.head(),'\n')

print(data.info(),'\n')

print(data.shape,'\n')

"""Integrity checked. No missing values detected"""



""" Add a column to change the data types of Diabetes_012 from 0,1,2 to : Diabetic for having diabetes, 
and Healthy for healthy people. This is useful for simplifying the analysis
"""

data["Diabetes_yes_no"] = data["Diabetes_012"].apply(lambda x: "Diabetic" if x > 0 else "Healthy")


print(data.head())