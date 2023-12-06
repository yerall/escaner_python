# Escáner de Puertos Simple en Python

Este script en Python realiza un escaneo de puertos en un objetivo dado. Proporciona información sobre los puertos abiertos en el objetivo especificado.

## Características

- Utiliza sockets para escanear puertos en el objetivo.
- Muestra la hora de escaneo y un banner informativo.

## Uso

Asegúrate de tener Python 3 instalado. Ejecuta el script desde la línea de comandos proporcionando el objetivo que deseas escanear:

```python
chmod +x escanerpython.py
python3 escanerpython.py <objetivo>

```

## Ejemplo de uso

```python
python3 ./escanerpython.py <ip>
--------------------------------------------------
Escaneando el objetivo 192.168.X.X
Hora de escaneo XXXX-XX-XX xx:xx:xx.x
--------------------------------------------------
Puerto 21 está abierto
Puerto 22 está abierto
Puerto 23 está abierto
Puerto 25 está abierto
Puerto 53 está abierto
Puerto 80 está abierto
Puerto 111 está abierto
Puerto 139 está abierto
Puerto 445 está abierto
--------------------------------------------------
```
