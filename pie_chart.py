# Pie chart

import matplotlib.pyplot as plt


state = ["Karnataka", "Delhi", "Hyderabad", "Tamil Nadu", "Maharashtra"]
colors = ["red", "green", "blue", "yellow", "purple"]
median_income = [200211, 102344, 212200, 254103, 301552]
plt.pie(median_income, labels=state, colors=colors, shadow=True, explode=(0, 0, 0, 0, 0.2), radius=1.2, autopct="%1.1f%%")
plt.legend(loc="lower left")
plt.show()
