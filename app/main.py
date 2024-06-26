from model import QuechuaModel
import streamlit as st

st.set_page_config(
    page_title="Lexemas - Generador de cuentos en Quechua Sureño",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(f"## Lexemas - Generador de cuentos en Quechua Sureño\n---\n")

st.sidebar.title("Parámetros")
prompt = st.text_area("Prompt", height=200)
max_length = st.sidebar.slider("Max Length", 50, 1000, 200)
temperature = st.sidebar.slider("Temperature", 0.1, 1.0, 0.7)
top_k = st.sidebar.slider("Top K", 1, 100, 50)
top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.95)
do_sample = st.sidebar.checkbox("Do Sample", value=True)


if st.button("Generar cuento"):
    if prompt:
        with st.spinner("Generando cuento..."):
            model = QuechuaModel.getInstance()
            story = model.generate_text(
                prompt, max_length, do_sample, temperature, top_k, top_p
            )
            st.markdown(f"---\n**Cuento generado**:\n\n{story}")
    else:
        st.warning("Por favor, ingrese un prompt para generar el cuento.")
