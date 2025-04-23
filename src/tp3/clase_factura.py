# Clase base
class Factura:
    def __init__(self, importe):
        self.importe = importe

    def mostrar_detalle(self):
        raise NotImplementedError("Debe implementar este método en la subclase.")


# Subclases específicas
class FacturaResponsable(Factura):
    def mostrar_detalle(self):
        print(f"Factura A - IVA Responsable\nImporte: ${self.importe:.2f}")


class FacturaNoInscripto(Factura):
    def mostrar_detalle(self):
        print(f"Factura C - IVA No Inscripto\nImporte: ${self.importe:.2f}")


class FacturaExento(Factura):
    def mostrar_detalle(self):
        print(f"Factura E - IVA Exento\nImporte: ${self.importe:.2f}")


# Fábrica
class FacturaFactory:
    @staticmethod
    def crear_factura(importe, condicion_iva):
        condicion = condicion_iva.lower()
        if condicion == "iva responsable":
            return FacturaResponsable(importe)
        elif condicion == "iva no inscripto":
            return FacturaNoInscripto(importe)
        elif condicion == "iva exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Condición impositiva desconocida")


# Uso
factura1 = FacturaFactory.crear_factura(1500, "IVA Responsable")
factura2 = FacturaFactory.crear_factura(1500, "IVA No Inscripto")
factura3 = FacturaFactory.crear_factura(1500, "IVA Exento")

factura1.mostrar_detalle()
factura2.mostrar_detalle()
factura3.mostrar_detalle()
