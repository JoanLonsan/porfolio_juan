import streamlit as st

st.title("¡Bienvenido!")

tab1, tab2 = st.tabs(["🙎🏼Sobre mi", "📚Mis Proyectos"])

with tab1:
    st.markdown("""
                ¡Hola! Soy Juan Crescenti, un apasionado programador con una sólida trayectoria en desarrollo de software y una reciente transición al emocionante mundo de la tecnología. Con habilidades destacadas en Python, R, y una variedad de tecnologías emergentes, me dedico a resolver problemas complejos y crear soluciones innovadoras en el ámbito de la Inteligencia Artificial y Machine Learning.

                Tras una carrera en el ámbito comercial y administrativo, decidí redirigir mi carrera hacia el sector tech, donde he acumulado experiencia significativa en proyectos de IA y aprendizaje automático. Mi experiencia incluye el desarrollo de modelos predictivos, el análisis de datos y la implementación de soluciones tecnológicas avanzadas. Actualmente, estoy buscando nuevas oportunidades que me permitan seguir creciendo y aportando valor en un entorno dinámico y desafiante.

                **Habilidades destacadas:**
                - Python, R, Keras, TensorFlow, Scikit-Learn
                - Desarrollo de modelos de Machine Learning y Deep Learning
                - Frameworks y herramientas como Django y Unity
                - Gestión de proyectos y equipos de trabajo

                ¡Conectemos para explorar cómo puedo contribuir a tu equipo o proyecto!
                                
                    - [Juan Crescenti en LinkedIn](https://www.linkedin.com/in/juancrescenti/)
                    - [Juan Crescenti en Github](https://github.com/JoanLonsan?tab=repositories)
    """)

with tab2:
    st.subheader("01. Análisis deportivo - Estudio del Salto")
    st.write("Analizamos un dataset del Countermovement Jump para identificar las variables más influyentes en la altura del salto y construimos un modelo predictivo. Descubre los hallazgos y prueba el modelo en la app.")
