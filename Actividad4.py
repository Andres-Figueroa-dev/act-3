import random
from collections import Counter
import unicodedata

# Ejercicio 1: Mostrar el Progreso de la Palabra al Usuario
def mostrar_palabra(palabra, letras_adivinadas):
    estado = ''
    for letra in palabra:
        if letra.lower() in letras_adivinadas:
            estado += letra + ' '
        else:
            estado += '_ '
    return estado.strip()

# Ejercicio 2: Actualizar y Mostrar Intentos Restantes
def actualizar_intentos(letra, palabra, intentos_restantes):
    if letra.lower() not in palabra.lower():
        intentos_restantes -= 1
        print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
    else:
        print("¡Buen trabajo! Has adivinado una letra.")
    return intentos_restantes

# Ejercicio 3: Verificar si el Jugador ha Ganado
def verificar_ganador(palabra, letras_adivinadas):
    for letra in palabra.lower():
        if letra not in letras_adivinadas:
            return False
    return True

# Ejercicio 4: Evitar que el Jugador Ingrese Letras Repetidas
def pedir_letra(letras_ingresadas):
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Debes ingresar una sola letra.")
        elif letra in letras_ingresadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
        else:
            letras_ingresadas.add(letra)
            return letra

# Ejercicio 5: Integrar Todas las Funciones en el Flujo del Juego
def jugar():
    palabra = random.choice(['innovacion', 'programacion', 'python', 'desarrollo'])  # Selección aleatoria de palabras
    letras_adivinadas = set()
    intentos_restantes = 10
    letras_ingresadas = set()

    while intentos_restantes > 0:
        print("\n" + mostrar_palabra(palabra, letras_adivinadas))
        letra = pedir_letra(letras_ingresadas)
        letras_adivinadas.add(letra) if letra in palabra.lower() else None
        intentos_restantes = actualizar_intentos(letra, palabra, intentos_restantes)

        if verificar_ganador(palabra, letras_adivinadas):
            print(f"¡Has ganado! La palabra era '{palabra}'.")
            break
    else:
        print(f"Has perdido. La palabra era '{palabra}'.")

# Ejercicio 6: Implementar Niveles de Dificultad
def seleccionar_dificultad():
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil (15 intentos)")
    print("2. Medio (10 intentos)")
    print("3. Difícil (5 intentos)")
    opcion = input("Introduce 1, 2 o 3: ")
    if opcion == '1':
        return 15
    elif opcion == '2':
        return 10
    elif opcion == '3':
        return 5
    else:
        print("Opción inválida. Se establecerá dificultad media.")
        return 10

# Juego principal que ejecuta la función de dificultad
if __name__ == "__main__":
    intentos_restantes = seleccionar_dificultad()
    jugar()
