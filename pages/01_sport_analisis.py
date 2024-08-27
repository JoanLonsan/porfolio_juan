# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import streamlit as st

# Título principal de la página
st.title("Análisis Deportivo: Predicción Altura de Salto")

# Función para cargar y ajustar el modelo
@st.cache_data
def load_and_train_models():
    # Cargar datos
    df = pd.read_csv("data/page1/c2_data.csv")
    df_numeric = df.drop(columns=['player_id'])
    
    # Preparar datos para el modelo con una variable
    x1 = df_numeric[['Positive Impulse']]
    y = df_numeric["Jump Height (Flight Time)"]
    x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y, test_size=0.2, random_state=42)
    
    # Ajustar el modelo con una variable
    model_1 = LinearRegression()
    model_1.fit(x1_train, y1_train)

    # Preparar datos para el modelo con dos variables
    x2 = df_numeric[['Positive Impulse', 'Peak Power / BM']]
    x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y, test_size=0.2, random_state=42)

    # Ajustar el modelo con dos variables
    model_2 = LinearRegression()
    model_2.fit(x2_train, y2_train)

    # Evaluar el modelo con una variable
    y_pred_1 = model_1.predict(x1_test)
    rmse_1 = np.sqrt(mean_squared_error(y1_test, y_pred_1))
    
    # Evaluar el modelo con dos variables
    y_pred_2 = model_2.predict(x2_test)
    rmse_2 = np.sqrt(mean_squared_error(y2_test, y_pred_2))

    return model_1, model_2, rmse_1, rmse_2

# Crear las pestañas
tab1, tab2, tab3 = st.tabs(["📂 Subject", "🔍 Estudio de Datos", "🛠️ App"])

# Código para la pestaña "Subject"
with tab1:
    st.header("Estudio del Salto en el Deporte (Countermovement Jump)")
    
    with open("data/page1/subject.md", "r") as file:
        markdown_content = file.read()
    
    st.markdown(markdown_content)

# Código para la pestaña "Estudio de Datos"
with tab2:
    st.header("Estudio de Datos")

    # Cargar modelos y datos
    model_1, model_2, rmse_1, rmse_2 = load_and_train_models()

    # Carga y Exploración de los Datos
    df = pd.read_csv("data/page1/c2_data.csv")
    st.subheader("Primeras filas del dataset")
    st.dataframe(df.head())

    # Identificación de Correlaciones
    df_numeric = df.drop(columns=['player_id'])
    corr_matrix = df_numeric.corr()

    # Visualización de la matriz de correlación
    st.subheader("Matriz de Correlación")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix,
                annot=True,
                cmap="coolwarm",
                square=True,
                ax=ax)
    plt.title("Matriz de Correlación")
    st.pyplot(fig)

    # Mostrar RMSE de ambos modelos
    st.subheader("Evaluación del Modelo")
    st.warning(f"RMSE del modelo con Positive Impulse: {rmse_1:.2f}")
    st.success(f"RMSE del modelo con Positive Impulse y Peak Power / BM: {rmse_2:.2f}")

# Código para la pestaña "App"
with tab3:
    # Cargar modelos y datos
    _, model_2, _, _ = load_and_train_models()

    # Sección Interactiva: Predicción basada en los inputs del usuario
    st.subheader("Haz tu Predicción")

    # Espacio para el Resultado de la Predicción
    predict_result = st.empty()
    
    # Inputs del usuario
    positive_impulse_input = st.number_input("Introduce Positive Impulse:",
                                             min_value=400.0,
                                             max_value=1200.0,
                                             step=0.1,
                                             format="%.2f")
    peak_power_bm_input = st.number_input("Introduce Peak Power / BM:",
                                          min_value=50.0,
                                          max_value=100.0,
                                          step=0.1,
                                          format="%.2f")

    # Botón para realizar la predicción
    if st.button("Predecir Jump Height"):
        # Crear el array de entrada para la predicción
        user_input = np.array([[positive_impulse_input, peak_power_bm_input]])

        # Realizar la predicción
        jump_height_prediction = model_2.predict(user_input)

        # Mostrar el resultado de la predicción
        predict_result.success(f"Jump Height (Flight Time): {jump_height_prediction[0]:.2f} cm")
