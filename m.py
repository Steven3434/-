import statistics

def calcular_estadisticas(numeros):
    moda = statistics.mode(numeros)
    mediana = statistics.median(numeros)
    promedio = statistics.mean(numeros)
    
    return moda, mediana, promedio

numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]

moda, mediana, promedio = calcular_estadisticas(numeros)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Promedio: {promedio}")
