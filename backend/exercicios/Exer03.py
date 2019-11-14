num = int(input("Entre com o valor: "))
r=0
lista = []

for i in range(0, num):
    value = float(input("Digite a nota {}: ".format(i)))
    lista.append(value)

for item in lista:
    r = item + r
    media = r/num
    
print("A média é: ", media) 