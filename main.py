import streamlit as st
import pickle
import numpy as np
import xgboost as xgb  # Importar xgboost explícitamente

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

# Selección de la ciudad (característica categórica)
st.subheader("Ciudad")
cities = ['Mallorca', 'Valencia', 'Girona', 'Málaga', 'Madrid', 'Menorca', 'Sevilla', 'Euskadi']
city = st.selectbox("Selecciona la ciudad", cities)

# Botón para realizar la predicción
if st.button("Predecir Precio"):
    # Codificación one-hot para la ciudad
    ciudad_Mallorca = 1 if city == 'Mallorca' else 0
    ciudad_Valencia = 1 if city == 'Valencia' else 0
    ciudad_Girona = 1 if city == 'Girona' else 0
    ciudad_Málaga = 1 if city == 'Málaga' else 0
    ciudad_Madrid = 1 if city == 'Madrid' else 0
    ciudad_Menorca = 1 if city == 'Menorca' else 0
    ciudad_Sevilla = 1 if city == 'Sevilla' else 0
    ciudad_Euskadi = 1 if city == 'Euskadi' else 0

    # Crear el vector de características en el orden correcto
    input_data = [
        accommodates,
        bathrooms,
        ciudad_Mallorca,
        ciudad_Valencia,
        ciudad_Girona,
        ciudad_Málaga,
        beds,
        bedrooms,
        ciudad_Madrid,
        ciudad_Menorca,
        ciudad_Sevilla,
        ciudad_Euskadi,
        minimum_nights,
        num_comodidades
    ]
    input_data = np.array([input_data])

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
