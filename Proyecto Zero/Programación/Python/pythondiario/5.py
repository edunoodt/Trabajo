numeros = []
numero = ''

def lectura(numeros):
    for i in range (0, len(numeros)):
        suma = numeros[i] + numeros[i + 1]
    return suma


while numero != '*':
    numero = input('Ingrese un número ("*" para finalizar.) :')
    if numero != '*':
        numeros.append(int(numero))

suma = lectura(numeros)

print(len(numeros))
#print(numeros, '\n' + str(suma))
