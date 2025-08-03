import matplotlib.pyplot as plt
import seaborn as sns 

# Creating a style
sns.set_style("darkgrid")

# Assigning the values of barplot
x = [2014, 2015, 2016, 2017, 2018, 2019]
y = [18500, 12700, 600, 14560, 8550, 11420]

colors = ["yellow", "green", "pink", "purple", "blue", "red"]

plt.bar(x, y , color=colors)
plt.title("Bar Graph")
plt.xlabel("Year")
plt.ylabel("Gross Amount")
plt.show()


