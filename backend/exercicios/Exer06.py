lista = [37, 52, 73, 91, 49, 67, 19, 64, 58, 22]
listaI = []
listaP = []
for item in lista:
    if item%2:
        listaI.append(item)
    else:
        listaP.append(item)

print("impares: ", listaI)
print("pares: ", listaP)