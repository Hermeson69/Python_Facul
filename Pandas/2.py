import pandas as pd

file_path = 'c:/Users/herme/OneDrive/Área de Trabalho/python/Pandas/Vendas.xlsx'

df = pd.read_excel(file_path)

# print(df.head(11))
# print('\n')
# print(df.shape)
# print('\n')
# print(df.describe())
# # print('\n')
# #print(df[['Produto', 'ID Loja']])

#Pegar linha
#print(df.loc[10])

#Caso queira mais de um linha df.loc[1:X]
#Caso queira pegar de uma loja em especifico
# Vendas_Norte = df.loc[df['ID Loja'] == 'Norte Shopping']
# print(Vendas_Norte.to_string())

#Caso queira pegar so a colunas com loc
#print(df.loc[df['ID Loja'] == 'Norte Shopping', ["ID Loja", "Produto", "Quantidade"]])

#Pega so o especifico print(df.loc[1, "Produto"])

#Adiconar uma coluna nova
df['Comissão'] = df['Valor Final'] * 0.05
print(df)

#No pandas para selecionar todas as linhs coloca-se :

#vendas_df = pd.DataFrame()