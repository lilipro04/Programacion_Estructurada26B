import time

def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

def medir_y_probar(funcion, lista, objetivo):
    inicio = time.perf_counter()
    resultado = funcion(lista, objetivo)
    fim = time.perf_counter()
    
    tiempo_total = fim - inicio
    print(f"{tiempo_total:.6f}")

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    lista1 = [i for i in range(1000)]
    lista2 = [i for i in range(2000)]
    lista3 = [i for i in range(4000)]
    lista4 = [i for i in range(8000)]

    objetivo = 9
    objetivo2 = 98

    print("--- Pruebas de rendimiento ---")
    medir_y_probar(suma_objetivo, lista, objetivo)
    medir_y_probar(suma_objetivo, lista1, objetivo2)
    medir_y_probar(suma_objetivo, lista2, objetivo)
    medir_y_probar(suma_objetivo, lista3, objetivo)
    medir_y_probar(suma_objetivo, lista4, objetivo2)