if op == "1":
        num = input("Ingresá el número decimal (>= 0): ").strip()
        # Validar que sea un entero positivo
        
        while (num == "") or (not num.isdigit()):
            print("Entrada inválida. Debe ser un entero no negativo sin signos ni puntos.")
            num = input("Reingresá el número decimal (>= 0): ").strip()
        
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