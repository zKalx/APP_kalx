import os
import random
from itertools import cycle
import time

def execute_generator():
    cant_caracteres = int()

    letras = "abcdefghijklmnopqrstuvwxyz"

    mayus = letras.upper()

    minus = letras.lower()

    simbolos = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"

    numeros = "0123456789"

    todo = mayus + minus + simbolos + numeros

    comb = [
        mayus,
        minus,
        simbolos,
        numeros,

        mayus + minus,
        mayus + simbolos,
        mayus + numeros,
        minus + simbolos,
        minus + numeros,
        simbolos + numeros,

        mayus + minus + simbolos,
        mayus + minus + numeros,
        mayus + simbolos + numeros,
        minus + simbolos + numeros,

        mayus + minus + simbolos + numeros
    ]

    def borrar():
        os.system("cls"if os.name=="nt" else "clear")
    borrar()
    while True:
        print("[1] Generar contraseña \n[2] Salir")
        opc = int(input("Escoge una opcion: "))
        if opc == 1:
            borrar()
            print("""
        [0] mayus
        [1] minus
        [2] simbolos
        [3] numeros,
        [4] mayus + minus
        [5] mayus + simbolos
        [6] mayus + numeros
        [7] minus + simbolos
        [8] minus + numeros
        [9] simbolos + numeros,
        [10] mayus + minus + simbolos
        [11] mayus + minus + numeros
        [12] mayus + simbolos + numeros
        [13] minus + simbolos + numeros
        [14] mayus + minus + simbolos + numeros""")
            opci = int(input("Introduce la opcion que deesees"))
            def algoritmo():
                borrar()
                ncontra = ""
                cant_caracteres = int(input("Elige el numero de caracteres para tu contraseña. "))
                for i in range(cant_caracteres):
                    ltr = random.choice(comb[opci])
                    ncontra += ltr
                print(f"La contraseña generada es: {ncontra}")
            if opci == 0:
                algoritmo()
            elif opci == 1:
                algoritmo()
            elif opci ==2:
                algoritmo()
            elif opci ==3:
                algoritmo()
            elif opci ==4:
                algoritmo()
            elif opci==5:
                algoritmo()
            elif opci==6:
                algoritmo()
            elif opci == 7:
                algoritmo()
            elif opci == 8:
                algoritmo()
            elif opci == 9:
                algoritmo()
            elif opci == 10:
                algoritmo()
            elif opci == 11:
                algoritmo()
            elif opci == 12:
                algoritmo()
            elif opci == 13:
                algoritmo()
            elif opci==14:
                algoritmo()
            else:
                print("Introduce una opcion correcta! ")
        elif opc == 2:
            break
        else:
            print("Introduce una opcion valida porfavor")