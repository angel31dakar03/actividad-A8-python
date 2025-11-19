encuestas = []

def agregar_respuesta(cliente, puntuacion, comentario):
    encuestas.append((cliente, puntuacion, comentario))
    print("Respuesta guardada.")

def promedio_satisfaccion():
    if encuestas:
        prom = sum(r[1] for r in encuestas) / len(encuestas)
        print(f"Promedio: {prom:.2f}")
    else:
        print("Sin datos.")

def comentarios_negativos():
    print("Comentarios negativos:")
    for c, p, co in encuestas:
        if p < 5:
            print(f"{c}: {co}")

while True:
    print("\n--- ENCUESTA ---")
    print("1. Agregar respuesta")
    print("2. Promedio de satisfacción")
    print("3. Comentarios negativos")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        cliente = input("Cliente: ")
        puntuacion = int(input("Puntuación (1-10): "))
        comentario = input("Comentario: ")
        agregar_respuesta(cliente, puntuacion, comentario)
    elif op == "2":
        promedio_satisfaccion()
    elif op == "3":
        comentarios_negativos()
    elif op == "4":
        break
    else:
        print("Opción inválida.")
