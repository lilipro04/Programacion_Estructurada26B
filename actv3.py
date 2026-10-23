import csv

def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        return list(lector)

def escribir_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)

def ordenamiento_burbuja_id(datos):
    encabezado = datos[0]
    filas = datos[1:]
    
    n = len(filas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(filas[j][0]) > int(filas[j + 1][0]):
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
                
    return [encabezado] + filas

if __name__ == "__main__":
    # Le agregamos 'Actividades/' para que siempre lo encuentre sin importar dónde esté parada la terminal
    archivo_entrada = "Actividades/pacientes_mini.csv"
    archivo_salida = "Actividades/pacientes_ordenados.csv"
    
    datos = leer_archivo_csv(archivo_entrada)
    datos_ordenados = ordenamiento_burbuja_id(datos)
    escribir_archivo_csv(archivo_salida, datos_ordenados)
    
    print("--- PACIENTES ORDENADOS POR ID ---")
    for fila in datos_ordenados:
        print(fila)
        
    print(f"\n¡Listo! Se ha creado el nuevo archivo: '{archivo_salida}' con los datos ordenados.")