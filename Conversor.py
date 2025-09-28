"""
Conversión de Números: Desarrollen un programa que convierta números decimales a
binarios y, de forma OPCIONAL, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.
"""

"""
Paso a paso sugerido por CHATGPT
Plan paso a paso

Menú inicial
    Preguntar al usuario si quiere convertir:
    Decimal → Binario
    Binario → Decimal

Conversión decimal → binario
    Validar que la entrada sea un número decimal entero no negativo.
    Usar división sucesiva entre 2 para construir el binario manualmente (no usar bin() si querés practicar lógica).
    Mostrar resultado.

Conversión binario → decimal
    Validar que la entrada contenga solo 0 y 1.
    Convertir manualmente (multiplicar cada dígito por potencias de 2).
    Mostrar resultado.

Manejo de errores
    Si la entrada es inválida, mostrar mensaje y terminar o permitir reintento.
"""

# Inicializo op en un numero que fuerce la entrada al bucle while principal:
op = "0"

while op != "1" or op != "2" or op != "3":
    # Printeamos un menú básicos, despues le agregaremos más instrucciones...
    print("=== Conversor de Números ===")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

    # Procesamos la entrada como un string para hacer más facil las validaciones
    op = input("Seleccione una opción (1 o 2): ").strip()

    # Conversión DECIMAL a BINARIO
    if op == "1":
        numBin = input("Ingresá el número decimal (>= 0): ").strip()
        # Validar que sea un entero positivo

        while (numBin == "") or (not numBin.isdigit()):
            print("Entrada inválida. Debe ser un entero no negativo sin signos ni puntos.")
            numBin = input("Reingresá el número decimal (>= 0): ").strip()

        n = int(numBin)
            # Analizamos el caso 0
        if n == 0:
                binario = "0"
        else:
        # Inicializamos la variable en vacio
            binario = ""
            print("-" * 50)
            while n > 0:
                # Vamos rescatando digito por dígito
                resto = n % 2 # calculamos el bit menos significativo

                # vamos guardando ese bit en la cadena binario, el primer resto sería el primer digito del numero en binario
                binario = str(resto) + binario

                print(f'{n} / 2 = {n/2}, resto {resto}.')
                # Al numero n que es int lo vamos dividiendo de a 2, para seguir
                # con las sucesivas divisiones por 2 como nos enseñaron en matematicas
                n = n // 2
                # El while de arriba lo va aseguir dividiendo hasta que el número deje de ser mayor que cero.
            print( "-" * 50)
        print(f"El número binario es: {binario}")

    # Conversión BINARIO a DECIMAL
    elif op == "2":
        # ========================================
        # VALIDACIÓN DE ENTRADA BINARIA CORREGIDA
        # ========================================
        bin_Valido = False
        while not bin_Valido:
            numBin = input("Ingrese un número binario: ").strip()

            # 1 Validar cadena vacía
            if numBin == "":
                print("ERROR: No ingresó nada.")
                continue  # vuelve a pedir

            # 2 Validar que solo contenga '0' y '1'
            es_binario = True
            for car in numBin:
                if car not in ("0", "1"):
                    es_binario = False
                    break

            if not es_binario:
                print("Error: Debe ingresar un número binario (solo 0 y 1).")
                continue  # vuelve a pedir

            # Si pasó ambas validaciones
            bin_Valido = True

        # ========================================
        # CONVERSIÓN A DECIMAL
        # ========================================
        decimal = 0
        longitudNumero = len(numBin)
        print(f'\n--------------------------------------------'
            f'\n----------------- CALCULO ------------------'
            f'\n--------------------------------------------'
            )
        for i in range(longitudNumero):
            potencia = 2 ** (longitudNumero - (i + 1))
            digito = int(numBin[i])
            resultado = digito * potencia
            decimal += resultado
            print(f"Posición {i}: bit={digito} → {digito}×2^{longitudNumero - (i + 1)} = {resultado} → Acumulado: {decimal}")
        print("-" * 50)
        print(f"El número decimal final es: {decimal}")

    elif op == "3":
        print("Saliendo.")
        break

    # Manejo de errores de tipeo
    else:
        print("Opción no válida. Debe elegir 1-2-3. Se vuelve al menú principal")
