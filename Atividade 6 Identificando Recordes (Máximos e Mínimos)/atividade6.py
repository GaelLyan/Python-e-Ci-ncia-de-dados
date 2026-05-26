import pandas as pd

dados = pd.read_csv("academia.csv")

# Maior idade
mais_velho = dados["Idade"].max()

# Menor idade
mais_novo = dados["Idade"].min()

print("Maior idade:", mais_velho)
print("Menor idade:", mais_novo)