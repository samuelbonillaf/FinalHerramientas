# FINAL HERRAMIENTAS COMPUTACIONALES
### Componenete practico
![Icono](https://images.crunchbase.com/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1483776490/fj7db3i1wfe3uvttpjpw.png)
### Integrantes:
- Kevin Cifuentes Quintero (Cl4ud123)
- Samuel Alberto Mateo Bonilla Franco (Samuelbonillaf)
- Shi Jian Alejandro Yu Che (Shorask)

## Python
### Menu
#### Codigo
>def generate_byte_representation():
    print("\nMenú:")
    print("1. Generar la representación en byte de un carácter")
    print("2. Generar la representación en byte de una palabra")
    print("0. Salir")
    choice = input("Ingrese su opción: ")
    if choice == "1":
        char = input("Ingrese un carácter: ")
    elif choice == "2":
        word = input("Ingrese una palabra: ")
    elif choice == "0":
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 0.")
#### Explicacion 
Se le asignan valores a cada una de las opciones que puede elegir el usuario (0, 1 y 2) y se le pide al usuario que elija una de estas, luego el programa comprueba cada una de las opciones y ejecuta las instrucciones correspondientes a la selecion del usuario, de ser invalida la seleccion, el programa se lo hace saber al usuario y le pide que ingrese otra cosa.

### Caracter a ASCII
#### Codigo
>def char_to_ascii(character):
    return ord(character)
#### Explicacion
La funcion char_to_ascii() toma un unico caracter y usando la funcion de python ord() devuelve la representacion numerica del caracter.

### ASCII a Binario
#### Codigo
>def ascii_to_binary(ascii_value):
    return bin(ascii_value)[2:].zfill(8)
#### Explicacion
La funcion ascii_to_binary() toma un valor numerico (que debe corresponder a un caracter ASCII) y lo transforma en binario, ademas rellena con 0s los bits faltantes para completar el byte.

## GitHub
### Comandos
- git clone https://github.com/samuelbonillaf/FinalHerramientas.git
- git checkiut -b Rama
- git status
- git add .
- git commit -m Readme
- git push

### Proceso
Creamos el repositorio desde la pagina de GitHub, luego cada uno la clono con git clone, creamos las ramas y las abrimos con el comando git checkiut -b Samuel, luego subimos los archivos a la rama con los comandos git status/add/commit/push, por ultimo para facilitarnos la vida y por cuestiones de tiempo hicimos el merge desde la pagina.

 
