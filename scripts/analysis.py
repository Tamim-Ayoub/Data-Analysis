import kagglehub as k




import pandas as pd

import matplotlib.pyplot as plt


import seaborn as sns



# Read the CSV files into a DataFrame

users = pd.read_csv("./Files/users.csv")
movies = pd.read_csv("./Files/movies.csv")
watch_history = pd.read_csv("./Files/watch_history.csv")
reviews = pd.read_csv("./Files/reviews.csv")
search_logs = pd.read_csv("./Files/search_logs.csv")



# Most common subscription plans for users

subscription_plans = users.value_counts("subscription_plan")

print(subscription_plans)

sns.countplot(x = subscription_plans)
plt.show()