turnos = []

def agregar_paciente(nombre, edad, especialidad):
    paciente = (nombre, edad, especialidad)
    turnos.append(paciente)
    print(f"Paciente agregado: {paciente}")

def atender_paciente():
    if turnos:
        atendido = turnos.pop(0)
        print(f"Paciente atendido: {atendido}")
    else:
        print("No hay pacientes en espera.")

def mostrar_turnos():
    if turnos:
        print("Pacientes en espera:")
        for paciente in turnos:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

while True:
    print("\n--- SISTEMA DE TURNOS MÉDICOS ---")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. Mostrar turnos")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ")
        e = int(input("Edad: "))
        esp = input("Especialidad: ")
        agregar_paciente(n, e, esp)
    elif op == "2":
        atender_paciente()
    elif op == "3":
        mostrar_turnos()
    elif op == "4":
        break
    else:
        print("Opción inválida.")
