import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_style("darkgrid")

x = [2014, 2015, 2016, 2017, 2018, 2019]
y = [1850, 12700, 600, 14560, 8550, 11420]

plt.plot(x, y)
plt.xlabel("Year")
plt.ylabel("Gross Amount")
plt.title("Line Graph")

plt.show()