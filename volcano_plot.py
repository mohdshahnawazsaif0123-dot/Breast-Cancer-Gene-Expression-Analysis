import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Top_Basal_Genes.csv")

plt.figure(figsize=(8,6))
plt.scatter(range(len(data)), data.iloc[:,1])
plt.xlabel("Genes")
plt.ylabel("Log2 Fold Change")
plt.title("Volcano Plot")
plt.savefig("Volcano_Plot.png", dpi=300)
plt.show()
