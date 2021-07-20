numeros = []
numero = ''

def lectura(numeros):
    suma=0
    for i in numeros:
        suma += i
    return suma


while numero != '*':
    numero = input('Ingrese un número ("*" para finalizar.) :')
    if numero != '*':
        numeros.append(int(numero))

suma = lectura(numeros)

print(len(numeros))
#print(numeros, '\n' + str(suma))
