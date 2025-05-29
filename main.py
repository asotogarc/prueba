import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Configuración de la página
st.set_page_config(page_title="Interfaz Simple", page_icon="👋", layout="wide")

# Cargar el modelo desde el archivo
try:
    with open('modelo_entrenado (1).pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("El archivo 'modelo_entrenado (1).pkl' no se encuentra. Asegúrate de colocarlo en el mismo directorio que este script.")
    st.stop()
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    st.stop()

# Título
st.title("Hi")

# Inputs para las características numéricas
st.subheader("Características Numéricas")
col1, col2 = st.columns(2)
with col1:
    accommodates = st.number_input("Accommodates (capacidad)", min_value=0.0, step=1.0, value=2.0)
    bathrooms = st.number_input("Bathrooms (baños)", min_value=0.0, step=0.5, value=1.0)
    beds = st.number_input("Beds (camas)", min_value=0.0, step=1.0, value=1.0)
    bedrooms = st.number_input("Bedrooms (dormitorios)", min_value=0.0, step=1.0, value=1.0)
    minimum_nights = st.number_input("Minimum Nights (noches mínimas)", min_value=0.0, step=1.0, value=1.0)
    num_comodidades = st.number_input("Num Comodidades (número de comodidades)", min_value=0.0, step=1.0, value=0.0)
with col2:
    longitud_descripcion = st.number_input("Longitud Descripción", min_value=0.0, step=1.0, value=0.0)
    longitud_resumen_barrio = st.number_input("Longitud Resumen Barrio", min_value=0.0, step=1.0, value=0.0)
    amenities_tiene_wifi = st.selectbox("Tiene WiFi", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    amenities_tiene_coffee = st.selectbox("Tiene Cafetera", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    amenities_tiene_kitchen = st.selectbox("Tiene Cocina", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    amenities_tiene_washer = st.selectbox("Tiene Lavadora", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    amenities_tiene_clothing = st.selectbox("Tiene Espacio para Ropa", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
    barrio_tiene_restaurants = st.selectbox("Barrio Tiene Restaurantes", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")

# Selección de la ciudad
st.subheader("Ciudad")
cities = ['Euskadi', 'Girona', 'Madrid', 'Mallorca', 'Menorca', 'Málaga', 'Sevilla', 'Valencia']
city = st.selectbox("Selecciona la ciudad", cities)

# Selección del tipo de habitación
st.subheader("Tipo de Habitación")
room_types = ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']
room_type = st.selectbox("Selecciona el tipo de habitación", room_types)

# Opciones: Mostrar mensaje o realizar predicción
st.subheader("Opciones")
opcion = st.radio("Selecciona una acción:", ["Mostrar mensaje 'hi'", "Realizar predicción"])

# Botón para ejecutar la acción seleccionada
if st.button("Ejecutar"):
    if opcion == "Mostrar mensaje 'hi'":
        st.write("hi")
    else:
        # Crear un DataFrame con las características
        input_data = pd.DataFrame({
            'accommodates': [accommodates],
            'bathrooms': [bathrooms],
            'beds': [beds],
            'bedrooms': [bedrooms],
            'minimum_nights': [minimum_nights],
            'num_comodidades': [num_comodidades],
            'longitud_descripcion': [longitud_descripcion],
            'longitud_resumen_barrio': [longitud_resumen_barrio],
            'amenities_tiene_wifi': [amenities_tiene_wifi],
            'amenities_tiene_coffee': [amenities_tiene_coffee],
            'amenities_tiene_kitchen': [amenities_tiene_kitchen],
            'amenities_tiene_washer': [amenities_tiene_washer],
            'amenities_tiene_clothing': [amenities_tiene_clothing],
            'barrio_tiene_restaurants': [barrio_tiene_restaurants],
            'ciudad': [city],
            'room_type': [room_type]
        })
        # Realizar la predicción
        try:
            precio_predicho_sqrt = model.predict(input_data)
            precio_predicho = precio_predicho_sqrt[0] ** 2  # Deshacer la transformación raíz cuadrada
            st.success(f"El precio predicho es: {precio_predicho:.2f} €")
        except Exception as e:
            st.error(f"Error al hacer la predicción: {e}")

# Instrucciones
st.markdown("---")
st.write("""
### Instrucciones
1. Descarga el archivo `modelo_entrenado (1).pkl` desde tu repositorio GitHub (asotogarc/prueba).
2. Colócalo en el mismo directorio que este script (`main.py`).
3. Instala las dependencias: `pip install streamlit pandas numpy scikit-learn`.
4. Ejecuta la aplicación: `streamlit run main.py`.
5. Ingresa los valores de las características, selecciona una ciudad y un tipo de habitación.
6. Elige una acción: mostrar el mensaje 'hi' o realizar una predicción.
7. Haz clic en "Ejecutar" para ver el resultado.
""")
