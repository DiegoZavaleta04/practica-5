import streamlit as st

def mostrar_productos():

    st.header("Gestión de productos")

    st.write(
        "En este módulo se presenta la información "
        "de los productos disponibles en el sistema."
    )

    st.subheader("Registrar producto")

    with st.form("form_productos"):

        nombre = st.text_input("Nombre del producto")

        precio = st.number_input(
            "Precio del producto ($)",
            min_value=0.01,
            step=0.50
        )

        cantidad = st.number_input(
            "Cantidad disponible",
            min_value=0,
            step=1
        )

        guardar = st.form_submit_button(
            "Registrar producto"
        )

        if guardar:
            if nombre.strip() == "":
                st.warning("Ingrese el nombre del producto.")
            else:
                st.success("Producto registrado correctamente.")

    st.divider()

    st.subheader("Información del módulo")

    st.write("Este apartado permitirá gestionar los productos.")
    st.write("Aquí se podrá consultar el nombre, precio y cantidad.")
