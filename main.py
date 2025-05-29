import streamlit as st

def main():
    # Título de la aplicación
    st.title("Mi aplicación sencilla con Streamlit")

    # Entrada de texto: nombre
    name = st.text_input("¿Cómo te llamas?", placeholder="Tu nombre aquí")

    # Slider: edad
    age = st.slider("¿Cuántos años tienes?", min_value=0, max_value=100, value=25)

    # Botón para procesar la información
    if st.button("Enviar"):
        if name:
            st.success(f"¡Hola {name}! Tienes {age} años.")
        else:
            st.error("Por favor, ingresa tu nombre antes de enviar.")

if __name__ == "__main__":
    main()
