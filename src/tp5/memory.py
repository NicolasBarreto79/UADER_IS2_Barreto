import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo mejorado con historial de 4 estados
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:

	def __init__(self):
		self.history = []

	def save(self, writer):
		if len(self.history) >= 4:
			self.history.pop(0)  # Elimina el más antiguo si ya hay 4
		self.history.append(writer.save())

	def undo(self, writer, index=0):
		if index < len(self.history):
			memento = self.history[-(index + 1)]
			writer.undo(memento)
		else:
			print(f"No hay suficiente historial para deshacer {index} pasos.")


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("\n--- Se graba algo en el objeto y se salva ---")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("--- Se graba información adicional y se salva ---")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("--- Se graba información adicional II y se salva ---")
	writer.write("Más contenido de patrones II\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("--- Se graba información adicional III y se salva ---")
	writer.write("Última parte del ejemplo\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("--- Se graba información adicional IV (sin guardar) ---")
	writer.write("Esto no está guardado todavía\n")
	print(writer.content + "\n")

	print("\n--- Se invoca <undo(0)> (estado inmediatamente anterior) ---")
	caretaker.undo(writer, 0)
	print(writer.content + "\n")

	print("--- Se invoca <undo(2)> (2 estados atrás) ---")
	caretaker.undo(writer, 2)
	print(writer.content + "\n")

	print("--- Se invoca <undo(3)> (3 estados atrás) ---")
	caretaker.undo(writer, 3)
	print(writer.content + "\n")
