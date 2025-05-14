class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def emit(self, emitted_id):
        print(f"\n[Subject] Emite ID: {emitted_id}")
        for observer in self._observers:
            observer.notify(emitted_id)


class Observer:
    def __init__(self, id_esperado):
        self.id_esperado = id_esperado

    def notify(self, emitted_id):
        if self.id_esperado == emitted_id:
            print(f"[{self.__class__.__name__}] ID coincidente detectado: {emitted_id}")


# Implementamos 4 observadores concretos con IDs distintos
class ObsAlpha(Observer):
    def __init__(self):
        super().__init__("A123")

class ObsBeta(Observer):
    def __init__(self):
        super().__init__("B456")

class ObsGamma(Observer):
    def __init__(self):
        super().__init__("C789")

class ObsDelta(Observer):
    def __init__(self):
        super().__init__("D000")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crear sujeto
    subject = Subject()

    # Crear e inscribir observadores
    subject.subscribe(ObsAlpha())
    subject.subscribe(ObsBeta())
    subject.subscribe(ObsGamma())
    subject.subscribe(ObsDelta())

    # Emitir 8 IDs (al menos 4 que coincidan con observadores)
    ids_a_emitir = ["X999", "A123", "B456", "Z111", "C789", "D000", "Y222", "A123"]
    
    for id_em in ids_a_emitir:
        subject.emit(id_em)
