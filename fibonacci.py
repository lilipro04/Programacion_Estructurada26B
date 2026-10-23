import time

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input("Ingrese un número: "))

    inicio = time.time()
    resultado = fibonacci(n)
    fin = time.time()

    print (f"El {n}º número de Fibonacci es: {resultado}")

    final = time.time()
    print (f"Tiempo de ejecución: {final - inicio:.6f} segundos")