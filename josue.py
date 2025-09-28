op = "0"
while op != "1" or op != "2":
    # Printeamos un menú básicos, despues le agregaremos más instrucciones...
    print("=== Conversor de Números ===")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")

    # Procesamos la entrada como un string para hacer más facil las validaciones
    op = input("Seleccione una opción (1 o 2): ")

    # Conversión DECIMAL a BINARIO
    if op == "1":
        num = input("Ingrese un número decimal: ")

        # Validar que sea un entero positivo
        if not num.isdigit():
            print("Error: Debe ingresar un número decimal entero positivo.")
        else:
            # El string lo pasamos a INT para hacer operaciones aritmétiucas sin problemas
            n = int(num)
            # Analizamos el caso 0
            if n == 0:
                binario = "0"
            else:
                # Inicializamos la variable en vacio
                binario = ""
                while n > 0:
                    # Vamos rescatando digito por dígito
                    resto = n % 2 # calculamos el bit menos significativo

                    # vamos guardando ese bit en la cadena binario, el primer resto sería el primer digito del numero en binario
                    binario = str(resto) + binario

                    # Al numero n que es int lo vamos dividiendo de a 2, para seguir
                    # con las sucesivas divisiones por 2 como nos enseñaron en matematicas
                    n = n // 2
                    # El while de arriba lo va aseguir dividiendo hasta que el número deje de ser mayor que cero.

            print(f"El número binario es: {binario}")

    # Conversión BINARIO a DECIMAL
    elif op == "2":
        num = input("Ingrese un número binario: ")

        # Validar que sea un entero positivo
        if not num.isdigit():
            print("Error: Debe ingresar un número binario.")
        else:
                # Inicializamos las variable en vacio
            decimal = 0
            num_inv=''
            suma=0
            #Invertimos el número, para luego poder convertirlo a decimal
            for x in range(len(num)-1, -1,-1):
                num_inv+=num[x]
            #Realizamos la converisón a decimal
            for i in range (len(num)):
                resultado=num_inv[i]
                resultado=int(resultado) #Transformamos la variable a INT, para poder operar aritemticament sin problemas
                resultado=resultado*(2**(i))
                decimal+=resultado  
        print(f"El número decimal es es: {decimal}")

    

    # Manejo de errores de tipeo
    else:
        print("Opción no válida. Debe elegir 1 o 2. Se vuelve al menú p´rincipal")