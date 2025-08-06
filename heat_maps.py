import numpy as np
import matplotlib.pyplot as plt

# heat map
# creating a heat map

data = np.random.random((12, 12))
plt.imshow(data, cmap="autumn", interpolation="nearest")
plt.title("2-D heat map")
plt.xlabel("Year")
plt.ylabel("Median income")
plt.show()

