import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Clasificador de Imágenes", page_icon="🧠")

# Requerimiento: Incluir el nombre del desarrollador
st.title("Clasificador de Imágenes con IA 🖼️")
st.markdown("**Desarrollado por: Javier** | *Examen - Computación en la Nube (UTH)*")
st.divider()

# Nombres de las clases de CIFAR-10 en español
nombres_clases = ['Avión', 'Auto', 'Pájaro', 'Gato', 'Ciervo', 
                  'Perro', 'Rana', 'Caballo', 'Barco', 'Camión']

# Función para cargar el modelo (caché para que no se recargue en cada interacción)
@st.cache_resource
def cargar_modelo():
    # Asegúrate de que el archivo modelo_cifar10.h5 esté en la misma carpeta
    return tf.keras.models.load_model('modelo_cifar10.h5')

try:
    modelo = cargar_modelo()
except Exception as e:
    st.error(f"Error al cargar el modelo. Verifica que 'modelo_cifar10.h5' esté en la carpeta. Detalles: {e}")
    st.stop()

def procesar_y_predecir(imagen):
    # Convertir a RGB por si la imagen tiene canal Alpha (RGBA)
    if imagen.mode != 'RGB':
        imagen = imagen.convert('RGB')
    
    # Redimensionar a 32x32 píxeles (formato esperado por CIFAR-10)
    img_redimensionada = imagen.resize((32, 32))
    
    # Convertir a arreglo de numpy y normalizar
    img_array = np.array(img_redimensionada) / 255.0
    img_array = np.expand_dims(img_array, axis=0) # Añadir dimensión de lote (batch)
    
    # Realizar predicción
    predicciones = modelo.predict(img_array)
    indice_clase = np.argmax(predicciones[0])
    confianza = np.max(predicciones[0])
    
    return nombres_clases[indice_clase], confianza

st.write("Sube una imagen o toma una foto con tu cámara para que la Inteligencia Artificial identifique el objeto.")

# Pestañas para elegir el método de entrada
tab1, tab2 = st.tabs(["📁 Subir Imagen", "📸 Usar Cámara"])

imagen_usuario = None

with tab1:
    archivo_subido = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])
    if archivo_subido is not None:
        imagen_usuario = Image.open(archivo_subido)

with tab2:
    foto_camara = st.camera_input("Toma una foto")
    if foto_camara is not None:
        imagen_usuario = Image.open(foto_camara)

# Procesar la imagen si el usuario proporcionó una
# Procesar la imagen si el usuario proporcionó una
if imagen_usuario is not None:
    # Selecciona el archivo original para mostrar en la interfaz y evitar el TypeError
    imagen_a_mostrar = archivo_subido if archivo_subido is not None else foto_camara
    st.image(imagen_a_mostrar, caption="Imagen cargada", use_container_width=True)
    
    with st.spinner("Analizando la imagen con el modelo..."):
        clase, confianza = procesar_y_predecir(imagen_usuario)
        
        st.success("¡Análisis completado!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Predicción", value=clase)
        with col2:
            # Mostrar la confianza en formato de 2 decimales (ej. 0.98)
            st.metric(label="Confianza", value=f"{confianza:.2f}")

        # Nota técnica sobre CIFAR-10
        if confianza < 0.60:
            st.warning("Nota: CIFAR-10 está entrenado con imágenes de muy baja resolución (32x32). Las fotos reales muy complejas pueden tener baja confianza.")
