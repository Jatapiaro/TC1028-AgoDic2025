"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
def main():
    num = int(input("Introduce un número: "))
    
    if num < 0: 
        print("negativo")
    elif num == 0: 
        print("cero")
    elif num > 0: 
        print("positivo")
    else:
        print("entrada inválida")

if __name__ == "__main__":
    main()