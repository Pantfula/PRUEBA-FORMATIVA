#AUTOR JAIME ESPINOSA
import sys
monto = 0
pedido = True
productos = 0
uno = 0
dos = 0
tres = 0
cuatro = 0

while pedido :
    flag = True
    while flag:
        try:
            print("1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800\nSi desea terminar su orden escoja el 0")
            opcion = int(input("\nEscoja una opción: "))
            while opcion not in [1,2,3,4,0]:
                print("1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800\nSi desea terminar su orden escoja el 0\nAsegurese de que responda entre [1,2,3,4,0]")
                opcion = int(input("\nEscoja una opción: "))
            match opcion:
                case 1:
                    monto += 4500
                    productos += 1
                    uno += 1
                case 2:
                    monto += 5000
                    productos += 1
                    dos += 1
                case 3:
                    monto += 5200
                    productos += 1
                    tres += 1
                case 4:
                    monto += 4800
                    productos += 1
                    cuatro += 1
                case 0:
                    pedido = False
                    break
            flag = False
        except:
            print("Opcion invalida, debe utilizar números")
            flag = True
    if opcion == 0:
        flag = True
        codigo = 0
        while flag:
            try:
                if monto !=0:
                    codigo=int(input("¿Usted posee un codigo de descuento?\nSi su respuesta es si, presione 1, de lo contrario presione 0: "))
                    while codigo not in [0,1]:
                        codigo = int(input("¿Usted posee un codigo de descuento?\nSi su respuesta es si, presione 1, de lo contrario presione 0\nAsegurese de que selecione entre 0 y 1: "))
                    flag = False
                if monto== 0:
                    flag = False
            except:
                print ("Responda con números no con texto")
                flag = True
        if codigo == 1 and monto != 0:
            answer= input("Ingrese su codigo: ")
            if answer == "soyotaku":
                monto2= int(monto * 0.9)
                descuento_calculo= int(monto * 0.1)
            print ("******************************")
            print (f"TOTAL PRODUCTOS: {productos}")
            print ("******************************")
            print (f"Pikachu Roll : {uno}")
            print(f"Otaku Roll : {dos}")
            print(f"Pulpo Venenoso Roll : {tres}")
            print(f"Anguila Eléctrica Roll : {cuatro}")
            print ("******************************")
            print (f"Subtotal a pagar: {monto}")
            print (f"Descuento por código: {descuento_calculo}")
            print (f"TOTAL: ${int(monto2)}")
            if answer != "soyotaku":
                print ("El codigo de descuento no es correcto")
                print("******************************")
                print(f"TOTAL PRODUCTOS: {productos}")
                print("******************************")
                print(f"Pikachu Roll : {uno}")
                print(f"Otaku Roll : {dos}")
                print(f"Pulpo Venenoso Roll : {tres}")
                print(f"Anguila Eléctrica Roll : {cuatro}")
                print("******************************")
                print(f"Subtotal a pagar: {monto}")
                print(f"TOTAL: ${monto}")
        if codigo == 0 and monto != 0:
            print("******************************")
            print(f"TOTAL PRODUCTOS: {productos}")
            print("******************************")
            print(f"Pikachu Roll : {uno}")
            print(f"Otaku Roll : {dos}")
            print(f"Pulpo Venenoso Roll : {tres}")
            print(f"Anguila Eléctrica Roll : {cuatro}")
            print("******************************")
            print(f"Subtotal a pagar: {monto}")
            print(f"TOTAL: ${monto}")
        if codigo == 0 and monto == 0:
            print ("No has escogido nada :(\n")
    flag = True
    while flag and pedido == False:
        try:
            opcion = int(input("Desea usted realizar otra orden (1= SI / 2= NO): "))
            while opcion not in [1,2]:
                opcion = int(input("Desea usted realizar otra orden (1= SI / 2= NO) RESPETE LOS NÚMEROS: "))
            if opcion == 1:
                pedido = True
                monto = 0
                productos = 0
                uno = 0
                dos = 0
                tres = 0
                cuatro = 0
            if opcion == 2:
                print ("Finaliza el programa...")
                sys.exit()
                break
            flag = False
        except SystemExit:
            sys.exit()
            break
        except:
            print ("Respete lo que se le solicita, input invalido")
            flag = True




print(monto)