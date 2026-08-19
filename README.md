# Clasificador de Imagenes con IA

**Examen - Computacion en la Nube**  
**Universidad Tecnologica de Honduras (UTH)**  
**Docente:** Ing. Asalia Zavala  
**Desarrollador:** Javier  

---

## Descripcion del Proyecto
Esta aplicacion web implementa un modelo de Machine Learning (Red Neuronal Convolucional) entrenado en Google Colab con el dataset CIFAR-10. La aplicacion permite a los usuarios subir imagenes o tomar fotografias en tiempo real con su camara web para clasificar el objeto principal en la captura.

El modelo es capaz de identificar 10 clases diferentes:
Avion, Auto, Pajaro, Gato, Ciervo, Perro, Rana, Caballo, Barco y Camion.

## Que hace la App y como usarla
La interfaz de la aplicacion esta dividida en dos pestañas principales:

1. Subir Imagen: Haz clic en "Browse files" o arrastra y suelta una imagen desde tu computadora (formatos soportados: JPG, JPEG, PNG). La IA analizara la imagen automaticamente una vez cargada.
2. Usar Camara: Concede permisos de camara a tu navegador si es la primera vez que la usas. Toma una foto usando el boton integrado. El modelo procesara la captura instantaneamente.

Resultados: Al procesar la imagen, la aplicacion mostrara la clase del objeto identificado (Prediccion) y el nivel de seguridad del modelo sobre su prediccion en escala de 0.00 a 1.00 (Confianza).

## Tecnologias y Herramientas Utilizadas
* Entrenamiento de IA: Google Colab, TensorFlow / Keras.
* Dataset: CIFAR-10.
* Despliegue y Frontend: Streamlit, Streamlit Cloud.
* Gestion de Entorno: Se configuro el archivo requirements.txt con fijacion de versiones para garantizar compatibilidad total en produccion y evitar conflictos entre librerias. Se aplico un parche para compatibilidad de formato .h5 en la lectura de pesos.

## Instalacion y Ejecucion Local
Si deseas correr este proyecto de forma local en tu computadora, sigue estos pasos:

1. Clona este repositorio y entra a la carpeta:
   ```bash
   git clone https://github.com/javiqueso22-design/examencompnube.git
   cd examencompnube
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicacion de Streamlit:
   ```bash
   streamlit run app.py
   ```

## Enlaces de Entrega
* URL Publica de la App: https://examencompnube-javiermoreno.streamlit.app/
* Codigo Fuente: https://github.com/javiqueso22-design/examencompnube.git
