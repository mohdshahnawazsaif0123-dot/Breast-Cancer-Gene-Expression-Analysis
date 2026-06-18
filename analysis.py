#PCA_analysis.py
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = pd.read_csv("Top_Basal_Genes.csv")

X = data.select_dtypes(include='number')

pca = PCA(n_components=2)
pcs = pca.fit_transform(X)

plt.figure(figsize=(8,6))
plt.scatter(pcs[:,0], pcs[:,1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Plot - Breast Cancer Samples")
plt.savefig("PCA_Plot.png", dpi=300)
plt.show()

#heatmap_analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Top_Basal_Genes.csv")

plt.figure(figsize=(10,8))
sns.heatmap(data.select_dtypes(include='number'))
plt.title("Top Variable Genes Heatmap")
plt.savefig("Heatmap.png", dpi=300)
plt.show()

#Dendogram_analysis.py
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

#volcano_plot.py
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
