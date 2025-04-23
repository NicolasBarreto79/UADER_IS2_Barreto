class MetodoEntrega:
    def descripcion(self):
        raise NotImplementedError

class EntregaMostrador(MetodoEntrega):
    def descripcion(self):
        return "entrega en mostrador"

class RetiroCliente(MetodoEntrega):
    def descripcion(self):
        return "retiro por el cliente"

class Delivery(MetodoEntrega):
    def descripcion(self):
        return "envío por delivery"

class Hamburguesa:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        print(f"Hamburguesa entregada por: {self.metodo_entrega.descripcion()}")

class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo_entrega):
        if tipo_entrega == "mostrador":
            return Hamburguesa(EntregaMostrador())
        elif tipo_entrega == "retiro":
            return Hamburguesa(RetiroCliente())
        elif tipo_entrega == "delivery":
            return Hamburguesa(Delivery())
        else:
            raise ValueError("Tipo de entrega no válido.")

# Uso
h = HamburguesaFactory.crear_hamburguesa("delivery")
h.entregar()
