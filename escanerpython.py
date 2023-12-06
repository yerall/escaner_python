#! /usr/bin/python3

import sys
import socket
from datetime import datetime

def escanear_puertos(objetivo, rango_puertos):
    # Añadir un banner
    print("-" * 50)
    print(f"Escaneando el objetivo {objetivo}")
    print(f"Hora de escaneo {datetime.now()}")
    print("-" * 50)

    # Escaneo de puertos
    for puerto in rango_puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} está abierto")
        s.close()

    print("-" * 50)

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <objetivo>")
        sys.exit(1)

    objetivo = sys.argv[1]
    rango_puertos = range(1, 500)

    escanear_puertos(objetivo, rango_puertos)

if __name__ == "__main__":
    main()
