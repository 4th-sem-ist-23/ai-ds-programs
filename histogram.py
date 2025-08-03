#plot a graph using two histograms on single chart with matplotlib take a random number
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
x1=np.random.normal(-2,2,1000)
y2=np.random.normal(2,2,1000)
sns.histplot(x1)
sns.histplot(y2)
plt.title("histogram")
plt.legend(['x1','y2'])
plt.show()