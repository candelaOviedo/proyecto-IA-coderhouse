import streamlit as st
import requests

# Configuración de la API de Hugging Face (Reemplaza con tu token)
HUGGINGFACE_API_KEY = "API_KEY_DE_HUGGINFACE"
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"

HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# Función para generar recetas con IA usando Mistral
def generar_receta(ingredientes):
    prompt = f"""
    Genera una receta saludable utilizando los siguientes ingredientes: {ingredientes}. 
    La receta debe incluir el nombre del plato, una breve descripción, los pasos de preparación y posibles variaciones. 
    Asegúrate de que sea equilibrada y fácil de preparar.
    """
    
    data = {"inputs": prompt}
    respuesta = requests.post(API_URL, headers=HEADERS, json=data)

    if respuesta.status_code == 200:
        return respuesta.json()[0]['generated_text']
    else:
        return f"Error: {respuesta.status_code}, {respuesta.text}"

# Interfaz de la aplicación con Streamlit
st.title("RecieApi´s")
st.title("🍽️ Generador de Recetas con IA (Mistral)")
st.write("Ingresa los ingredientes que tienes y la IA generará una receta saludable para ti.")

# Campo de entrada para ingredientes
ingredientes = st.text_area("Lista de ingredientes (separados por comas):")

if st.button("Generar Receta"):
    if ingredientes:
        receta = generar_receta(ingredientes)
        st.subheader("Aquí tienes tu receta:")
        st.write(receta)
    else:
        st.warning("Por favor, ingresa al menos un ingrediente.")
