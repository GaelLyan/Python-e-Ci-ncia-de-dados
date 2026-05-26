import pandas as pd 

dados = {'Frutas': ['Banana', 'Maca', 'Laranja', 'Uva', 'Maracuja'], 'Quantidade': [5, 3, 8, 9, 2],
        'Preco': [9.0, 3.0, 4.0, 2.5, 14.0]}

df = pd.DataFrame(dados)

print(df)
