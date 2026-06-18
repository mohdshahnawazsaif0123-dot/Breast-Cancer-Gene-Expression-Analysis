import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Top_Basal_Genes.csv")

plt.figure(figsize=(10,8))
sns.heatmap(data.select_dtypes(include='number'))
plt.title("Top Variable Genes Heatmap")
plt.savefig("Heatmap.png", dpi=300)
plt.show()
