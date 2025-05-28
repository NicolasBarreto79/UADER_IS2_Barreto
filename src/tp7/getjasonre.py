#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJson.py - versión 1.1

Copyright UADER-FCyT-IS2 ©2024 todos los derechos reservados

Este programa accede a un archivo JSON y busca una clave determinada.
Implementa el patrón Singleton para asegurar una única instancia de lectura.
Controla robustamente todos los errores y puede ejecutarse desde línea de comandos.
"""

import json
import sys
import os


class JsonReaderBase:
    """
    Clase base abstracta para acceso a archivos JSON.
    Permite implementar branching by abstraction.
    """
    def search_key(self):
        raise NotImplementedError("Método no implementado")


class JSONReaderSingleton(JsonReaderBase):
    """
    Clase Singleton que gestiona la lectura de archivos JSON y búsqueda de claves.
    """

    _instance = None

    def __new__(cls, filename, key):
        if cls._instance is None:
            cls._instance = super(JSONReaderSingleton, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filename, key):
        if not self._initialized:
            self.filename = filename
            self.key = key
            self.data = None
            self.obj = None
            self._initialized = True

    def read_file(self):
        """
        Intenta leer el contenido del archivo JSON.
        """
        if not os.path.isfile(self.filename):
            print(f"Error: El archivo '{self.filename}' no existe.")
            return False

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = file.read()
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False
        return True

    def parse_json(self):
        """
        Intenta convertir el texto leído a objeto JSON.
        """
        try:
            self.obj = json.loads(self.data)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.filename}' no tiene formato JSON válido.")
            return False
        return True

    def search_key(self):
        """
        Busca la clave dentro del objeto JSON cargado.
        """
        if self.obj is None:
            print("Error: Objeto JSON no cargado correctamente.")
            return

        if self.key in self.obj:
            print(f"Valor de '{self.key}': {self.obj[self.key]}")
        else:
            print(f"Error: La clave '{self.key}' no existe en el archivo.")


def main():
    """
    Función principal que interpreta argumentos de línea de comandos y ejecuta la lógica.
    """

    # Verificar si el usuario pidió la versión
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("getJson.py versión 1.1")
        return

    # Nombre del archivo y clave con valores por defecto
    filename = "sitedata.json"
    key = "token1"

    # Procesar argumentos si existen
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        key = sys.argv[2]
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) > 3:
        print("Uso: python getJson.py [archivo.json] [clave] o python getJson.py -v")
        return

    # Crear instancia Singleton y ejecutar lógica
    reader = JSONReaderSingleton(filename, key)

    if reader.read_file() and reader.parse_json():
        reader.search_key()


if __name__ == "__main__":
    main()
