import os
import random
from itertools import cycle
import time
from generador import execute_generator
from encriptador import execute_encriptador
from biblioteca import biblio
def borrar():
    os.system("cls"if os.name=="nt"else"clear")
while True:
        print("MI APP by zKalx \nv1.0.2\n")
        print("""
        Opciones:
        [1] Encriptador de texto
        [2] Generador de contraseñas
        [3] Biblioteca
        [4] Salir
        """)
        xyz = input("Introduzca la opcion que desee: ")
        if xyz.isdigit():
            xyz = int(xyz)
            if xyz == 1:
                borrar()
                execute_encriptador()
            elif xyz==2:
                borrar()
                execute_generator()
            elif xyz==3:
                borrar()
                biblio()
            elif xyz==4:
                borrar()
                break
            else:
                borrar()
                print("Introduzca una opcion valida")
