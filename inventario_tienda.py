inventario = {"Leche": 10, "Pan": 20, "Queso": 5}
agotados = set()

def vender_producto(producto, cantidad):
    if producto in inventario:
        inventario[producto] -= cantidad
        if inventario[producto] <= 0:
            inventario[producto] = 0
            agotados.add(producto)
            print(f"Producto agotado: {producto}")
        else:
            print(f"Stock actualizado: {inventario[producto]}")
    else:
        print("Producto no existe.")

def mostrar_inventario():
    print("\nInventario:")
    for p, c in inventario.items():
        print(f"{p}: {c}")
    print(f"Agotados: {agotados}")

while True:
    print("\n--- INVENTARIO ---")
    print("1. Vender producto")
    print("2. Mostrar inventario")
    print("3. Salir")

    op = input("Opción: ")

    if op == "1":
        p = input("Producto: ")
        c = int(input("Cantidad: "))
        vender_producto(p, c)
    elif op == "2":
        mostrar_inventario()
    elif op == "3":
        break
    else:
        print("Opción inválida.")
