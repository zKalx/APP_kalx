import os
import random
def biblio():
    libros = []
    def borrar():
        os.system("cls"if os.name == "nt" else "clear")
    def mostrar():
        for posicion, libro in enumerate(libros):
            print(f"[{posicion}] Nombre del libro: {libro['nombre']}\nAutor del libro: {libro['autor']}\nFecha de lanzamiento: {libro['fecha']}\n-------------------------------")
    while True:
        print("Biblioteca v1 by zKalx\n\n\n")
        print("[1] Añadir libro\n[2] Eliminar libro\n[3] Listar Libros\n[4] Buscar libro\n[5] Salir")
        opi = input("Elige la opcion que desees: ")
        if opi.isdigit():
            borrar()
            opi = int(opi)
            if opi == 1:
                name = input("Nombre del libro que deseas añadir: ")
                author = input("Nombre del autor: ")
                date = input("Fecha de lanzamiento: ")
                libro = {
                    "nombre": name,
                    "autor": author,
                    "fecha": date,
                }
                libros.append(libro)
                borrar()
            elif opi == 2:
                borrar()
                mostrar()
                brar = input("Que opcion deseas borrar: ")
                sgr = input(f"Estas apunto de borrar el libro de la posicion numero {brar}, estas seguro? Si/No: ")
                sgr = sgr.lower()
                if sgr == "si":
                    if brar.isdigit():
                        brar = int(brar)
                        if 0<=brar<len(libros):
                            libros.pop(brar)
                        else:
                            print("Esa posicion no existe ")
                    else:
                        print("Introduce un numero ")
                else:
                    print("Volviendo al menu principal...")
            elif opi == 3:
                borrar()
                mostrar()
            elif opi == 4:
                borrar()
                search = input("Nombre del libro que buscas: ")
                for libro in libros:
                    encontrado = False
                    if search.lower() in libro["nombre"].lower():
                        print(libro)
                        encontrado = True
                    if not encontrado:
                        print("No se a encontrado titulos similares")
            elif opi ==5:
                borrar()
                break
            else:
                print("Introduzca una opcion correcta ")
        else:
            print("Solo numeros!!")
