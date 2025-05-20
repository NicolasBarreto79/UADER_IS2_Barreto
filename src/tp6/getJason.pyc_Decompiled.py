import json
import sys

# Obtiene el nombre del archivo JSON desde los argumentos del sistema, o usa uno por defecto
jsonfile = sys.argv[1] if len(sys.argv) > 1 else "sitedata.json"

# Obtiene la clave a buscar dentro del archivo JSON, o usa una clave por defecto
jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

try:
    # Intenta abrir y leer el archivo JSON especificado
    with open(jsonfile, "r") as myfile:
        data = myfile.read()

    # Intenta convertir el contenido del archivo a un objeto Python
    obj = json.loads(data)

    # Busca la clave especificada dentro del objeto JSON cargado
    if jsonkey in obj:
        print(f"Valor de '{jsonkey}': {obj[jsonkey]}")
    else:
        print(f"Error: La clave '{jsonkey}' no existe en {jsonfile}.")
except FileNotFoundError:
    # Error si el archivo no existe
    print(f"Error: No se encontró el archivo {jsonfile}.")
except json.JSONDecodeError:
    # Error si el contenido del archivo no es un JSON válido
    print(f"Error: El archivo {jsonfile} no tiene un formato JSON válido.")
