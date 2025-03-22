# ReciApi's
## 🍽️ **Generador de Recetas con IA (Mistral)**

## **Objetivo de la Aplicación**

El **Generador de Recetas con IA** es una aplicación creada para ayudarte a generar recetas saludables utilizando los ingredientes que tengas a tu disposición. La inteligencia artificial (IA) de **Mistral AI** genera recetas equilibradas y fáciles de preparar a partir de los ingredientes que le proporciones. Solo tenes que ingresar una lista de ingredientes y la IA generará una receta completa para ti, incluyendo:

- Nombre del plato
- Descripción breve
- Pasos de preparación
- Posibles variaciones

Este proyecto busca hacer más fácil la creación de recetas personalizadas sin necesidad de buscar en diferentes fuentes.

## **Tecnologías Usadas**

- **Streamlit**: Framework para crear la interfaz web interactiva.
- **Hugging Face + Mistral AI**: Inteligencia artificial para generar recetas basadas en el lenguaje natural.
- **Requests**: Para interactuar con la API de Hugging Face y obtener respuestas de la IA.

## **Cómo Usar la Aplicación**

### Paso 1: Ejecutar la Aplicación**
Para comenzar, asegúrate de tener **Streamlit** y **requests** instalados. Si aún no los tienes, puedes instalarlos con el siguiente comando en tu terminal:

```bash
pip install streamlit requests
```
### Paso 2: Ejecutar la App
Una vez que hayas guardado el código en un archivo llamado app.py, abre la terminal y navega hasta la carpeta donde se encuentra tu archivo. Luego, ejecuta el siguiente comando para iniciar la aplicación:

```bash
streamlit run app.py
```

## Paso 3: Ingresar los Ingredientes
En la interfaz de Streamlit, verás un campo de texto donde puedes ingresar una lista de ingredientes. Separa los ingredientes con comas. Por ejemplo, puedes ingresar algo como:

```
tomate, pollo, zanahoria, arroz
```

## Paso 4: Generar la Receta
Una vez que hayas ingresado los ingredientes, haz clic en el botón "Generar Receta". La IA comenzará a procesar la información y generará una receta basada en los ingredientes que proporcionaste

## Paso 5: Ver la receta


Después de unos momentos, la IA generará la receta y la mostrará en la pantalla. La receta incluirá:

- El nombre del plato
- Una breve descripción del platillo
- Los pasos para prepararlo
- Variaciones posibles para modificar la receta

## Paso 6: Repetir

Si deseas generar más recetas, solo teenes que ingresar una nueva lista de ingredientes y hacer clic nuevamente en **"Generar Receta"**.


## Posibles errores ❌

- Error 403 o 404 al usar Hugging Face: Si recibes un error relacionado con el modelo de Hugging Face, verifica que tu token de API esté correctamente configurado y que el modelo sea accesible. Si el modelo de Mistral no está disponible, podes probar con otros modelos de Hugging Face, como HuggingFaceH4/zephyr-7b-alpha.

- La app no se inicia: Si al intentar ejecutar streamlit run app.py no se abre la aplicación en el navegador, asegurate de estar en la carpeta correcta y de tener las dependencias instaladas.

- La receta tarda en generarse: Si la IA tarda más de lo esperado, es posible que los servidores de Hugging Face estén ocupados o que el modelo necesite más tiempo para procesar la solicitud.