print("="*40)
print("\nCALCULO DE MÉDIA DA TURMA\n")
print("="*40)

# Variáveis
aprovados = 0
reprovados = 0

# Entrada
nome_turma = input("Qual o nome da turma que será calculada? ")
quantidade_alunos = int(input("Quantos alunos tem na turma? "))

# Processamento e saída
for i in range(1, quantidade_alunos +1 ):
    nome_aluno = input(f"\nQual o nome do aluno da turma {nome_turma}? ")

    nota1 = int(input(f"Qual a primeira nota do aluno {nome_aluno}? "))
    nota2 = int(input(f"Qual a segunda nota do aluno {nome_aluno}? "))
    media_notas = (nota1 + nota2)/2

    if (media_notas >= 60):
        print(f"\nO aluno(a) {nome_aluno} está aprovado.")
        afirmativa = input(f"\nA média de notas do aluno {nome_aluno} é {media_notas}, ele(a) está aprovado, certo?")
        aprovados +=1
    else: 
        print(f"\nO aluno(a) {nome_aluno} está reprovado.")
        afirmativa = input(f"\nA média de notas do aluno {nome_aluno} é {media_notas}, ele(a) está reprovado, certo?")
        reprovados +=1

print(f"\nDo total de alunos, {aprovados} foram aprovados e {reprovados} foram reprovados")