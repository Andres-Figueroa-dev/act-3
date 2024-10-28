import random
import os
import csv
from collections import Counter
import requests
from cryptography.fernet import Fernet

# Ejercicio 1: Añadir Palabras al Archivo
def agregar_palabra():
    palabra_nueva = input("Introduce una nueva palabra: ")
    with open('palabras.txt', 'a') as archivo:
        archivo.write(palabra_nueva + '\n')
    print("Palabra añadida exitosamente.")

# Ejercicio 2: Eliminar Palabras Duplicadas del Archivo
def eliminar_duplicados():
    with open('palabras.txt', 'r') as archivo:
        palabras = [linea.strip() for linea in archivo.readlines()]
    palabras_unicas = list(set(palabras))
    with open('palabras_unicas.txt', 'w') as archivo_unicas:
        for palabra in palabras_unicas:
            archivo_unicas.write(palabra + '\n')
    print("Archivo 'palabras_unicas.txt' creado sin duplicados.")

# Ejercicio 3: Ordenar las Palabras Alfabéticamente
def ordenar_palabras():
    with open('palabras.txt', 'r') as archivo:
        palabras = [linea.strip() for linea in archivo.readlines()]
    palabras_ordenadas = sorted(palabras)
    print("Palabras ordenadas alfabéticamente:")
    for palabra in palabras_ordenadas:
        print(palabra)

# Ejercicio 4: Contar la Frecuencia de Letras en las Palabras
def contar_frecuencia_letras():
    with open('palabras.txt', 'r') as archivo:
        palabras = [linea.strip() for linea in archivo.readlines()]
    texto_completo = ''.join(palabras).lower()
    frecuencia = Counter(texto_completo)
    print("Frecuencia de letras:")
    for letra, conteo in frecuencia.items():
        print(f"{letra}: {conteo}")

# Ejercicio 5: Seleccionar Palabras Según su Longitud
def cargar_palabras_por_longitud(longitud):
    with open('palabras.txt', 'r') as archivo:
        palabras = [linea.strip() for linea in archivo.readlines()]
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) == longitud]
    return palabras_filtradas

# Ejercicio 6: Implementar Caché para la Carga de Palabras
_palabras_cache = None

def cargar_palabras():
    global _palabras_cache
    if _palabras_cache is None:
        with open('palabras.txt', 'r') as archivo:
            _palabras_cache = [linea.strip() for linea in archivo.readlines()]
    return _palabras_cache

# Ejercicio 7: Manejo de Archivos CSV
def leer_palabras_csv():
    with open('palabras.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        palabras = [fila[0] for fila in lector]
    print("Palabras desde CSV:")
    for palabra in palabras:
        print(palabra)

# Ejercicio 8: Registrar las Partidas Jugadas en un Archivo
def registrar_partida(resultado, palabra_utilizada):
    with open('historial.txt', 'a') as historial:
        historial.write(f"Resultado: {resultado}, Palabra: {palabra_utilizada}\n")
    print("Resultado registrado en 'historial.txt'.")

# Ejercicio 9: Leer Palabras desde una URL
def leer_palabras_desde_url(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        palabras = respuesta.text.splitlines()
        print("Palabras descargadas:")
        for palabra in palabras:
            print(palabra)
    else:
        print("Error al descargar el archivo.")

# Ejercicio 10: Encriptar las Palabras del Archivo
def encriptar_archivo():
    clave = Fernet.generate_key()
    with open('clave.key', 'wb') as archivo_clave:
        archivo_clave.write(clave)

    fernet = Fernet(clave)
    with open('palabras.txt', 'rb') as archivo:
        datos = archivo.read()
    datos_encriptados = fernet.encrypt(datos)
    with open('palabras_encriptadas.txt', 'wb') as archivo_encriptado:
        archivo_encriptado.write(datos_encriptados)
    print("Archivo encriptado creado como 'palabras_encriptadas.txt'.")

# Ejecución de Ejercicios
if __name__ == "__main__":
    # Descomenta el ejercicio que deseas ejecutar

    # Ejercicio 1: Añadir Palabras al Archivo
    # agregar_palabra()

    # Ejercicio 2: Eliminar Palabras Duplicadas del Archivo
    # eliminar_duplicados()

    # Ejercicio 3: Ordenar las Palabras Alfabéticamente
    # ordenar_palabras()

    # Ejercicio 4: Contar la Frecuencia de Letras en las Palabras
    # contar_frecuencia_letras()

    # Ejercicio 5: Seleccionar Palabras Según su Longitud
    # longitud_deseada = int(input("Introduce la longitud de las palabras: "))
    # palabras_seleccionadas = cargar_palabras_por_longitud(longitud_deseada)
    # print("Palabras seleccionadas:", palabras_seleccionadas)

    # Ejercicio 6: Implementar Caché para la Carga de Palabras
    # palabras = cargar_palabras()
    # print("Palabras en caché:", palabras)

    # Ejercicio 7: Manejo de Archivos CSV
    # leer_palabras_csv()

    # Ejercicio 8: Registrar las Partidas Jugadas en un Archivo
    # registrar_partida("Ganó", "ejemplo")

    # Ejercicio 9: Leer Palabras desde una URL
    # url = 'https://ejemplo.com/palabras.txt'
    # leer_palabras_desde_url(url)

    # Ejercicio 10: Encriptar las Palabras del Archivo
    # encriptar_archivo()
