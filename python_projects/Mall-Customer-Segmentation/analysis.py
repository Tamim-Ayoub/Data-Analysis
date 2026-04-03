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

categories = ["window_shopper",'budget_conscious','normal_spender','big_spender','extravagant_spender']


data['spending_category'] = np.select(conditions, categories, default='Unknown')

print(data.head(), '\n')

# Sort the data accoring to the Spending Score in descending order.

data_sorted = data.sort_values("spending_score",ascending=False)
print("Data Sorted")
print(data_sorted.head(),'\n')



"""Draw Barplots to visualize relationships"""

fig,axes = plt.subplots(1,3)

# Get the average annual income of shoppers according to their Spending Category

mean_income_to_categroty = data.groupby("spending_category")["annual_income"].mean()

# Order of the labels on the plot and the Labels themselves
order = ["window_shopper","budget_conscious","normal_spender","big_spender","extravagant_spender"]

labels=["Window Shopper"," Budget Conscious","Normal Spender", "Big Spender", "Extravagant Spender"]


g1 = sns.barplot(mean_income_to_categroty,order=order,ax=axes[0])

axes[0].set_title("Annual Income for each Spending Category ")

g1.set_xticklabels(labels=labels,rotation=80)

g1.set_xlabel("Spending Category")
g1.set_ylabel("Annual Income")
print(mean_income_to_categroty,'\n')

# Draw a bar plot showcasing the mean Annual Income against the Spending Category showcasing the difference between each Gender.
                                                         
g2 = sns.barplot(data,x="spending_category",y="annual_income",hue='gender',order=order,ax=axes[1])
g2.set_xticklabels(labels=labels,rotation=80)

g2.set_xlabel("Spending Category")
g2.set_ylabel("Annual Income")
axes[1].set_title("Annual Income for each Spending Category seperated by Gender")


# Draw a bar plot showcasing the mean Age or each Spending Category
g3 = sns.barplot(data,x='spending_category',y='age',ax=axes[2],order=order)

g3.set_xticklabels(labels=labels,rotation=70)

axes[2].set_title("Average Age for each Spending Category")
g3.set_xlabel("Spending Category")
g3.set_ylabel("Age")


plt.tight_layout()
plt.show()




# Make a scatterplot for the Annual Income against the Spending score in betweeen the Spending Category

g4 = sns.scatterplot(data=data,x="annual_income", y="spending_score",hue='spending_category')
g4.set_title("Income vs. Spending Score: The 5 Natural Segments")
g4.set_xlabel("Annual Income")
g4.set_ylabel("Spending Score")



plt.show()