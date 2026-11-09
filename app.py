import streamlit as st
import os
import sys

st.title("Diagnóstico del proyecto")

# Mostrar ubicación de ejecución
st.write("Directorio actual:")
st.write(os.getcwd())

# Mostrar archivos encontrados
st.write("Archivos y carpetas:")
st.write(os.listdir("."))

# Comprobar carpeta modulos
st.write("¿Existe la carpeta modulos?")
st.write(os.path.isdir("modulos"))

# Comprobar contenido de modulos
if os.path.isdir("modulos"):
    st.write("Contenido de modulos:")
    st.write(os.listdir("modulos"))

# Mostrar ruta de búsqueda de Python
st.write("Rutas de búsqueda de Python:")
st.write(sys.path)
