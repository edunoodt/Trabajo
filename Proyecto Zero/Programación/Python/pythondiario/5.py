numeros = []
numero = 0

while numero != '*':
    numero = input('Ingrese un número al azar...\n("*" para finalizar).\n\n')
    numeros.append(int(numero))
    numero = str(numero)

def sum(numeros):
    for n in range(0, len(numeros)):
        print(n)

sum(numeros)