try:    
    while True:
        try:
            lista_numeros = input("Ingresa la lista de números para calcular su promedio (separa los números con espacios)-> ")
            lista_numeros = lista_numeros.split()

            lista_numeros = [float(numero) for numero in lista_numeros]

            suma = sum(lista_numeros)

            promedio = suma / len(lista_numeros)

            print("El promedio de los números es -> ",promedio)

            pregunta = input("¿Quieres hacer otro promedio nuevo? -> (s/n)")
            if pregunta == "s" or pregunta == "S":
                continue
            elif pregunta == "n" or pregunta =="N":
                print("¡ADIOS!")
                break
            else:
                print("No es una respuesta válida, por favor responde con: (s/n)")
                print("\nSiendo s para introducir otra frase y n para salir del script.")

        except ValueError:
            print("ERROR: Ingresa solo números separados por espacios.")
except KeyboardInterrupt:
    print("\nCerrando Script...")