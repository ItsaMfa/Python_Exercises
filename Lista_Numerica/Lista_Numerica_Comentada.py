#======================================================
# PROGRAMA: REGISTRO DE NÚMEROS Y ESTADÍSTICAS BÁSICAS
#======================================================


numeros=[] # Lista que almacena los números ingresados

""" Bucle principal del programa 
Genera un menú de opciones y ejecuta la opción seleccionada por el usuario
hasta seleccionar la opción de salir (6) """


#======================================================
# ---------------------- MENU -------------------------
#======================================================

while True: # 'while True' crea un ciclo infinito para que el menú se muestre repetidamente

# Mostramos las opciones del menú en la consola
    print('\n * ** * ** M e n ú ** * ** *')
    print('1.- Ingresar números')
    print('2.- Mostrar mayor')
    print('3.- Mostrar menor')
    print('4.- Mostrar promedio')
    print('5.- Mostrar todos los números ingresados')
    print('6.- Salir \n')

#Try except para capturar errores de tipo ValueError al ingresar la opción del menú 
#Para evitar que el programa se cierre inesperadamente si el usuario ingresa un valor no numérico
    try:
        opcion=int(input('Ingresa la opción que deseas: '))

# Si el usuario ingresa un valor no numérico
#  se captura la excepción ValueError y se muestra un mensaje de error
    except ValueError:
        print('¡Debes ingresar un número entero!')
        continue


# El match case funcina como un if especializado para comparar
#  el valor de la variable 'opcion' con los casos definidos 

    match opcion:


#======================================================
# --------------- Ingresar Numeros --------------------
#======================================================
        case 1:
            while True:
                # Este try valida que el numero ingresado sea un entero y que esté entre 1 y 100
                try:
                    numero=int(input('Ingresa un numero (entre el 1-100): '))
                    if 1 <= numero <=100:
                        numeros.append(numero) 
                        print('Ingreso Exitoso')
                        # 'break' rompe este bucle interno y nos regresa al menú principal
                        break 
                    else:

                        print('¡Debes ingresar un número entre el 1 y el 100!')
                #Except es quien captura la excepción ValueError y muestra un mensaje
                #de error si el usuario ingresa un valor no numérico
                except ValueError as error:
                    print('¡Debes ingresar un número entero!')

#=======================================================
# -------------- Mostrar el número mayor ---------------
#=======================================================
       
        case 2:
            if len(numeros) > 0:
                # max devuelve el valor máximo de la lista "numeros"
                num_mayor= max(numeros) 
                print('El número mayor ingresado es: ', num_mayor)
            else:
                print('No se han ingresado numeros :(')

#=======================================================
# -------------- Mostrar el número menor ---------------
#=======================================================

        case 3:
            if len(numeros)> 0:
                # min devuelve el valor mínimo de la lista "numeros"
                num_menor= min(numeros) 
                print('El número menor ingresado es: ', num_menor)
            else:
                print('No se han ingresado numeros :(')

#=======================================================
# -------------- Mostrar el promedio -------------------
#=======================================================    
#            
        case 4:
            try:
                # sum suma todos los elementos de la lista "numeros"
                # len devuelve la cantidad total de elementos de la lista "numeros"
                promedio=sum(numeros) / len(numeros)  

                # end="" evita que el print agregue un salto de línea al final del mensaje
                print('El promedio de los numero ingresados es: ', end="")

                # is_integer() verifica si el promedio es un número entero (True/False)
                if promedio.is_integer():
                    print(int(promedio))  #este es el caso de que sea un numero entero (True)

                else:
                    #Round redondea el promedio a 2 decimales
                    print(round(promedio, 2))
            except ZeroDivisionError:
                #Se activa cuando la lista está vacia y se intenta dividir entre cero
                print('No se puede calcular el promedio :(')

#=======================================================
# ----- Mostrar un historial de números ingresados -----
#=======================================================
        case 5:
            #Si la lista contiene numeros muestra los numeros
            #  ingresados separados por un guion
            if len(numeros) > 0:

                # "join" une los elementos de la lista "numeros" en una cadena de texto (str)
                #  separados por un guion " - "
                #for i in numeros: recorre los elementos de la lista "Numeros"
                lista= ' - '.join(str(i) for i in numeros)
                print('Los números ingresados son:', lista)
            else:
                print('No se han ingresado números :(')

#=======================================================
# ------------------ Cerrar programa -------------------
#=======================================================

        case 6:
            #Rompe el bucle principal y termina el programa
            print('Fin del programa. ByeBye.')
            break

#=======================================================
# ------------------- Caso Defecto --------------------
#======================================================= 

# Se ejecuta si la opción introducida
#  no es ninguno de los números que aparecen en el menú (1-6)
        case _:
            print('Por favor ingresa una opción valida')
