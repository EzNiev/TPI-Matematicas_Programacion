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

    # Conversión BINARIO a DECIMAL
    elif op == "2":
        # Pedimos una cadena de 0s y 1s. Validamos manualmente cada carácter para evitar estructuras complejas.
        numBin= input("\nIngresá un número binario (solo 0 y 1): ").strip()

        # Validación del binario: no vacío y cada carácter debe ser '0' o '1'.
        # Usamos un bucle while para repetir hasta que sea correcto.
        es_valido = False  # asumimos inválido hasta verificar
        while not es_valido:
            es_binario = True #Asumimos que la cadena es binaria, si se encuentra un error la cambiamos a false

            if numBin == "":
                print("Entrada inválida. No puede estar vacía.")
                es_binario = False
            else:
                # Recorremos cada carácter y revisamos que sea 0 u 1.
                i = 0
                while i < len(numBin) and es_binario:
                    caracter = numBin[i]
                    if caracter != "0" and caracter != "1": #si se encuentra un caracter que no 0 ni 1 corta el bucle
                        es_binario = False
                        break

                    i = i + 1

            if es_binario:
                es_valido = True
            else:
                print("Entrada inválida. Solo se permiten dígitos 0 y 1.")
                numBin= input("\nReingresá un número binario (solo 0 y 1): ").strip()

        # Convertimos el binario validado a decimal usando acumulación por base 2.
        # Recorremos de izquierda a derecha: acumulador = acumulador * 2 + dígito
        decimal = 0
        i = 0
        while i < len(numBin):
            dig = int(numBin[i])     # seguro: solo 0 o 1
            decimal = decimal * 2 + dig
            i += 1
        print(f"El número binario {numBin} equivale a {decimal} en decimal.")

    elif op == "3":
        print("Saliendo.")
        break

    # Manejo de errores de tipeo
    else:
        print("Opción no válida. Debe elegir 1 o 2. Se vuelve al menú pirincipal")
