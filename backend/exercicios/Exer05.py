nome = input("Digite seu nome: ")
countH = int(input("Digite seu banco de horas: "))
cashH = int(input("Digite seu cash por hora: "))

salario = countH * cashH

print("Nome: ", nome)
print("Salario: R$ ", salario)