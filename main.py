import streamlit as st

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
with col2:
    bedrooms = st.number_input("Bedrooms (dormitorios)", min_value=0.0, step=1.0, value=1.0)
    minimum_nights = st.number_input("Minimum Nights (noches mínimas)", min_value=0.0, step=1.0, value=1.0)
    num_comodidades = st.number_input("Num Comodidades (número de comodidades)", min_value=0.0, step=1.0, value=0.0)

# Selección de la ciudad
st.subheader("Ciudad")
cities = ['Mallorca', 'Valencia', 'Girona', 'Málaga', 'Madrid', 'Menorca', 'Sevilla', 'Euskadi']
city = st.selectbox("Selecciona la ciudad", cities)

# Botón para mostrar el mensaje
if st.button("Mostrar"):
    st.write("hi")

# Instrucciones
st.markdown("---")
st.write("""
### Instrucciones
1. Ingresa los valores de las características y selecciona una ciudad.
2. Haz clic en "Mostrar" para ver el mensaje 'hi'.
3. Instala la dependencia: `pip install streamlit`.
4. Ejecuta la aplicación: `streamlit run main.py`.
""")
