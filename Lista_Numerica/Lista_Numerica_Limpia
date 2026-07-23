numeros=[] 

while True:
    print('\n * ** * ** M e n ú ** * ** *')
    print('1.- Ingresar números')
    print('2.- Mostrar mayor')
    print('3.- Mostrar menor')
    print('4.- Mostrar promedio')
    print('5.- Mostrar todos los números ingresados')
    print('6.- Salir \n')

    try:
        opcion=int(input('Ingresa la opción que deseas: '))

    except ValueError:
        print('¡Debes ingresar un número entero!')
        continue

    match opcion:
        case 1:
            while True:
                try:
                    numero=int(input('Ingresa un numero (entre el 1-100): '))
                    if 1 <= numero <=100:
                        numeros.append(numero) 
                        print('Ingreso Exitoso')
                        break
                    else:
                        print('¡Debes ingresar un número entre el 1 y el 100!')
                except ValueError as error:
                    print('¡Debes ingresar un número entero!')
        
        case 2:
            if len(numeros) > 0:
                num_mayor= max(numeros) 
                print('El número mayor ingresado es: ', num_mayor)
            else:
                print('No se han ingresado numeros :(')
        case 3:
            if len(numeros)> 0:
                num_menor= min(numeros) 
                print('El número menor ingresado es: ', num_menor)
            else:
                print('No se han ingresado numeros :(')
        case 4:
            try:
                promedio=sum(numeros) / len(numeros) 
                print('El promedio de los numero ingresados es: ', end="")

                if promedio.is_integer():
                    print(int(promedio))
                else:
                    print(round(promedio, 2))
            except ZeroDivisionError:
                print('No se puede calcular el promedio :(')
        case 5:
            if len(numeros) > 0:
                lista= ' - '.join(str(i) for i in numeros)
                print('Los números ingresados son:', lista)
            else:
                print('No se han ingresado números :(')
        case 6:
            print('Fin del programa. ByeBye.')
            break
        case _:
            print('Por favor ingresa una opción valida')
