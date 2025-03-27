def hacer_menu():
    print("1. Registrar Nuevo Cliente.")
    print("2. Eliminar Cliente.")
    print("0. Salir del sistema.")
    print("...seleccione una opción...")
    opcion = int(input())
    return  opcion

def tomar_cliente():
    nombre_cliente = input("Digite el nombre: ")
    apellido_cliente = input("Digite el apellido: ")
    cedula_cliente = input("Digite la cedula: ")
    info_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return info_cliente

def guardar_cliente(info_cliente, bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente

def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad nueva de clientes: "))
    for i in range(cantidad_nuevas):
        aux = tomar_cliente()
        aux_lista.append(aux)
    print(aux_lista)

# ****Zona de Código Principal ****
incluir_nueva_lista()
base_datos_clientes = []

while True:
    aux_opcion = hacer_menu()
    match aux_opcion:
        case 1:
            aux_info_cliente = tomar_cliente()
            base_datos_clientes = aux_basedatos
        case 2:
            aux_lista = incluir_nueva_lista()
            base_datos_clientes.extend(aux_lista)



base_datos_clientes = []
aux_opcion = hacer_menu()
aux_info_cliente = tomar_cliente()

aux_basedatos = guardar_cliente(aux_info_cliente, base_datos_clientes)
base_datos_clientes = aux_basedatos
print(base_datos_clientes)