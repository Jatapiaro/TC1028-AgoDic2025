"""
Crea un programa que pida al usuario dos números enteros y que diga si:
- Son iguales
- Cual es mayor y cual es menor

Ejemplo de ejecución:
>>> 99
>>> 20

90 es mayor que 20

- - - -
>>> 99
>>> 99

Ambos números son iguales
"""
def main():
    first_num = int(input("Ingresa el primer número entero: "))
    second_num = int(input("Ingresa el segundo número entero: "))
    
    if first_num == second_num:
        print("Ambos son iguales")
    elif first_num > second_num:
        print(f"{first_num} es mayor que {second_num}")
    else:
        print(f"{second_num} es mayor que {first_num}")
        
if __name__ == "__main__":
    main()