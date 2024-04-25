import cv2
from deepface import DeepFace
from tkinter import *
from PIL import Image, ImageTk

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Dimensiones deseadas para las imágenes en la interfaz
width, height = 400, 300  # Puedes ajustar estas dimensiones según necesites

# Configuración de la ventana principal para la webcam
root = Tk()
root.title("Webcam")

lmain = Label(root)
lmain.pack(side=LEFT)

# Configuración de la ventana secundaria para la Mona Lisa
mona_window = Toplevel(root)
mona_window.title("Mona Lisa")

mona_label = Label(mona_window)
mona_label.pack()

# Cargar y mostrar la imagen por defecto
default_image_path = 'emociones/mona_neutral.png'
default_image = Image.open(default_image_path)
default_image_resized = default_image.resize((width, height), Image.Resampling.LANCZOS)
default_photo = ImageTk.PhotoImage(default_image_resized)
mona_label.image = default_photo
mona_label.configure(image=default_photo)

def update():
    _, frame = cap.read()
    frame_resized = cv2.resize(frame, (width, height))
    cv2image = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    
    # Detección de emociones
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result['dominant_emotion']
        mona_image_path = f'emociones/mona_{emotion}.png'
        mona_image = Image.open(mona_image_path)
        mona_image_resized = mona_image.resize((width, height), Image.Resampling.LANCZOS)
        mona_photo = ImageTk.PhotoImage(mona_image_resized)
        mona_label.image = mona_photo
        mona_label.configure(image=mona_photo)
    except Exception as e:
        print("Error en la detección de emociones o en la carga de imágenes:", e)

    lmain.after(100, update)  # Actualizar la imagen cada 100 milisegundos

update()  # Iniciar la función de actualización
root.mainloop()