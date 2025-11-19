asistentes = set()
registro_horas = {}

def registrar_asistencia(nombre, hora):
    if nombre in asistentes:
        print("Ya asistió.")
    else:
        asistentes.add(nombre)
        registro_horas[nombre] = hora
        print(f"Asistencia registrada para {nombre} a las {hora}")

def total_asistentes():
    print(f"Asistentes únicos: {len(asistentes)}")

while True:
    print("\n--- CONTROL DE ASISTENCIA ---")
    print("1. Registrar asistencia")
    print("2. Total asistentes")
    print("3. Salir")

    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ")
        h = input("Hora (HH:MM): ")
        registrar_asistencia(n, h)
    elif op == "2":
        total_asistentes()
    elif op == "3":
        break
    else:
        print("Opción inválida.")
