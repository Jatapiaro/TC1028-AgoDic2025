"""
Imprime un cuadrado de 5x5 usando el carácter asterisco (*).
"""


def main():
    for _ in range(5):
        line = ""
        for _ in range(5):
            line += "*"
        print(line)


main()
