import random


print("""
      //////////////////////////////////////////////////////

        Bienvenido a "Adivina el número", para jugar escribe
        un número para empezar a adivinarlo! Es un número
        entre 1 y 1000
      
      //////////////////////////////////////////////////////
      """)

numero = int(input())
numero_random = random.randint(1,1000)
pasos = 0
while numero != numero_random:
    if numero < numero_random:
        print("Más arriba")
    else:
        print("Más abajo")
    numero = int(input())
    pasos += 1

if numero == numero_random:
    print(f"Felicidades, has ganado! Lo completaste en {pasos} pasos!!")
    