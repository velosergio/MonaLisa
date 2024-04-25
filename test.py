from deepface import DeepFace
import cv2

# Ruta a la imagen que deseas analizar
img_path = 'emociones\img2.jpg'
img = cv2.imread(img_path)

# Verifica que la imagen se haya cargado correctamente
if img is None:
    print("No se pudo cargar la imagen. Verifica la ruta del archivo y el formato de la imagen.")
else:
    # Intenta analizar la imagen con DeepFace
    try:
        result = DeepFace.analyze(img, actions=['emotion'])
        print("Emoción detectada:", result['dominant_emotion'])
    except Exception as e:
        print("Error en la detección de emociones:", e)
