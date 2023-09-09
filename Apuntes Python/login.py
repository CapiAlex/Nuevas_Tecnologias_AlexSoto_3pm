import random

def generate_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    captcha_question = f"What is {num1} {operator} {num2}? "
    expected_answer = eval(f"{num1} {operator} {num2}")
    return captcha_question, expected_answer

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
            captcha_question, expected_answer = generate_captcha()
            print("Captcha:", captcha_question)
            user_answer = int(input("Respuesta del Captcha: "))
            
            if user_answer == expected_answer:
                print(f"Bienvenido, {name}!")
                break
            else:
                print("Respuesta de Captcha incorrecta. Inicio de sesión fallido.")
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
        else:
            print("Primero debes registrarte.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")