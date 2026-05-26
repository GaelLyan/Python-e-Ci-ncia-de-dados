import pandas as pd

dados = pd.read_csv("academia.csv")

# Criando a coluna IMC
dados["IMC"] = dados["Peso"] / (dados["Altura"] * dados["Altura"])

print(dados)
