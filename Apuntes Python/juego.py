import random


vidas = 5
puntos = 0


while vidas != 0:

    num = random.randint(0,9)
    
    if num == 0:
        vidas -=1
        print(f"Te quedan {vidas} vidas")
    else:
        puntos += 1
        print(f"Has ganado {puntos} puntos")