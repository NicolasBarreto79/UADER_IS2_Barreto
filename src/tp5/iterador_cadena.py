class StringIterator:
    def __init__(self, data, reverse=False):
        self._data = data
        self._reverse = reverse
        self._index = len(data) - 1 if reverse else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._reverse:
            if self._index < 0:
                raise StopIteration
            value = self._data[self._index]
            self._index -= 1
            return value
        else:
            if self._index >= len(self._data):
                raise StopIteration
            value = self._data[self._index]
            self._index += 1
            return value


class StringCollection:
    def __init__(self, cadena):
        self._cadena = cadena

    def __iter__(self):
        return StringIterator(self._cadena)

    def reverse_iterator(self):
        return StringIterator(self._cadena, reverse=True)


# --- Ejemplo de uso ---
if __name__ == "__main__":
    coleccion = StringCollection("Hola Mundo")

    print("Recorrido directo:")
    for caracter in coleccion:
        print(caracter, end=" ")

    print("\n\nRecorrido reverso:")
    for caracter in coleccion.reverse_iterator():
        print(caracter, end=" ")
