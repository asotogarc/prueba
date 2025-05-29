import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Interfaz Simple", page_icon="📊", layout="wide")

# Título simplificado
st.title("Hi")
st.write("Ingrese los valores de las características para visualizarlas.")

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

# Botón para mostrar el gráfico
if st.button("Mostrar Valores"):
    # Crear un DataFrame con las características
    input_data = pd.DataFrame({
        'accommodates': [accommodates],
        'bathrooms': [bathrooms],
        'beds': [beds],
        'bedrooms': [bedrooms],
        'minimum_nights': [minimum_nights],
        'num_comodidades': [num_comodidades],
        'ciudad': [city]
    })

    # Crear gráfico simple con Plotly
    features = ['accommodates', 'bathrooms', 'beds', 'bedrooms', 'minimum_nights', 'num_comodidades']
    values = [accommodates, bathrooms, beds, bedrooms, minimum_nights, num_comodidades]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=features,
            y=values,
            marker_color='lightcoral',
            text=[f"{v:.1f}" for v in values],
            textposition='auto'
        )
    )

    # Actualizar diseño
    fig.update_layout(
        title_text=f"Valores Ingresados para {city}",
        xaxis_title="Características",
        yaxis_title="Valor",
        height=400,
        width=800,
        showlegend=False
    )

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# Instrucciones
st.markdown("---")
st.write("""
### Instrucciones
1. Ingresa los valores de las características y selecciona una ciudad.
2. Haz clic en "Mostrar Valores" para ver un gráfico de los valores ingresados.
3. Instala las dependencias: `pip install streamlit pandas plotly`.
4. Ejecuta la aplicación: `streamlit run main.py`.
""")
