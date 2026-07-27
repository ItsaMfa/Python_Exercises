import random

#lista_empleados = {id_empleado: [bono recibido]}
lista_empleados = {}

bono_max = 0
empleados = 0
Presupuesto_inicial = 0
presupuesto_restante = 0


            
def ingreso_presupuesto():
    while True:
        try:
            presupuesto = int(input("Ingrese el presupuesto disponible: $"))
            Presupuesto_inicial = presupuesto
            if presupuesto < 0:
                print("El presupuesto no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico válido")
    return Presupuesto_inicial, presupuesto



def ingreso_bono(opcion, presupuesto):
    global bono_max
    while True:
        try:
            if opcion == 1:
                bono = int(input("Ingrese el bono a repartir: $"))

            elif opcion == 4:
                 bono = int(input("Ingrese el bono minimo a repartir: $"))
                 bono_max = int(input("Ingrese el bono maximo a repartir por persona: $"))
                 
            else:
                bono = int(input("Ingrese el bono minimo repartir: $"))

            
            if bono < 0:
                print("El bono mínimo no puede ser negativo. Intente nuevamente.")
                
                continue

            if bono > presupuesto:
                print("El bono mínimo no puede ser mayor al presupuesto disponible.")
                continue
            break
        except ValueError:
                    print("Ingrese un valor numérico válido")
    return bono, bono_max

def ingreso_empleados():

    while True:
        try:
            empleados = int(input("Ingrese la cantidad de empleados: "))
            if empleados < 0:
                print("La cantidad de empleados no puede ser negativa. Intente nuevamente.")
                continue
            for i in range(empleados):
                lista_empleados[i + 1] = [0]

            break
        except ValueError:
            print("Ingrese un valor numérico válido")

    return empleados

def ver_empleados():
    print("---- Empleados existentes ----\n")

    if not lista_empleados:
        print("No hay empleados ingresados.")
        return
    
    for key, value in lista_empleados.items():
        bono_formateado = f"${value[0]:,}".replace(",", ".")
        print(f"ID: {key}| Bono asignado: {bono_formateado}")


def asignar_bono_equitativo(presupuesto, lista_empleados, bono):
    global empleadosatendidos, bono_asignado

    total_empleados = len(lista_empleados)
    print("\n================ Asignación de bonos equitativo ================")

    if total_empleados == 0:
        print("No hay empleados registrados en el sistema.")
        return bono_asignado, empleadosatendidos, presupuesto

    bono_equitativo = presupuesto // total_empleados 
    aux = True
    if bono_equitativo < bono:
                    print("El bono equitativo no cubrirá a todas las personas") 
                    aux = False

    match aux:
        case False:
            for key, value in lista_empleados.items():


                if bono_equitativo < bono:
                        if presupuesto >= bono:
                            lista_empleados[key][0] = bono
                            presupuesto -= bono
                            bono_asignado += bono
                            empleadosatendidos += 1       
                            bono_formateado = f"${value[0]:,}".replace(",", ".")
                            presupuesto_formateado = f"${presupuesto:,}".replace(",", ".")
                            print(f"Empleado: {key}| Bono asignado: {bono_formateado} | Presupuesto restante: {presupuesto_formateado} ")

            if empleadosatendidos == total_empleados:
                                print("Todos los empleados han sido atendidos.")
                                
            else:
                                print("No se pudo atender a todos los empleados por falta de presupuesto.")
                                
        case True:
        
            for key, value in lista_empleados.items():
          

                if presupuesto >= bono_equitativo:
                            lista_empleados[key][0] = bono_equitativo
                            presupuesto -= bono_equitativo
                            bono_asignado += bono_equitativo
                            empleadosatendidos += 1
            
                
                bono_formateado = f"${value[0]:,}".replace(",", ".")
                presupuesto_formateado = f"${presupuesto:,}".replace(",", ".")
                print(f"Empleado: {key}| Bono asignado: {bono_formateado} | Presupuesto restante: {presupuesto_formateado} ")

            if empleadosatendidos == total_empleados:
                        print("Todos los empleados han sido atendidos.")
            else:
                        print("No se pudo atender a todos los empleados por falta de presupuesto.")

            
                

   
    return bono_asignado, empleadosatendidos, presupuesto


def asignar_bonos_estandar(presupuesto, lista_empleados, bono):
    global empleadosatendidos, bono_asignado
        
    print("\n================ Asignación de bonos estandar ================")
    
    total_empleados = len(lista_empleados)
    if total_empleados == 0:
        print("No hay empleados registrados en el sistema.")
        return bono_asignado, empleadosatendidos, presupuesto

    for key, value in lista_empleados.items():
        if presupuesto >= bono:
            lista_empleados[key][0] = bono
            presupuesto -= bono
            bono_asignado += bono
            empleadosatendidos += 1
            faltante = (total_empleados- empleadosatendidos) * bono
            bono_formateado = f"${value[0]:,}".replace(",", ".")
            presupuesto_formateado = f"${presupuesto:,}".replace(",", ".")
            print(f"Empleado: {key}| Bono asignado: {bono_formateado} | Presupuesto restante: {presupuesto_formateado}")
           
        else:
            print(f"Presupuesto insuficiente para el empleado {key} (Se requiere: ${faltante:,})".replace(",", "."))
            break

    if empleadosatendidos == total_empleados:
        print("Todos los empleados han sido atendidos.")
    else:
        print("No se pudo atender a todos los empleados por falta de presupuesto.")


    return bono_asignado, empleadosatendidos, presupuesto
    
    
    

def asignar_bonos_random(presupuesto,empleados, bono_minimo):
    global empleadosatendidos, bono_asignado

    print("\n================ Asignación de bonos Random ================")
    
            
    for key, value in lista_empleados.items():
        if presupuesto < bono_minimo:
            print(f"Presupuesto ya alcanzado.")
            break
    

        bono = random.randint(bono_minimo, presupuesto)
        lista_empleados[key][0] = bono
        if presupuesto >= bono:
            presupuesto -= bono
            bono_asignado += bono
            empleadosatendidos += 1
            bono_formateado = f"${value[0]:,}".replace(",", ".")
            presupuesto_formateado = f"${presupuesto:,}".replace(",", ".")
            print(f"Empleado: {key}| Bono asignado: {bono_formateado} | Presupuesto restante: {presupuesto_formateado} ")
        else:
            break
    if empleadosatendidos == len(empleados):
        print("Todos los empleados han sido atendidos.")
    else:
        print(f"No se pudo atender a todos los empleados por falta de presupuesto.")

    return bono_asignado, empleadosatendidos, presupuesto



def asignar_bonos_random_limitado(presupuesto,empleados, bono_minimo, bono_maximo):
    global empleadosatendidos, bono_asignado

    print("\n================ Asignación de bonos Random ================")
    
            
    for key, value in lista_empleados.items():
        if presupuesto < bono_minimo:
            print(f"Presupuesto ya alcanzado.")
            break

    

        bono = random.randint(bono_minimo, bono_maximo)
        lista_empleados[key][0] = bono
        if presupuesto >= bono:
            presupuesto -= bono
            bono_asignado += bono
            empleadosatendidos += 1

            bono_formateado = f"${value[0]:,}".replace(",", ".")
            presupuesto_formateado = f"${presupuesto:,}".replace(",", ".")
            print(f"Empleado: {key}| Bono asignado: {bono_formateado} | Presupuesto restante: {presupuesto_formateado} ")
        else:
            break
    if empleadosatendidos == len(empleados):
        print("Todos los empleados han sido atendidos.")
    else:
        print(f"No se pudo atender a todos los empleados por falta de presupuesto.")

    return bono_asignado, empleadosatendidos, presupuesto


#==================== main menu ====================




while True:
            print("\n [-----| MENÚ |-----]")
            print("1.- Asignar bono estandar.")
            print("2.- Repartir bonos de manera equitativa.")
            print("3.- Asignar presupuesto de manera aleatoria.")
            print("4.- Asignar presupuesto de manera aleatoria limitado.")
            print("5.- Ver empleados.")
            print("6.- Salir.")
    
            try:
                opcion = int(input("Ingrese la opción que desea: "))
            except ValueError:
                print("Opción no válida. Por favor, ingrese un número.")
                continue

            if opcion in [1, 2, 3, 4]:
                bono_asignado = 0
                empleadosatendidos =0
                lista_empleados.clear()
                empleados= ingreso_empleados()
                Presupuesto_inicial, presupuesto = ingreso_presupuesto()
            match opcion:
                case 1:
                    
                    bono, bono_max= ingreso_bono(opcion,presupuesto )
                    bono_asignado, empleadosatendidos, presupuesto_restante= asignar_bonos_estandar(presupuesto, lista_empleados, bono)

                case 2:
                    bono, bono_max=ingreso_bono(opcion, presupuesto)
                    bono_asignado, empleadosatendidos, presupuesto_restante = asignar_bono_equitativo(presupuesto, lista_empleados, bono)
                case 3:
                    bono, bono_max=ingreso_bono(opcion, presupuesto)
                    bono_asignado, empleadosatendidos, presupuesto_restante = asignar_bonos_random(presupuesto,lista_empleados, bono)
                case 4: 
                    bono, bono_max=ingreso_bono(opcion, presupuesto)
                    bono_asignado, empleadosatendidos, presupuesto_restante = asignar_bonos_random_limitado(presupuesto,lista_empleados, bono, bono_max)
                case 5:
                    ver_empleados()
                case 6:
                    print("Adios...Cerrando sistema")
                    break
                    
                case _:
                    print("Por favor ingrese una opcion disponible")

            print("\n================ Resumen de la asignación de bonos ================")
            print(f"Total de empleados: {empleados}")
            print(f"Presupuesto inicial: ${Presupuesto_inicial:,}".replace(",", "."))
            print(f"Empleados atendidos: {empleadosatendidos}")
            print(f"Bono total asignado: ${bono_asignado:,}".replace(",", ".")) 
            print(f"Presupuesto restante: ${presupuesto_restante:,}".replace(",", "."))

