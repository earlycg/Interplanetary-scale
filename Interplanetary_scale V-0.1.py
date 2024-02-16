#--------------------------------------------------------------------#
print(" ", "* " * 12, "\n  Bascula Interplanetaria", "\n", " *" * 12)
#--------------------------------------------------------------------#

import re

to_proceed = 'si'
nombre = ""
masa = 0

def recibir_un_nombre():
    global to_proceed, nombre
    
    while to_proceed == 'si':
        nombre = input("Como te llamas? ").title().strip()

        if nombre.lower() != 'exit' and not re.match("^[A-Za-z\\s]{3,20}$", nombre):
            print("Por favor, ingrese su nombre(s) con solo texto (letras) y sin signos o símbolos o (exit) para salir de la app.")
        elif nombre.lower() == 'exit':
            print("Saliendo de la aplicación.")
            exit()  # Usar exit() para salir del programa
        else:
            break

def recibir_masa():
    global to_proceed, nombre, masa
    
    while to_proceed == 'si':
        masa = input(f"Hola {nombre}\n ¿Indicanos en kilogramos (kg) tu peso o masa corporal en el planeta tierra o (exit) para salir? ").strip()
        
        if masa.lower() == 'exit':
            print("Saliendo de la aplicación.")
            exit()  # Usar exit() para salir del programa
        
        while not re.match("^(?:[1-9]\\d{0,2}|500)$", masa):
            print("Por favor, ingrese su peso solo con un numero  (no mayor a 500 y sin espacios) o (exit) para salir.")
            masa = input(f"Hola {nombre}\n ¿Indicanos en kg tu masa corporal en el planeta tierra o (exit) para salir? ").strip()

        print(masa)
        break

def ecuacion():
    global to_proceed, nombre, masa
    
    planetas = {
        "Sol": 273.70,
        "Mercurio": 3.70,
        "Venus": 8.85,
        "Luna": 1.62,
        "Marte": 3.72,
        "Jupiter": 26.39,
        "Saturno": 11.67,
        "Urano": 11.43,
        "Neptuno": 11.07,
    }

    for planeta, gravedad in planetas.items():
        gravedad = float(gravedad)
        peso_Total = (float(masa) / 9.81) * gravedad
        print(f"{nombre}: Tu peso en el planeta {planeta} es de: {peso_Total:.2f} kg")
    
    to_proceed = input("Desea continuar -SI- o -NO-: ").lower().strip()
    
    while to_proceed != 'si' and to_proceed != 'no':
        print("Entrada no válida. Por favor, ingresa 'si' o 'no' sin espacios ni otros caracteres.")
        to_proceed = input("Desea continuar -SI- o -NO-: ").lower().strip()

# Flujo principal
while to_proceed == 'si':
    recibir_un_nombre()
    recibir_masa()
    ecuacion()

print('Fin del programa.')
