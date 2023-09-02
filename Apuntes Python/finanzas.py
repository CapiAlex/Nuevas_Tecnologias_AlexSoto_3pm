def ingresar_ingresos():
    ingresos = []
    ingresos.append(float(input("Ingrese ingresos por salario: ")))
    ingresos.append(float(input("Ingrese ingresos por honorarios: ")))
    ingresos.append(float(input("Ingrese ingresos por pensiones: ")))
    ingresos.append(float(input("Ingrese ingresos por remesas o donaciones: ")))
    return ingresos

def ingresar_egresos():
    egresos = []
    egresos.append(float(input("Ingrese egresos por alimentación: ")))
    egresos.append(float(input("Ingrese egresos por transporte: ")))
    egresos.append(float(input("Ingrese egresos por servicios públicos: ")))
    egresos.append(float(input("Ingrese egresos extras: ")))
    return egresos

def mostrar_lista_y_suma(lista, tipo):
    print(f"\nLista de {tipo}:")
    for item in lista:
        print(f"- ${item}")
    suma = sum(lista)
    print(f"\nTotal de {tipo}: ${suma}")
    return suma

ingresos_totales = []
egresos_totales = []

while True:
    tipo_registro = input("¿Desea agregar un ingreso o un egreso? (Ingrese 'ingreso' o 'egreso', o 'terminar' para finalizar): ")

    if tipo_registro.lower() == 'ingreso':
        print("\nIngrese los tipos de ingresos:")
        ingresos = ingresar_ingresos()
        ingresos_totales.extend(ingresos)

    elif tipo_registro.lower() == 'egreso':
        print("\nIngrese los tipos de egresos:")
        egresos = ingresar_egresos()
        egresos_totales.extend(egresos)

    elif tipo_registro.lower() == 'terminar':
        break

    else:
        print("\nOpción no válida. Por favor, ingrese 'ingreso', 'egreso' o 'terminar'.")

ingresos_suma = mostrar_lista_y_suma(ingresos_totales, "ingresos")
egresos_suma = mostrar_lista_y_suma(egresos_totales, "egresos")

balance = ingresos_suma - egresos_suma

print("\nResumen de transacciones:")
print("-" * 25)
print(f"Total Ingresos: ${ingresos_suma}")
print(f"Total Egresos: ${egresos_suma}")
print("-" * 25)
print(f"Balance General: ${balance}")