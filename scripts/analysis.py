import kagglehub as k




import pandas as pd

import matplotlib.pyplot as plt


import seaborn as sns



# URLs for the data files on Kaggle


path = k.dataset_download("sayeeduddin/netflix-2025user-behavior-dataset-210k-records",output_dir='./Files',force_download=True)

print(path)

""" 
url_users = "https://www.kaggle.com/datasets/sayeeduddin/netflix-2025user-behavior-dataset-210k-records?select=users.csv"

url_movies = "https://www.kaggle.com/datasets/sayeeduddin/netflix-2025user-behavior-dataset-210k-records?select=movies.csv"

url_reviews = "https://www.kaggle.com/datasets/sayeeduddin/netflix-2025user-behavior-dataset-210k-records?select=reviews.csv"

url_search_logs = "https://www.kaggle.com/datasets/sayeeduddin/netflix-2025user-behavior-dataset-210k-records?select=search_logs.csv"

url_watch_history = "https://www.kaggle.com/datasets/sayeeduddin/netflix-2025user-behavior-dataset-210k-records?select=watch_history.csv"



# Reading the data files and converting them to Panda's DataFrames
users = pd.read_csv(url_users)

movies = pd.read_csv(url_movies)

reviews = pd.read_csv(url_reviews)

search_logs = pd.read_csv(url_search_logs)

watch_history = pd.read_csv(url_watch_history)



# Most common subscription plans for users

subscription_plans = users.value_counts("subscription_plan")


 """
