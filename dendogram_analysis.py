import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

data = pd.read_csv("Top_Basal_Genes.csv")

X = data.select_dtypes(include='number')

linked = linkage(X, method='ward')

plt.figure(figsize=(12,8))
dendrogram(linked)
plt.title("Hierarchical Clustering")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.savefig("Dendrogram.png", dpi=300)
plt.show()
