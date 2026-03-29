import pandas as pd

import matplotlib.pyplot as plt


import seaborn as sns

data = pd.read_csv("Files/health_inequality.csv")


high_exp_data_2001 = data[(data["le_agg_q1_F"] >= 80) & (data["year"] == 2001) ][["statename","le_agg_q1_F"]]


sns.barplot(data= high_exp_data_2001,x="statename",y="le_agg_q1_F")

plt.show()
