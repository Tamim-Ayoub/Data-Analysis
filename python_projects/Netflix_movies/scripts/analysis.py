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


# Another way to plot the most common subscription plans

"""
sns.countplot(data=users,x="subscription_plans")

plt.show()
"""




# Get the most common device types to watch movies on 

common_device_types = watch_history.value_counts("device_type")


print(common_device_types)


# Join users table with watch_history_table

users_watch_history = users.merge(watch_history,how='left'\
                                  ,on='user_id',suffixes=("_users","_wh"))


# Count out how many movies each user watched

movies_watched_user_id = users_watch_history.value_counts('user_id')


movies_watched_user_id = movies_watched_user_id.reset_index()

movies_watched_user_id.columns = ['user_id','movie_count']


print(movies_watched_user_id)

movies_watched_user_name = movies_watched_user_id.merge(users,how='left',on='user_id')\
[["first_name","last_name","movie_count"]].drop_duplicates(keep='first')



print(movies_watched_user_name)


# Most common subscription plans for users

subscription_plans = users.value_counts("subscription_plan").reset_index()

subscription_plans.columns = ["sub_plans","count"]

print(subscription_plans)

sns.barplot(data=subscription_plans, x="sub_plans",y="count")

plt.show()