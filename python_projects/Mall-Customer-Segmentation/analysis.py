import kagglehub 

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

# Download the Data

#kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python",output_dir='./data',force_download=True)



data = pd.read_csv("/home/edward/repos/Data-Analysis/python_projects/Mall-Customer-Segmentation/data/Mall_Customers.csv")


# Examine the data and its integrity (Making sure no missing values exist)
print(data.head(10))
print(data.info())
print(data.shape)



# Change Column names for easier processing

data.columns = ["CustomerID","gender","age","annual_income","spending_score"]



# Make sure no CustomerID value is repeated:

print(data.value_counts("CustomerID") ,'\n')


# Get the correlation between the annual income and the spending behaviour
print("Correlation between Annual Income and Spending Score : ", data["spending_score"].corr(data["annual_income"]), '\n')


# Add a column to categorize the spending_score:

conditions = [
    data["spending_score"] <= 10,
    (data["spending_score"] > 10) & (data['spending_score'] <= 25),
    (data['spending_score'] > 25) & (data['spending_score'] <= 50),
    (data['spending_score'] > 50) & (data['spending_score'] <= 75),
    data['spending_score'] > 75
]

categorizes = ["window_shopper",'budget_conscious','normal_spender','big_spender','extravagent_spender']


data['spending_category'] = np.select(conditions, categorizes, default='Unknown')

print(data.head(), '\n')

# Sort the data accoring to the Spending Score in descending order.

data_sorted = data.sort_values("spending_score",ascending=False)
print("Data Sorted")
print(data_sorted.head(),'\n')



"""Draw Barplots to visualize relationships"""

# Get the average annual income of shoppers according to their Spending Category

mean_income_to_categroty = data.groupby("spending_category")["annual_income"].mean()

# Order of the labels on the plot
order = ["window_shopper","budget_conscious","normal_spender","big_spender","extravagent_spender"]




g1 = sns.barplot(mean_income_to_categroty,order=order)

g1.set_xticklabels(labels=["Window Shopper"," Budget Conscious","Normal Spender", "Big Spender", "Extravagent Spender"],rotation=30)


print(mean_income_to_categroty,'\n')

# Draw a bar plot showcasing the mean annual income against the spending category showcasing the difference between each gender.

g2 = sns.barplot(data,x="spending_category",y="annual_income",hue='gender',order=order)
g2.set_xticklabels(labels=["Window Shopper"," Budget Conscious","Normal Spender", "Big Spender", "Extravagent Spender"],rotation=30)
plt.show()









