import streamlit as st

st.title("Hello!")

tab1, tab2 = st.tabs(["🙎🏼Sobre mi", "📚Mis Proyectos"])

with tab1:
    st.markdown("""
    ¡Hola! Soy Juan Crescenti, un apasionado del análisis de datos y la modelización predictiva en el ámbito deportivo.
    
    Puedes conocer más sobre mi experiencia y proyectos en:
    - [Juan Crescenti en LinkedIn](https://www.linkedin.com/in/juancrescenti/)
    - [Juan Crescenti en Github](https://github.com/JoanLonsan?tab=repositories)
    """)

with tab2:
    st.subheader("01. Análisis deportivo - Estudio del Salto")