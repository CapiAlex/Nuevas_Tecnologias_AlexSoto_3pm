import random

def register_user():
    print("Registro de Usuario")
    name = input("Nombre: ")
    email = input("Email: ")
    phone = input("Teléfono: ")
    while True:
        password = input("Contraseña: ")
        if len(password) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        else:
            break
    
    print("Registro exitoso.")
    return name, email, phone, password

def login_user(email, phone, password):
    while True:
        login_method = input("¿Ingresarás por email o teléfono? ").lower()
        if login_method == "email":
            entered_email = input("Ingresa tu email registrado: ")
            if entered_email == email:
                break
            else:
                print("Email inválido. Inténtalo nuevamente.")
        elif login_method == "teléfono":
            entered_phone = input("Ingresa tu teléfono registrado: ")
            if entered_phone == phone:
                break
            else:
                print("Teléfono inválido. Inténtalo nuevamente.")
        else:
            print("Opción inválida. Por favor, elige 'email' o 'teléfono'.")
    
    while True:
        entered_password = input("Ingresa tu contraseña: ")
        if entered_password == password:
            print(f"Bienvenido, {name}!")
            break
        else:
            print("Contraseña incorrecta. Inténtalo nuevamente.")

print("Bienvenido al sistema de registro e inicio de sesión.")

while True:
    print("\nMenú:")
    print("1. Registrar")
    print("2. Iniciar Sesión")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        name, email, phone, password = register_user()
    elif opcion == '2':
        if 'email' in locals() and 'phone' in locals() and 'password' in locals():
            login_user(email, phone, password)
            while True:
                print("\nMenú 2:")
                print("1. Tarjeta de credito")
                print("2. Juego")
                print("3. Volver")
                opcion2 = input("Seleccione una opción: ")
                if opcion2 == '1':
                    valor_compra= input("Ingrese el valor de la compra: ")
                    n_cuotas = input("Ingrese el numero de cuotas: ")

                    valor_cuota = int(valor_compra)/int(n_cuotas)
                    cupo=0

                    saldo=int(valor_compra)
                    cant_cuota = 0
                    while n_cuotas != 0:
                        cant_cuota +=1
                        if valor_cuota !=0:
                            n_cuotas = int(n_cuotas)-1
                            if cupo==0 and saldo==int(valor_compra) :
                                cupo = valor_cuota
                                saldo = int(valor_compra)- valor_cuota
                            else:
                                cupo += valor_cuota
                                saldo -= valor_cuota

                        print(f"cuota:{cant_cuota}   valor:{valor_cuota}   saldo:{saldo}   cupo:{cupo}")
                elif opcion2 == '2':
                    
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
                elif opcion2 == '3':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        else:
            print("Primero debes registrarte.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")