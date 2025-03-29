def hacer_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar Nuevo Cliente.")
    print("2. Eliminar Cliente.")
    print("3. Mostrar Clientes.")
    print("0. Salir del sistema.")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def tomar_cliente():
    nombre_cliente = input("Digite el nombre: ")
    apellido_cliente = input("Digite el apellido: ")
    cedula_cliente = input("Digite la cédula: ")
    return [nombre_cliente, apellido_cliente, cedula_cliente]

def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad de nuevos clientes: "))
    for _ in range(cantidad_nuevas):
        aux_lista.append(tomar_cliente())
    return aux_lista

def mostrar_clientes(bd_clientes):
    if not bd_clientes:
        print("\nNo hay clientes registrados.")
    else:
        print("\n--- Lista de Clientes ---")
        for i, cliente in enumerate(bd_clientes, start=1):
            print(f"{i}. {cliente[0]} {cliente[1]} - Cédula: {cliente[2]}")

def eliminar_cliente(bd_clientes):
    mostrar_clientes(bd_clientes)
    if bd_clientes:
        try:
            indice = int(input("\nDigite el número del cliente a eliminar: ")) - 1
            if 0 <= indice < len(bd_clientes):
                eliminado = bd_clientes.pop(indice)
                print(f"Cliente {eliminado[0]} {eliminado[1]} eliminado con éxito.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada no válida.")

# **** Zona de Código Principal ****
base_datos_clientes = []

while True:
    opcion = hacer_menu()
    
    if opcion == 1:
        nuevo_cliente = tomar_cliente()
        base_datos_clientes.append(nuevo_cliente)
        print("Cliente registrado con éxito.")
    
    elif opcion == 2:
        eliminar_cliente(base_datos_clientes)
    
    elif opcion == 3:
        mostrar_clientes(base_datos_clientes)
    
    elif opcion == 0:
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente nuevamente.")
