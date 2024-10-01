import pandas as pd

# Substitua 'your_absolute_path_to_file' pelo caminho absoluto real do seu arquivo CSV
file_path = 'c:/Users/herme/OneDrive/Área de Trabalho/python/Pandas/pokemon_data.csv'
df = pd.read_csv(file_path)


print('\n')
media = df.mean(numeric_only=True)
moda = df.mode(numeric_only=True)
mediana = df.median(numeric_only=True)
maior_ataque = df['Attack'].max()
pokemon_maior_ataque = df[df['Attack'] == maior_ataque]

print('Pokemon com maior ataque é:\n')
print(pokemon_maior_ataque,'\n')
print('A média de todas as colunas são: \n')
print(media,'\n')
print('\nA Moda de todas as colunas são: \n')
print(moda,'\n')
print('\nA Mediana de todas as colunas são: \n')
print(mediana,'\n')

print(df.to_string)