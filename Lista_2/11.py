def ler_notas():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para sair): ")
        if nome.lower() == 'sair':
            break
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        alunos[nome] = [nota1, nota2]
    return alunos

def calculo_media(alunos, nome):
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        return media
    else:
        return None

def main():
    alunos = ler_notas()
    nome_aluno = input("Digite o nome do aluno: ")
    media = calculo_media(alunos, nome_aluno)
    if media is not None:
        print(f'A média do aluno {nome_aluno} é {media}')
    else:
        print(f'Aluno {nome_aluno} não encontrado')

main()
