# Matriz bidimensional 3 x 3
matriz = [
    [25, 10, 96],
    [17, 2, 16],
    [13, 4,68]
]
print("Matriz original")
print(matriz)

# Metodo de ordenamiento buble_sort
def bubble_sort(fila):
    # algoritmo buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] < fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]

# Ordenar la primera las filas de la matriz
bubble_sort(matriz[1])

print("Primera fila ordenada")
print(matriz)