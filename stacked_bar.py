# plot grouped and stacked box

import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd


# creating a style
sns.set_style("darkgrid")

# Assigning a value for stacked box

df = pd.DataFrame({'y1' : [2012, 2015, 2014, 2006, 2018],
                   'y2' : [1201, 15021, 2013, 20133, 2206]}, 
                  index=["karnataka", "delhi", "hyderabad", "tamil nadu", "Maharastra"])

df.plot(kind='bar', stacked=True, color=["yellow", "purple"])
plt.title("Stacked Bar")
plt.xlabel("city")
plt.ylabel("median income")
plt.show()
