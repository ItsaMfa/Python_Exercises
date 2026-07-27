#Arriendo = {ID_Cliente: [nombre, transporte, dias_arriendo, total]}
arriendo = {}
#Transporte = {ID: [Tipo, disponibe, precio_arriendo_diario]}
transporte = {1: ["Bicicleta", True, 5000], 2: ["Moto", True, 10000], 3: ["Auto", True, 20000],        
             4: ["Camioneta", True, 30000], 5: ["Bus", True, 40000], 6: ["Camión", True, 50000], 
             7: ["Avión", True, 100000], 8: ["Barco", True, 200000], 9: ["Tren", True, 300000],
             10: ["Helicóptero", True, 400000], 11: ["Submarino", True, 500000], 12: ["Cohete", True, 1000000]}

contador_id = 1
#============================== Metodos ==============================

def ingresar_cliente():
    global contador_id  

    try:
        nombre = str(input("Ingrese el nombre del cliente: ").strip().title())
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.") 

        if any(caracter.isdigit() for caracter in nombre):
            raise ValueError("El nombre no puede contener dígitos o números.") 
    except ValueError as e:
        print(e)
        return

    arriendo[contador_id] = [nombre, None, 0, 0]
    print(f"El cliente {nombre} fue ingresado correctamente \n Su ID es: {contador_id}")
    contador_id += 1

def transportes_disponibles():
    print("---- Transportes Disponibles ----\n")
    for key, value in transporte.items():
        if value[1] == True:
            print(f"ID: {key}| Tipo: {value[0]} - Precio diario: ${value[2]}")
    print("----------------------------------------")

def solicitar_transporte():


    try:
           id_cliente = int(input("Ingrese el ID del cliente: "))
    except ValueError as e:
           print(e)
           return
   


    if id_cliente not in arriendo:
        print("Cliente no encontrado.")
        return

    if arriendo[id_cliente][1] is not None:
        print("Error: Este cliente ya tiene un transporte arrendado. Debe devolverlo primero.")
        return
    
    else:
        try:
            id_transporte = int(input("Ingrese el ID del transporte que desea solicitar: "))
        except ValueError as e:
            print(e)
            return

        if id_transporte not in transporte:
                    print("Transporte no encontrado.")
                    return
        if transporte[id_transporte][1] == False:
                    print("Transporte no disponible de momento.")
                    return
        else:

            try:
                dias_arriendo = int(input("Ingrese la cantidad de días que desea arrendar el transporte: "))
                if dias_arriendo <= 0:
                    print("Error: La cantidad de días debe ser mayor a 0.")
                    return
            except ValueError as e:
                print(e)
                return

            total = dias_arriendo * transporte[id_transporte][2]
            arriendo[id_cliente][1] = id_transporte
            arriendo[id_cliente][2] = dias_arriendo
            arriendo[id_cliente][3] = total
            
            transporte[id_transporte][1] = False
            print(f"Transporte {transporte[id_transporte][0]} arrendado correctamente por {dias_arriendo} días.")
            print(f"El total a pagar por el arriendo es: ${total}")

            


def ver_arriendos():
    hay_arriendos = False
    print("---- Arriendos ----")
    for key, value in arriendo.items():
        if value[1] is not None:
            id_transporte = value[1]
            nombre_transporte = transporte[id_transporte][0]
            print(f"ID Cliente: {key} | Nombre: {value[0]} - Transporte: {nombre_transporte} - ID Transporte: {id_transporte} - Días de arriendo: {value[2]} - Total a pagar: ${value[3]}")
            hay_arriendos = True
    if hay_arriendos == False:
            print("No hay arriendos registrados de momento :(.")
             


def ver_clientes():
    print("---- Clientes ----")
    if not arriendo:
        print("No hay clientes registrados en el sistema :(")
        return
    for key, value in arriendo.items():
        if value[1] is not None:
            id_transporte = value[1]
            nombre_transporte = transporte[id_transporte][0]
            print(f"ID Cliente: {key} | Nombre: {value[0]} - Transporte: {nombre_transporte} - ID Transporte: {id_transporte} - Días de arriendo: {value[2]} - Total a pagar: ${value[3]}")
        else:
            print(f"ID Cliente: {key} | Nombre: {value[0]} - No ha solicitado transporte.")
            

def devolver_transporte():

    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
    except ValueError as e:
        print(e)
        return
    if id_cliente not in arriendo:
        print("Cliente no encontrado.")
        return
    
    if arriendo[id_cliente][1] is None:
        print("El cliente no tiene transporte arrendado.")
        return
    
    else:
        id_transporte = arriendo[id_cliente][1]
        transporte_nombre = transporte[id_transporte][0]
        transporte[id_transporte][1] = True

        arriendo[id_cliente][1] = None
        arriendo[id_cliente][2] = 0
        arriendo[id_cliente][3] = 0
        print(f" {transporte_nombre.capitalize()} devuelto correctamente.")
#============================== Menu ==============================
while True:

    print("\n [-----| MENU |-----]")
    print("1.- Ingresar cliente.")
    print("2.- Ver transportes disponibles.")
    print("3.- Solicitar transporte.")
    print("4.- Ver transportes arrendados.")
    print("5.- Ver lista de clientes.")
    print("6.- Devolver transporte.")
    print("7.- Salir.")

    try:
        opcion = int(input("Ingrese la opción que desea: "))
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número.")
        continue

    match opcion:
            case 1:
                ingresar_cliente()
            case 2:
                transportes_disponibles()
            case 3:
                solicitar_transporte()
            case 4:
                ver_arriendos()
            case 5:
                ver_clientes()
            case 6:
                devolver_transporte()
            case 7:
                print("Saliendo del programa...ByeBye!")
                break
            case _:
                print("Opción no válida. Por favor, ingrese una opcion disponible.")
            

