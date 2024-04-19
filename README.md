
# Mona Lisa

Este proyecto utiliza inteligencia artificial para detectar emociones en tiempo real a través de una webcam. Según la emoción detectada en la persona, se muestra una imagen correspondiente de la Mona Lisa con la emoción reflejada.

## Características

- **Detección de Emociones en Tiempo Real**: Utiliza la cámara web para analizar las emociones faciales del usuario.
- **Cambio Dinámico de Imagen**: Cambia la imagen de la Mona Lisa según la emoción detectada.
- **Interfaz Gráfica de Usuario**: Dos ventanas que muestran la captura de la webcam y la Mona Lisa emocionalmente correspondiente.

## Dependencias

Este proyecto depende de varias bibliotecas de Python:

> Python 3.11

El siguiente proyecto usa las siguientes dependencias en las versiones:

1. OpenCv [4.9.0.80]
2. DeepFace [0.0.90]
3. TensorFlow [2.16.1]
4. Tkinter [0.1.0]
5. PIL [10.3.0]
6. tf-keras [2.16.0]

- **OpenCV**: Para la captura y manipulación de imágenes de la webcam.
- **DeepFace**: Para el análisis de emociones en tiempo real.
- **TensorFlow**: Requerido por DeepFace.
- **Tkinter**: Para la creación de la interfaz gráfica.
- **PIL**: Para la manipulación de imágenes dentro de Tkinter.

Para instalar todas las dependencias necesarias, puedes usar el siguiente comando:

\`\`\`bash
pip install opencv-python tensorflow deepface tkinter Pillow tf-keras
\`\`\`

## Estructura del Proyecto

El proyecto está estructurado en los siguientes archivos principales:

- `app.py`: Contiene la lógica principal del programa, incluyendo la captura de webcam, detección de emociones y la interfaz gráfica.
- `mona_lisa_images/`: Directorio que contiene las diferentes imágenes de la Mona Lisa con varias expresiones emocionales.

## Uso

Para ejecutar la aplicación, simplemente corre el siguiente comando en tu terminal:

\`\`\`bash
python app.py
\`\`\`

Asegúrate de que tu webcam esté conectada y funcional antes de ejecutar la aplicación.

## Licencia

Este proyecto está bajo licencia MIT. Para más detalles, consulta el archivo `LICENSE` incluido en este repositorio.
