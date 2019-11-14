nome = input("Digite o seu nome: ").lower()
idade = int(input("Digite a sua idade: "))

if (nome == 'pedro'  and idade == 22) or nome == 'drake':
    print('Salve Drake')
elif nome == 'murilo':
    print('Salve Henrique Henrique')
else:
    print('Você não é o Drake')

numero = 0
while numero < 5:
    print(numero)
    numero = numero + 1

lista = ['Cubo Magico','pagode japones','skate','manga com leite']

# for item in lista:
#    print(item)

# for i in range(0, len(lista), 2):
#    print(lista[i])

# for i in range(len(lista)-1, 0, -2):
#    print(lista[i])

for i in range(len(lista)):
    print(lista[i])