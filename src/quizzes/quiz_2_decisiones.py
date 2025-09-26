"""
Escribe un programa para calcular el precio final de un artículo en una tienda, considerando un descuento basado en el tipo de cliente.

El usuario ingresará dos valores:
- el precio original del artículo.
- un número entero que representa el tipo de cliente. Puede ser:
    0 para clientes nuevos ( no tiene descuento)
    1 para clientes regulares (descuento del 10%).
    2 para clientes VIP (descuento del 20%).

El programa debe calcular el precio final del artículo aplicando el descuento
correspondiente según el tipo de cliente.

El programa debe mostrar el precio original, el monto del descuento y el precio final.

Ejemplo de ejecución:
Ingrese el precio original del artículo: 150.0
Ingrese el tipo de cliente (0 si no es cliente, 1 para regular, 2 para VIP): 1

Output:
El precio original del artículo es: 150
El monto del descuento es: 15
El precio final del artículo con descuento es: 135.0
"""

precio_original: float = float(input("Ingrese el precio original del artículo: "))
tipo_de_cliente: float = float(
    input(
        "Ingrese el tipo de cliente (0 si no es cliente, 1 para regular, 2 para VIP): "
    )
)

monto_de_descuento = 0
if tipo_de_cliente == 1:
    monto_de_descuento = precio_original * 0.10
elif tipo_de_cliente == 2:
    monto_de_descuento = precio_original * 0.20

# No usamos else, asumimos que si es 0 o cualquier otro número
# no se aplica descuento.

print(f"El precio original del artículo es: {precio_original}")
print(f"El monto del descuento es: {monto_de_descuento}")
print(
    f"El precio final del artículo con descuento es: {precio_original - monto_de_descuento}"
)
