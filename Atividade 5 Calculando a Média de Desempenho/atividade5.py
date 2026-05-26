import pandas as pd

dados = pd.read_csv("academia.csv")

# Média das horas de treino
media = dados["Horas_Treino"].mean()

print(media)
