import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

sns.set_style("darkgrid")

# Assiging values

df = pd.DataFrame(
	{
     "Idli" : [6, 8, 10],
     "Masa Dosi" : [6, 8, 13],
     "Pongal" : [2, 5, 4]
	}, index=["Day 1", "Day 2", "Day 3"])

# plot the stacked bar plot

df.plot(kind="bar", stacked=True, color=["yellow", "blue", "green"])
plt.xticks(rotation=0)
plt.xlabel("Hotel Breakfast Items")
plt.ylabel("Number of Plates")
plt.title("Sales Statistics of Three Days")
plt.show()
