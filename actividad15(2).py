import random

def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(0, 100))
        lista.sort()
    return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n = int(input())

aleatorios = listaAleatorios(n)
print(aleatorios)

n = input ("Escribe la frase o el texto")
a = input ("Qué letra quieres contar")

print(f'La frase tiene {n.count(a)}')
