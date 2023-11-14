

    if choice == "1":
        char = input("Ingrese un carácter: ")
        ascii_value = char_to_ascii(char)
        binary_representation = ascii_to_binary(ascii_value)
        print(f"La representación en byte de '{char}' es: {binary_representation}")

    elif choice == "2":
        word = input("Ingrese una palabra: ")
        byte_representation = " ".join([ascii_to_binary(char_to_ascii(char)) for char in word])
        print(f"La representación en byte de '{word}' es: {byte_representation}")

    elif choice == "0":
        print("Saliendo del programa.")
        exit()

    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 0.")

# Loop del programa
while True:
    generate_byte_representation()
