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

