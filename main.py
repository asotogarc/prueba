import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Interfaz Sencilla", page_icon="📊", layout="wide")

# Título y descripción
st.title("Interfaz Sencilla con Streamlit")
st.write("Una aplicación simple para cargar datos, mostrarlos y visualizar un gráfico.")

# Barra lateral para cargar archivo
st.sidebar.header("Cargar Datos")
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])

# Contenido principal
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Mostrar los datos
    st.subheader("Datos Cargados")
    st.dataframe(df.head())
    
    # Selección de columna para gráfico
    st.subheader("Visualización")
    column = st.selectbox("Selecciona una columna para graficar", df.columns)
    
    # Crear y mostrar gráfico
    fig, ax = plt.subplots()
    df[column].plot(kind='hist', ax=ax)
    ax.set_title(f"Histograma de {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)
else:
    st.info("Por favor, sube un archivo CSV para comenzar.")

# Pie de página
st.markdown("---")
st.write("Creado con Streamlit | Ejemplo sencillo")
