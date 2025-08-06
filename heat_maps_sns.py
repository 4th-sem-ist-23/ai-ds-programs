import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd


data = {"Kannada" : [67, 45, 79],
        "English" : [34, 67, 89],
        "Science" : [56, 78, 91]}

names = ["Mithun Kumar", "Thiru Kumar", "Yashwant"]

df = pd.DataFrame(data, index=names)

plt.figure(figsize=(6, 4))
sns.heatmap(df, annot=True, cmap="coolwarm")
plt.title("Student Marks Representation")
plt.tight_layout()
plt.show()