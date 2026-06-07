# Diccionario de empleados
empleados = {
    1111: {"nombre": "Daniel González", "dias": 12},
    2222: {"nombre": "Manuel Rodríguez", "dias": 18},
    3333: {"nombre": "Sergio Gómez", "dias": 22},
    4444: {"nombre": "Pedro Fernández", "dias": 15},
    5555: {"nombre": "Lucas Pérez", "dias": 6},
    6666: {"nombre": "Pablo López", "dias": 8}
}

print("=== Sistema de Gestión de Vacaciones ===")

# Solicita DNI
while True:

    try:
        dni = int(input("Ingrese su DNI: "))
        break

    except ValueError:
        print("Error: debe ingresar un DNI numérico.")

# Verifica si el DNI coincide en la base de datos (GATEWAY 1)
if dni not in empleados:

    print("Error: el DNI no se encuentra en la base de datos.")

#Si coincide:
else:

    # Solicita cantidad de días
    while True:

        try:
            dias = int(input("Ingrese la cantidad de días solicitados: "))

            if dias > 0:
                break

            print("Error: debe ingresar un número válido mayor a cero.")

        except ValueError:
            print("Error: debe ingresar una cantidad válida.")

    saldo = empleados[dni]["dias"]

    # Verifica el saldo disponible y acepta la solicitud si tiene saldo suficiente (GATEWAY 2)
    if dias <= saldo:
        # Actualiza el saldo
        empleados[dni]["dias"] -= dias

        print("Solicitud aprobada.")
        print(f"Saldo actualizado: {empleados[dni]['dias']} días.")
    # Si no tiene saldo suficiente , rechaza la solicitud
    else:

        print("Solicitud rechazada.")
        print(f"Saldo disponible: {saldo} días.")