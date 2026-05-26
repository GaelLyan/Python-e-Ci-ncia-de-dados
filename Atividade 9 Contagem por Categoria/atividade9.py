import pandas as pd

dados = pd.read_csv("academia.csv")

# Contagem de alunos por idade
contagem = dados["Idade"].value_counts()

print(contagem)
