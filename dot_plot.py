import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_style("darkgrid")

# Assign the value to x and y

x = [2014, 2015, 2016, 2017, 2018, 2019]
y = [18500, 12700, 600, 14560, 8550, 11420]

plt.scatter(x, y , marker=".")
plt.xticks(x)
plt.title("Dot Plot")
plt.xlabel("Year")
plt.ylabel("Gross Amount")
plt.show()