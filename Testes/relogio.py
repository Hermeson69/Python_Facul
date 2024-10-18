import datetime

# Obter a data e hora local atual
agora = datetime.datetime.now()

# Formatar a data e hora em uma string legível
hora_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")

# Exibir a data e hora formatada
print("Data e hora atual:", hora_formatada)