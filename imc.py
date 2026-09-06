import os
import random
def borrar():
    os.system("cls"if os.name=="nt"else"clear")


def imc():
    while True:
        opciones=input("¿Quieres calcular tu imc? Si/No? ")
        opciones = opciones.lower()
        if opciones == "si":
            borrar()
            nombre=input("Introduce tu nombre: ")
            bajo=[
                    f"{nombre}, el imc calculado es menor al recomendado se recomienda que tomas acciones respecto a tu salud",
                    f"Estimado {nombre}, el imc que calculamos para ti es menor al recomendado por la OMS, recomendamos que consultes con un experto",
                    f"{nombre}, Te recomiendo encarecidamente que te contactes con un experto de la salud para que te de recomendaciones respecto a tu salud, debido a tu bajo imc"]
            normal=[
                    f"{nombre}, me alegro que estes dentro de un rango normal de IMC, sigue asi!"
                    f"{nombre}, estas en un rango de IMC normal",
                    f"Estimado {nombre}, el imc calculado para ti esta dentro del rango normal"
                    ]
            sobre = [
                    f"{nombre}, el IMC calculado para ti indica sobrepeso, se recomienda que tomes acciones respecto a tu salud",
                    f"Estimado {nombre}, el IMC que calculamos para ti indica sobrepeso, recomendamos que consultes con un experto para recibir orientación",
                    f"{nombre}, te recomiendo que consultes con un experto de la salud para recibir recomendaciones respecto a tu salud, debido a que tu IMC se encuentra por encima del rango recomendado"
                    ]

            obs = [
                    f"{nombre}, el IMC calculado para ti indica obesidad, se recomienda que tomes acciones respecto a tu salud",
                    f"Estimado {nombre}, el IMC que calculamos para ti indica obesidad, recomendamos que consultes con un experto para recibir orientación",
                    f"{nombre}, te recomiendo encarecidamente que te contactes con un experto de la salud para recibir recomendaciones respecto a tu salud, debido a que tu IMC se encuentra considerablemente por encima del rango recomendado"
                    ]   

            peso=input("Cuanto pesas (en kg): ")
            try:
                float(peso)
                peso = float(peso)
                altura=input("Introduce tu altura en metros: ")
                try:
                    float(altura)
                    altura=float(altura)
                    altura2=altura**2
                    imc = peso/altura2
                    borrar()
                    print(f"Tu imc es: {imc}")
                    if imc<18.5:
                        print(random.choice(bajo))
                        
                    elif 18.5<imc<=24.9:
                        print(random.choice(normal))
                        
                    elif 24.9<imc<30:
                        print(random.choice(sobre))
                        
                    elif imc>=30:
                        print(random.choice(obs))
                        
                except ValueError:
                    print("Introduce un numero valido! ")
            except ValueError:
                print("Introduce un numero valido! ")
        elif opciones == "no":
            borrar()
            break
        else:
            print("Introduce una opcion valida")
