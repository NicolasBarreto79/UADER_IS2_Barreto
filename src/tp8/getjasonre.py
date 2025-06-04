#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
getJson.py - versión 1.2

Copyright UADER-FCyT-IS2 ©2025 todos los derechos reservados

Este programa gestiona pagos automáticos usando tokens de bancos almacenados
en un archivo JSON, implementando patrón Singleton para lectura, y cadena
de responsabilidad para el procesamiento de pagos balanceado y controlado.

Incluye listado cronológico de pagos realizados usando patrón iterador.
"""

import json
import sys
import os


class JsonReaderBase:
    """Clase base abstracta para acceso a archivos JSON."""
    def search_key(self):
        raise NotImplementedError("Método no implementado")


class JSONReaderSingleton(JsonReaderBase):
    """Singleton que gestiona lectura y búsqueda de claves en archivo JSON."""

    _instance = None

    def __new__(cls, filename, key=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, filename, key=None):
        if not self._initialized:
            self.filename = filename
            self.key = key
            self.data = None
            self.obj = None
            self._initialized = True

    def read_file(self):
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
        try:
            self.obj = json.loads(self.data)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.filename}' no tiene formato JSON válido.")
            return False
        return True

    def get_token_value(self, token_name):
        if self.obj and token_name in self.obj:
            return self.obj[token_name]
        print(f"Error: La clave '{token_name}' no existe en el archivo JSON.")
        return None


class Payment:
    """Representa un pago realizado."""

    def __init__(self, order_number, token, amount):
        self.order_number = order_number
        self.token = token
        self.amount = amount


class PaymentHandler:
    """
    Handler en cadena para procesar pagos con un token (cuenta)
    y saldo asociado.
    """

    def __init__(self, token, saldo_inicial):
        self.token = token
        self.saldo = saldo_inicial
        self.next_handler = None
        self.payments = []

    def set_next(self, handler):
        self.next_handler = handler

    def handle_payment(self, order_number, amount):
        if self.saldo >= amount:
            self.saldo -= amount
            pago = Payment(order_number, self.token, amount)
            self.payments.append(pago)
            print(f"Pedido {order_number}: pago de ${amount:.2f} realizado con {self.token}. Saldo restante: ${self.saldo:.2f}")
            return True
        elif self.next_handler:
            return self.next_handler.handle_payment(order_number, amount)
        else:
            print(f"Pedido {order_number}: no se pudo realizar el pago de ${amount:.2f}, saldo insuficiente en todas las cuentas.")
            return False

    def get_payments(self):
        return self.payments


class PaymentProcessor:
    """
    Controla la cadena de responsabilidad de handlers y el proceso
    de pagos balanceados entre cuentas.
    """

    def __init__(self, handlers):
        self.handlers = handlers
        # Vincular handlers en cadena
        for i in range(len(handlers) - 1):
            handlers[i].set_next(handlers[i + 1])
        self.current_handler_index = 0  # Para alternar

    def process_payment(self, order_number, amount):
        n = len(self.handlers)
        attempts = 0
        processed = False

        while attempts < n and not processed:
            handler = self.handlers[self.current_handler_index]
            processed = handler.handle_payment(order_number, amount)
            self.current_handler_index = (self.current_handler_index + 1) % n
            attempts += 1

        if not processed:
            print(f"Pedido {order_number}: pago NO realizado, fondos insuficientes.")
        return processed

    def list_all_payments(self):
        # Generar un iterador que recorra cronológicamente todos los pagos
        # Se asume que los pagos están ordenados por orden de registro en cada handler
        all_payments = []
        for handler in self.handlers:
            all_payments.extend(handler.get_payments())

        # Ordenar por número de pedido (order_number)
        all_payments.sort(key=lambda p: p.order_number)
        return all_payments


def main():
    """
    Función principal que interpreta argumentos y realiza procesamiento.
    """

    # Control de versión
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("getJson.py versión 1.2 - Ejecución de pagos con cadena de responsabilidad")
        return

    filename = "sitedata.json"
    # Tokens los vamos a leer del JSON
    # Si el archivo o clave no existen, se maneja luego

    # No se reciben argumentos para token ya que es automático

    reader = JSONReaderSingleton(filename)

    if not (reader.read_file() and reader.parse_json()):
        return

    token1_key = "token1"
    token2_key = "token2"
    token1_value = reader.get_token_value(token1_key)
    token2_value = reader.get_token_value(token2_key)

    if token1_value is None or token2_value is None:
        print("Error: Tokens no encontrados en el JSON.")
        return

    # Inicializamos cuentas con saldo fijo
    handler1 = PaymentHandler(token1_key, 1000.0)
    handler2 = PaymentHandler(token2_key, 2000.0)

    processor = PaymentProcessor([handler1, handler2])

    # Realizar pagos pedidos: pedidos de $500, 6 pedidos para probar alternancia y saldo
    pedidos = [(1, 500), (2, 500), (3, 500), (4, 500), (5, 500), (6, 500)]

    for pedido, monto_pago in pedidos:
        processor.process_payment(pedido, monto_pago)

    print("\nListado completo de pagos realizados:")

    for pago in processor.list_all_payments():
        print(f"Pedido {pago.order_number}: pago de ${pago.amount:.2f} realizado con {pago.token}.")

if __name__ == "__main__":
    main()
