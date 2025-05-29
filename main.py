import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Interfaz Simple", page_icon="👋", layout="wide")

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

# Coeficientes de la regresión lineal (extraídos del resumen proporcionado)
coeficientes = {
    'const': 11.4817,
    'accommodates': 1.8663,
    'bathrooms': 0.5437,
    'bedrooms': 0.2943,
    'beds': -0.0740,
    'minimum_nights': -0.0421,
    'num_comodidades': 0.3594,
    'longitud_descripcion': -0.0918,
    'longitud_resumen_barrio': 0.0790,
    'amenities_tiene_wifi': 0.3481,
    'amenities_tiene_coffee': -0.1054,
    'amenities_tiene_kitchen': -0.9269,
    'amenities_tiene_washer': -0.2155,
    'amenities_tiene_clothing': -0.4224,
    'barrio_tiene_restaurants': 0.1346,
    'ciudad_Euskadi': -0.0219,
    'ciudad_Girona': -0.8543,
    'ciudad_Madrid': -0.4808,
    'ciudad_Mallorca': 0.4619,
    'ciudad_Menorca': -0.1331,
    'ciudad_Málaga': -0.9250,
    'ciudad_Sevilla': -0.3763,
    'ciudad_Valencia': -0.9442,
    'room_type_Hotel room': 0.2961,
    'room_type_Private room': -2.2214,
    'room_type_Shared room': -3.4089
}

# Función para realizar la predicción manual
def predecir_precio(input_data, coeficientes):
    precio = coeficientes['const']
    for feature in coeficientes:
        if feature != 'const':
            precio += coeficientes[feature] * input_data.get(feature, 0)
    return precio

# Opciones: Mostrar mensaje o realizar predicción
st.subheader("Opciones")
opcion = st.radio("Selecciona una acción:", ["Mostrar mensaje 'hi'", "Realizar predicción"])

# Botón para ejecutar la acción seleccionada
if st.button("Ejecutar"):
    if opcion == "Mostrar mensaje 'hi'":
        st.write("hi")
    else:
        # Crear un diccionario con las características
        input_data = {
            'accommodates': accommodates,
            'bathrooms': bathrooms,
            'beds': beds,
            'bedrooms': bedrooms,
            'minimum_nights': minimum_nights,
            'num_comodidades': num_comodidades,
            'longitud_descripcion': longitud_descripcion,
            'longitud_resumen_barrio': longitud_resumen_barrio,
            'amenities_tiene_wifi': amenities_tiene_wifi,
            'amenities_tiene_coffee': amenities_tiene_coffee,
            'amenities_tiene_kitchen': amenities_tiene_kitchen,
            'amenities_tiene_washer': amenities_tiene_washer,
            'amenities_tiene_clothing': amenities_tiene_clothing,
            'barrio_tiene_restaurants': barrio_tiene_restaurants,
            f'ciudad_{city}': 1,
            f'room_type_{room_type}': 1
        }
        # Realizar la predicción
        precio_predicho = predecir_precio(input_data, coeficientes)
        st.success(f"El precio predicho es: {precio_predicho:.2f} €")

# Instrucciones
st.markdown("---")
st.write("""
### Instrucciones
1. Ingresa los valores de las características numéricas, selecciona una ciudad y un tipo de habitación.
2. Elige una acción: mostrar el mensaje 'hi' o realizar una predicción.
3. Haz clic en "Ejecutar" para ver el resultado.
4. Instala las dependencias: `pip install streamlit pandas numpy`.
5. Ejecuta la aplicación: `streamlit run main.py`.
""")
