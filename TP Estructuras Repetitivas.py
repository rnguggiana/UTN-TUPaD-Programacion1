# Ejercicio 1 — “Caja del Kiosco”

nombre_cliente = input("Ingrese su nombre: ")

while nombre_cliente == "" or nombre_cliente.isalpha() == False:
    print("El nombre ingresado no es correcto, intente nuevamente.")
    nombre_cliente = input("Ingrese su nombre: ")

cantidad_producto = input("Ingrese la cantidad de productos: ")

while cantidad_producto.isdigit() == False or int(cantidad_producto) <=0:
    print("La cantidad ingresada no es correcta, intente nuevamente.")
    cantidad_producto = input("Ingrese la cantidad de productos: ")

cantidad_producto = int(cantidad_producto)

total_sdescuento = 0
total_cdescuento = 0

detalle_productos = ""

for i in range(cantidad_producto):
    print(f"Producto {i + 1}")

    precio_producto = input("Ingrese el precio del producto: ")

    while precio_producto.isdigit() == False:
        print("El precio ingresado no es correcto, intente nuevamente.")
        precio_producto = input("Ingrese el precio del producto: ")

    precio_producto = int(precio_producto)

    descuento = input("El producto tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error, ingrese S o N")
        descuento = input("El producto tiene descuento? (S/N): ").lower()

    detalle_productos += f"Producto {i + 1} - Precio: {precio_producto} Descuento (S/N): {descuento}\n"

    total_sdescuento += precio_producto

    if descuento == "s":
        precio_final_producto = precio_producto * 0.9
    else:
        precio_final_producto = precio_producto
    
    total_cdescuento += precio_final_producto

ahorro = total_sdescuento - total_cdescuento
promedio = total_cdescuento / cantidad_producto


print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_producto}")
print(detalle_productos)
print(f"El total sin descuentos es de: ${total_sdescuento}")
print(f"El total con descuentos es de: ${total_cdescuento}")
print(f"El ahorro es de: ${ahorro:.2f}")
print(f"El promedio por producto es de: ${promedio:.2f}")


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = 'alumno'
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and acceso == False:
    print(f"Intento {intentos + 1}/3 - Usuario: ", end="")
    usuario = input()

    print("Clave: ", end="")
    clave = input()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")
        acceso = True
    else:
        print("Credenciales invalidas, vuelva a intentar")
        print()
    
if acceso == False:
    print("Cuenta bloqueda, contacte al administrador")

else:
    opcion = ""

    while opcion != "4":
        print()
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        while opcion.isdigit() == False:
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        while int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while opcion.isdigit() == False:
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

        if opcion == "1":
            print("Inscripto")

        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: La clave nueva debe tener minimo 6 caracteres, intente nuevamente.")
                nueva_clave = input("Nueva clave: ")
    
            confirmar_clave = input("Confirmar clave: ")

            if nueva_clave == confirmar_clave:
                clave_correcta = nueva_clave
                print("La clave se ha modificado con exito.")
            else:
                print("Error: Las claves no coinciden.")

        elif opcion == "3":
            print("La practica hace al Maestro")

        elif opcion == "4":
            print("Saliendo del sistema, vuelva pronto.")


# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")

while operador == "" or operador.isalpha() == False:
    print("Error, solo letras.")
    operador = input("Ingrese nuevamente el nombre del operador: ")

opcion = "" 

while opcion != "5":
    print()
    print("1) Reservar Turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    print()

    opcion = input("Seleccione una Opcion: ")

    while opcion.isdigit() == False:
        print("Error: Opcion Invalida")
        opcion = input("Seleccione una Opcion nuevamente: ")
    
    while int(opcion) < 1 or int(opcion) > 5:
        print("Error: Fuera de rango")
        opcion = input("Seleccione una Opcion nuevamente: ")

        while opcion.isdigit() == False:
            print("Error: Opcion Invalida")
            opcion = input("Seleccione una Opcion nuevamente: ")

    if opcion == "1":
        dia = input("Ingrese el dia a seleccionar (1= Lunes, 2= Martes): ")

        while dia != "1" and dia != "2":
            print("Error, elija un dia disponible")
            dia = input("Ingrese nuevamente el dia a seleccionar (1= Lunes, 2= Martes): ")

        paciente = input("Ingrese el nombre del paciente a reservar: ")
    
        while paciente == "" or paciente.isalpha() == False:
            print("Error: Solo letras")
            paciente = input("Ingrese nuevamente el nombre del paciente a reservar: ")

        if dia == "1":

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Paciente ya registrado!.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Truno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Truno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Truno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Truno reservado correctamente.")

            else:
                print("No hay turnos disponibles.")

        elif dia == "2":

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Paciente ya registrado!.")

            elif martes1 == "":
                martes1 = paciente
                print("Truno reservado correctamente.")

            elif martes2 == "":
                martes2 = paciente
                print("Truno reservado correctamente.")

            elif martes3 == "":
                martes3 = paciente
                print("Truno reservado correctamente.")

            else:
                print("No hay turnos disponibles.")

    elif opcion == "2":
        dia = input("Ingrese el dia a seleccionar (1= Lunes, 2= Martes): ")

        while dia != "1" and dia != "2":
            print("Error, elija un dia disponible")
            dia = input("Ingrese nuevamente el dia a seleccionar (1= Lunes, 2= Martes): ")

        paciente = input("Ingrese el nombre del paciente a cancelar: ")

        while paciente == "" or paciente.isalpha() == False:
            print("Error: Solo letras.")
            paciente = input("Ingrese nuevamente el nombre del paciente a cancelar: ")

        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("Paciente no encontrado.")

        elif dia == "2":
            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("Paciente no encontrado.")

    elif opcion == "3":
        dia = input("Ingrese el dia a consultar (1= Lunes, 2= Martes): ")

        while dia != "1" and dia != "2":
            print("Error, elija un dia disponible")
            dia = input("Ingrese nuevamente el dia a consultar (1= Lunes, 2= Martes): ")

        if dia == "1":
            print("Agenda del Lunes: ")

            if lunes1 == "":
                print("Turno 1: (LIBRE)")
            else:
                print(f"Turno 1: (OCUPADO) - PACIENTE: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (LIBRE)")
            else:
                print(f"Turno 2: (OCUPADO) - PACIENTE: {lunes2}")
            
            if lunes3 == "":
                print("Turno 3: (LIBRE)")
            else:
                print(f"Turno 3: (OCUPADO) - PACIENTE: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (LIBRE)")
            else:
                print(f"Turno 4: (OCUPADO) - PACIENTE: {lunes4}")
        
        elif dia == "2":
            print("Agenda del Martes: ")

            if martes1 == "":
                print("Turno 1: (LIBRE)")
            else:
                print(f"Turno 1: (OCUPADO) - PACIENTE: {martes1}")

            if martes2 == "":
                print("Turno 2: (LIBRE)")
            else:
                print(f"Turno 2: (OCUPADO) - PACIENTE: {martes2}")
            
            if martes3 == "":
                print("Turno 3: (LIBRE)")
            else:
                print(f"Turno 3: (OCUPADO) - PACIENTE: {martes3}")

    elif opcion == "4":
        lunes_ocupados = 0
        martes_ocupados = 0
        
        if lunes1 != "":
            lunes_ocupados += 1
        if lunes2 != "":
            lunes_ocupados += 1
        if lunes3 != "":
            lunes_ocupados += 1
        if lunes4 != "":
            lunes_ocupados += 1

        if martes1 != "":
            martes_ocupados += 1
        if martes2 != "":
            martes_ocupados += 1
        if martes3 != "":
            martes_ocupados += 1

        lunes_disponibles = 4 - lunes_ocupados
        martes_disponibles = 3 - martes_ocupados 

        print("Resumen general: ")
        print(f"Lunes -> Ocupados: {lunes_ocupados} | Disponibles: {lunes_disponibles}")
        print(f"Martes -> Ocupados: {martes_ocupados} | Disponibles: {martes_disponibles}")

        if lunes_ocupados > martes_ocupados:
            print("El dia con mas turnos es el Lunes.")
        elif martes_ocupados > lunes_ocupados:
            print("El dia con mas turnos es el Martes.")
        else:
            print("Empate, los dias tienen la misma cantidad de turnos")

    elif opcion == "5":
        print("Sistema cerrado.")
        

# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False

nombre_agente = input("Por favor, ingrese el nombre del agente: ")

while nombre_agente == "" or nombre_agente.isalpha() == False:
    print("Error, solo letras")
    nombre_agente = input("Por favor, ingrese nuevamente el nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:
    print("ESTADO Y MENU:")
    print()
    print(f"Agente: {nombre_agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")
    print()
    print(f"Elija una opción agente {nombre_agente}")
    print()

    opcion = input("Ingrese su opción: ")

    while opcion.isdigit() == False:
        print("ERROR: Ingrese una opción válida")
        opcion = input("Ingrese nuevamente su opción: ")

    while int(opcion) < 1 or int(opcion) > 3:
        print("ERROR: Opción fuera de rango")
        opcion = input("Ingrese nuevamente su opción: ")

        while opcion.isdigit() == False:
            print("ERROR: Ingrese un número válido")
            opcion = input("Ingrese nuevamente su opción: ")

    if opcion == "1":
        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            alarma = True
            print("La cerradura se trabó. Se activó la alarma.")

        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")

                while riesgo.isdigit() == False:
                    print("ERROR: Ingrese un número válido.")
                    riesgo = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")

                while int(riesgo) < 1 or int(riesgo) > 3:
                    print("ERROR: Fuera de rango.")
                    riesgo = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")

                    while riesgo.isdigit() == False:
                        print("ERROR: Ingrese un número válido.")
                        riesgo = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")

                if riesgo == "3":
                    alarma = True
                    print("Se activó la alarma.")
                else:
                    cerraduras_abiertas += 1
                    print("Abriste una cerradura.")
            else:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

    elif opcion == "2":
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        for i in range(4):
            print(f"Paso {i + 1}/4 completado")
            codigo_parcial += "*"

        print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El hackeo abrió una cerradura automáticamente.")

    elif opcion == "3":
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10
            print("La alarma te cuesta 10 de energía")

        print(f"Descansaste agente {nombre_agente}")

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("El sistema se bloqueó por la alarma.")

if cerraduras_abiertas == 3:
    print("VICTORIA: Abriste la bóveda")
elif bloqueado == True:
    print("DERROTA: La bóveda quedó bloqueada")
else:
    print("DERROTA: Te quedaste sin energía o sin tiempo")


# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while nombre == "" or nombre.isalpha() == False:
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print()
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    while opcion.isdigit() == False:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    while int(opcion) < 1 or int(opcion) > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while opcion.isdigit() == False:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

    if opcion == "1":
        if vida_enemigo < 20:
            danio = danio_pesado * 1.5
        else:
            danio = danio_pesado

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("¡Te curaste 30 puntos de vida!")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
