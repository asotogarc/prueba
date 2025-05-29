import streamlit as st
import pickle
import numpy as np

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

# Título y descripción de la interfaz
st.title("Predicción de Precio")
st.write("Ingrese los valores de las características para predecir el precio.")

# Inputs para las características numéricas
accommodates = st.number_input("Accommodates", min_value=0.0, step=1.0)
bathrooms = st.number_input("Bathrooms", min_value=0.0, step=0.5)
beds = st.number_input("Beds", min_value=0.0, step=1.0)
bedrooms = st.number_input("Bedrooms", min_value=0.0, step=1.0)
minimum_nights = st.number_input("Minimum Nights", min_value=0.0, step=1.0)
num_comodidades = st.number_input("Num Comodidades", min_value=0.0, step=1.0)

# Selección de la ciudad (característica categórica)
cities = ['Mallorca', 'Valencia', 'Girona', 'Málaga', 'Madrid', 'Menorca', 'Sevilla', 'Euskadi']
city = st.selectbox("Ciudad", cities)

# Botón para realizar la predicción
if st.button("Predecir"):
    # Establecer las características binarias de la ciudad (one-hot encoding)
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
        st.success(f"El precio predicho es: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error al hacer la predicción: {e}")

# Instrucciones para el usuario
st.markdown("---")
st.write("""
### Instrucciones
1. Asegúrate de tener el archivo `modelo_entrenado.pkl` en el mismo directorio que este script.
2. Instala las dependencias ejecutando: `pip install -r requirements.txt`.
3. Corre la aplicación con: `streamlit run main.py`.
4. Ingresa los valores de las características y selecciona una ciudad para predecir el precio.
""")
