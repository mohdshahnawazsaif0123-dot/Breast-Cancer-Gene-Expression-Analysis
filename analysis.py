import pandas as pd

genes = pd.read_csv("Top_Basal_Genes.csv")

with open("Basal_100_Probes.txt", "w") as f:
    for x in genes["ID_REF"]:
        f.write(str(x) + "\n")

print("Basal_100_Probes.txt saved")