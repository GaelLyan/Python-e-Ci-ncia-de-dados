import pandas as pd

dados = pd.read_csv("academia.csv")

# Filtrar alunos que treinam mais de 5 horas
filtro = dados[dados["Horas_Treino"] > 5]

print(filtro)
