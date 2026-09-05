
def execute_encriptador():
    import os
    def borrar():
        os.system("cls" if os.name=="nt" else "clear")
    titulo = """Encriptador
                Made by zLelx in
                Python 3.14.3"""
    x = titulo.center(100)
    print(x)

    alfabeto = "abcdefghijklmnopqrstuvwxyzñáéíóúü 0123456789.,!?¿¡:;()-_"
    cifrado = "abczñádefghvwxyéíóúü 0189.,234567!ijklmnopqrstu?¿¡:;()-_"
    cifrado2 = "almno,!?¿¡:pq_uvrsü 0hfgit9.)-wxyzñáébcdekíóúj12345678;("


    #posicion = de que tipo de cifrado quieres convertir
    #paso = a que lo traduces
    def encriptar():
        txt = input("Palabra a traducir: ")
        txt = txt.lower()
        resultado = ""
        for i in txt:
            posicion = alfabeto.index(i)
            paso1 = cifrado[posicion]
            resultado = resultado + paso1
        resultado2 = ""
        for x in resultado:
            nposicion = cifrado.index(x)
            paso2 = cifrado2[nposicion]
            resultado2 = resultado2 + paso2
        print(resultado2)

    def desencriptar():
        res = ""
        txtcript = input("¿Que deseas desencriptar? ")
        for i in txtcript:
            posi = cifrado2.index(i)
            pa1 = cifrado[posi]
            res = res + pa1
        res2 = ""
        for x in res:
            posi2 = cifrado.index(x)
            pa2 = alfabeto[posi2]
            res2 = res2 + pa2
        print(res2)
    def menu():
        print("""Que deseas hacer:
    [1] Encriptar
    [2] Desencriptar
    [3] Salir""")
    while True:
        menu()
        opc = input("Introduce la opcion que desees: ")
        if opc.isdigit():
            borrar()
            opc = int(opc)
            if opc >=1 and opc <=3:
                if opc == 1:
                    encriptar()
                elif opc == 2:
                    desencriptar()
                elif opc ==  3:
                    print("Gracias por usar esta app, ¡Vuelva pronto!")
                    break