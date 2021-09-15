nome = input("Digite seu nome:")
nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("Nota3: "))
media = (nota1+nota2+nota3)/3
print("Aluno:", nome)
print("Media=", media)
if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
