import kagglehub 

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


# Download the Data

#kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python",output_dir='./data',force_download=True)



data = pd.read_csv("./data/Mall_Customers.csv")


# Examine the data and its integrity (Making sure no missing values exist)
print(data.head(10))
print(data.info())
print(data.shape)



# Change Column names for easier processing

data.columns = ["CustomerID","gender","age","annual_income","spending_score"]



# Make sure no CustomerID value is repeated:

print(data.value_counts("CustomerID"))

# Sort the data accoring to the Spending Score in descending order.

data_sorted = data.sort_values("spending_score",ascending=False)

print(data_sorted.head())




# Add a column to categorize the spending_score:

conditions = [
    data["spending_score"] <= 10,
    (data["spending_score"] > 10) & (data['spending_score'] <= 25),
    (data['spending_score'] > 25) & (data['spending_score'] <= 50),
    (data['spending_score'] > 50) & (data['spending_score'] <= 75),
    data['spending_score'] > 75
]

categorizes = ["window_shoppers",'budget_conscious','normal_spenders','big_spenders','extravagent_spenders']

