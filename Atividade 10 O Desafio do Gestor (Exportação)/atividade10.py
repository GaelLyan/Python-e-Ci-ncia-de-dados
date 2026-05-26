import pandas as pd

dados = pd.read_csv("academia.csv")

# Filtrar alunos que gastaram mais de 400 calorias
elite = dados[dados["Calorias"] > 400]

# Salvar em um novo arquivo CSV
elite.to_csv("alunos_elite.csv", index=False)

print(elite)
