"""Este módulo proporciona una interfaz para interactuar con el modelo Gemini de Google."""
from google.generativeai import GenerativeModel
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

# Reemplaza con tu clave de API de Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL_NAME = "gemini-1.5-flash"  # Cambiando al modelo sugerido

ultima_consulta = ""

def interactuar_con_gemini(consulta_usuario):
    """
    Acepta una consulta del usuario, la imprime con el prefijo "You:",
    invoca la API de Google Gemini con la consulta y luego imprime
    la respuesta de Gemini con el prefijo "Gemini:".

    Args:
        consulta_usuario (str): La consulta proporcionada por el usuario.
    """
    global ultima_consulta
    if consulta_usuario.strip():
        print(f"You: {consulta_usuario}")
        ultima_consulta = consulta_usuario  # Guarda la última consulta exitosa

        # Inicializa el modelo Gemini
        genai.configure(api_key=GOOGLE_API_KEY)
        model = GenerativeModel(GEMINI_MODEL_NAME)

        try:
            response = model.generate_content(consulta_usuario)
            respuesta_gemini = response.text
            print(f"Gemini: {respuesta_gemini}")
        except Exception as e:
            print(f"Error inesperado al invocar a Gemini: {e}")
    else:
        print("La consulta del usuario está vacía.")

if __name__ == "__main__":
    while True:
        try:
            consulta = input("Ingresa tu consulta (o '^U' para editar la última): ")
            if consulta == '^U' and ultima_consulta:
                prompt = f"Editando la última consulta: '{ultima_consulta}'. "
                nueva_consulta = input(prompt + "Introduce la nueva consulta: ")
                if nueva_consulta.strip():
                    interactuar_con_gemini(nueva_consulta)
                else:
                    print("La nueva consulta está vacía.")
            elif consulta:
                interactuar_con_gemini(consulta)
            else:
                print("No ingresaste ninguna consulta.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado en el bucle principal: {e}")