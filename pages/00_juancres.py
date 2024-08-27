import streamlit as st

st.title("¡Bienvenido!")

tab1, tab2 = st.tabs(["🙎🏼Sobre mi", "📚Mis Proyectos"])

with tab1:
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image("data/juan.jpg", use_column_width=True)
        _, col, _ = st.columns([1.5, 7, 1.5])
        with col:
            st.write("**Transición y Adaptación**")
            st.write("**Crecimiento y Aprendizaje**")
            st.write("**Machine Learning e IA**")
            st.write("**Metodologías Ágiles**")
    with col2:
        st.markdown("""
                ¡Hola! Soy **Juan Crescenti**, un apasionado programador con una sólida trayectoria en desarrollo de software y una reciente transición al emocionante mundo de la tecnología. Con habilidades destacadas en Python, R, y una variedad de tecnologías emergentes, me dedico a resolver problemas complejos y crear soluciones innovadoras en el ámbito de la Inteligencia Artificial y Machine Learning.

                Tras una carrera en el ámbito comercial y administrativo, decidí redirigir mi futuro profesional hacia el sector Tech, donde he acumulado experiencia significativa en proyectos de IA y aprendizaje automático. Mi experiencia incluye el desarrollo de modelos predictivos, el análisis de datos y la implementación de soluciones tecnológicas avanzadas. Actualmente, estoy buscando nuevas oportunidades que me permitan seguir creciendo y aportando valor en un entorno dinámico y desafiante.

                **Habilidades destacadas:**
                - Python, R, Keras, TensorFlow, Scikit-Learn
                - Desarrollo de modelos de Machine Learning y Deep Learning
                - Frameworks y herramientas como Django y Unity
                - Gestión de proyectos y equipos de trabajo

                ¡Conectemos para explorar cómo puedo contribuir a tu equipo o proyecto!
                                
                - [Juan Crescenti en 🧑‍💼 LinkedIn](https://www.linkedin.com/in/juancrescenti/)
                - [Juan Crescenti en 🤖 Github](https://github.com/JoanLonsan?tab=repositories)

                Y además de amante del mundo Tech, tengo mis hobbies y aficiones que puedes seguir en:
                - [Juan en 📷 Instagram](https://www.instagram.com/joan_lonsan/)
                
                Como verás, los 🎲 juegos de mesa y 📕 rol junto con mi enorme compañero 🐕 Quentin son dos pilares en mi día a día.
        """)

with tab2:
    st.subheader("01. Análisis deportivo - Estudio del Salto")
    st.write("Analizamos un dataset del Countermovement Jump para identificar las variables más influyentes en la altura del salto y construimos un modelo predictivo. Descubre los hallazgos y prueba el modelo en la app.")
