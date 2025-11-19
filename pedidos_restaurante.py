pedidos = []

def agregar_pedido(mesa, platos, total):
    pedido = {"mesa": mesa, "platos": platos, "total": total}
    pedidos.append(pedido)
    print(f"Pedido agregado: {pedido}")

def entregar_pedido(mesa):
    for ped in pedidos:
        if ped["mesa"] == mesa:
            pedidos.remove(ped)
            print(f"Pedido entregado: {mesa}")
            return
    print("Mesa no encontrada.")

def mostrar_pedidos():
    print("Pedidos pendientes:")
    if pedidos:
        for p in pedidos:
            print(p)
    else:
        print("Sin pedidos.")

while True:
    print("\n--- CONTROL DE PEDIDOS ---")
    print("1. Agregar pedido")
    print("2. Entregar pedido")
    print("3. Mostrar pedidos")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        mesa = input("Mesa: ")
        platos = input("Platos (separados por comas): ").split(",")
        total = float(input("Total: "))
        agregar_pedido(mesa, platos, total)
    elif op == "2":
        mesa = input("Mesa: ")
        entregar_pedido(mesa)
    elif op == "3":
        mostrar_pedidos()
    elif op == "4":
        break
    else:
        print("Opción inválida.")
