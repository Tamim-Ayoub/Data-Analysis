import kagglehub 


# Download the Data
#kagglehub.dataset_download("dandanjia/vgsales-csv",output_dir='./data')


import os

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np


data = pd.read_csv("/home/edward/repos/Data-Analysis/python_projects/Video_Games_Sales/data/vgsales.csv")




# Checking the integrity of the data
print("Head: \n",data.head(),'\n')

print("INFO \n",data.info(),'\n')

print("Shape: \n",data.shape,'\n')

"""Results: Year and Publisher columns contain missing values"""

print("Rows with missing values: \n",data[data.isna().any(axis=1)])


""" Export the rows that contain missing values to a CSV file to Desktop for further inspection and fixing
"""
#mssing_values_table = data[data.isna().any(axis=1)]

#mssing_values_table.to_csv("missing_values.csv",index=False)


"""Get the indices of the missing values for merging with the edited completed rows"""
#missing_rows_indices = data.index[data.isna().any(axis=1)]

#fixed_values = pd.read_csv("fixed_values.csv")

#data.loc[missing_rows_indices] = fixed_values.values



data = data.dropna()

"""Isolate and analyze all titles that achieved over 20 million units in global sales."""



"""Initiate a 'Era' column to analyse the time period of each game publishing """

data['Era'] = ""
data["Era"] = (data["Year"] // 10 * 10).astype(int).astype(str) + "s"


over_20_mil = data[data['Global_Sales'] >= 20]

print("Games with over 20 Million global sales \n",over_20_mil)


print("Publishers of those games \n",over_20_mil.value_counts('Publisher'))

"""Conclusion: Games with tremendous success are overwhelmingly published by Nintendo, with one from Microsoft
and 2 from Take-Two Interactive """




print('Platformers that those games were published on \n',over_20_mil.value_counts("Platform"))
"""Conclusion: Wii tops the chart with 7 games that managed to get over 20 Mil $, fillowed by Nintendo DS with 4"""


print("Publishers and their platform \n",over_20_mil.groupby(['Platform','Publisher'])['Name'].count())


print('Eras of each game\n', over_20_mil.value_counts('Era'))
"""Conclusion: the 2000s witnessed the golden age of gaming, with 12-over-20-million games published in that decade"""





"""Genre Popularity (Which is considered an indication of Culture Differences)
between Japan's and North America's video games consumers"""

jp_na_per_genre = data.groupby("Genre")[["JP_Sales","NA_Sales"]].sum()

print(jp_na_per_genre)


"""Bar Plot to showcase this relationship"""
jp_na_genre_long_form = data.melt(
    id_vars="Genre",
    value_vars=["JP_Sales", "NA_Sales"],
    var_name="Region",
    value_name="Sales"
)
plt.figure(figsize=(12,6))


sns.barplot(data=jp_na_genre_long_form, x="Genre", y="Sales", hue="Region", estimator="sum")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



"""Conclusion: It seems that the NA gamers have a wider range of interests, whereas Japan players have greater interestin 
Role-Playing games
"""

"""IMP NOTE: Because of the huge difference between the NA population and Japan's population, there can be bias and inaccuarcies
in measuring the 'Trends' and 'Culture Differences' according to sales count without taking into account the population count
of each faction (Japan and North America)


For this reason, an approach of calculating 'Market share per genre' will be used to get the pure analysis of cultrual trends
"""


market_share_per_genre_jp = data.groupby('Genre')['JP_Sales'].sum()/data['JP_Sales'].sum() 


market_share_per_genre_na = data.groupby('Genre')['NA_Sales'].sum()/data['NA_Sales'].sum() 

market_share = pd.DataFrame({'JP': market_share_per_genre_jp,
                             'NA': market_share_per_genre_na})

market_share = market_share.reset_index().melt(id_vars='Genre',value_vars=['JP','NA']
                                               ,var_name='Region',value_name='Market Share')

plt.figure(figsize=(12,6))

sns.barplot(market_share,x='Genre',y='Market Share',hue='Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


"""Conclusion: Japan has an overwhelming desire twoards Role Playing Games, whereas North American gamers prefer  
action games much more than Japanese gamers """




"""Platform Efficiency Study (The Profitability Trap)

Caclulating the mean sales per game for every platform in the dataset

"""

platform_mean_sale_per_game = data.groupby('Platform')['Global_Sales'].mean()

plt.figure(figsize=(12,6))

sns.barplot(data,x='Platform',y='Global_Sales',estimator='mean')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




"""Generate a timeline visualization of Total Global Sales per year (1980–2020)."""

plt.figure(figsize=(12,6))
sns.lineplot(data,x='Year',y='Global_Sales',estimator='sum')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


