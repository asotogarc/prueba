import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb  # Para evitar el error de xgboost

# Cargar el modelo
try:
    with open('modelo_entrenado.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("El archivo 'modelo_entrenado.pkl' no se encuentra. Asegúrate de colocarlo en el mismo directorio que este script.")
    st.stop()
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    st.stop()

# Configuración de la página
st.set_page_config(page_title="Predicción de Precio", page_icon="📊", layout="wide")

# Título y descripción
st.title("Predicción de Precio de Alojamiento")
st.write("Ingrese los valores de las características para predecir el precio.")

# Inputs para las características numéricas
st.subheader("Características Numéricas")
accommodates = st.number_input("Accommodates (capacidad)", min_value=0.0, step=1.0, value=2.0)
bathrooms = st.number_input("Bathrooms (baños)", min_value=0.0, step=0.5, value=1.0)
beds = st.number_input("Beds (camas)", min_value=0.0, step=1.0, value=1.0)
bedrooms = st.number_input("Bedrooms (dormitorios)", min_value=0.0, step=1.0, value=1.0)
minimum_nights = st.number_input("Minimum Nights (noches mínimas)", min_value=0.0, step=1.0, value=1.0)
num_comodidades = st.number_input("Num Comodidades (número de comodidades)", min_value=0.0, step=1.0, value=0.0)

# Selección de la ciudad (como variable categórica única)
st.subheader("Ciudad")
cities = ['Mallorca', 'Valencia', 'Girona', 'Málaga', 'Madrid', 'Menorca', 'Sevilla', 'Euskadi']
city = st.selectbox("Selecciona la ciudad", cities)

# Botón para realizar la predicción
if st.button("Predecir Precio"):
    # Crear un DataFrame con las características
    input_data = pd.DataFrame({
        'accommodates': [accommodates],
        'bathrooms': [bathrooms],
        'beds': [beds],
        'bedrooms': [bedrooms],
        'minimum_nights': [minimum_nights],
        'num_comodidades': [num_comodidades],
        'ciudad': [city]  # Ciudad como variable categórica única
    })

    # Realizar la predicción
    try:
        prediction = model.predict(input_data)
        st.success(f"El precio predicho es: {prediction[0]:.2f} €")
    except Exception as e:
        st.error(f"Error al hacer la predicción: {e}")

# Instrucciones
st.markdown("---")
st.write("""
### Instrucciones
1. Descarga el archivo `modelo_entrenado.pkl` desde tu repositorio de GitHub.
2. Colócalo en el mismo directorio que este script (`main.py`).
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Ejecuta la aplicación: `streamlit run main.py`.
5. Ingresa los valores de las características y selecciona una ciudad para predecir el precio.
""")
