# Sistema de gestion de pedidos
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

def confirmar_pedido(total):
    # Validacion pendiente: verificar si el usuario esta logueado
    if total > 0:
        print("Pedido confirmado")
    else:
        print("Error en pedido")
      
