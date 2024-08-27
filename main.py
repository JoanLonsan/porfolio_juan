import streamlit as st
from utils.config import *

def main():
    st.set_page_config(page_title=PAGE_TITLE,
                       page_icon=PAGE_ICON,
                       layout=LAYOUT,
                       initial_sidebar_state=INIT_COLLID_BAR)

    st.markdown(HIDE_IMG_FS, unsafe_allow_html=True)

    pages = {
        "Juan Crescenti": [
            st.Page("pages/00_juancres.py",
                    title="Sobre mí",
                    icon="👱🏻",
                    default=True),
        ],
        " Análisis Deportivo": [
            st.Page("pages/01_sport_analisis.py",
                    title="01. Predicción Altura de Salto",
                    icon="⛹🏽‍♂️"),
        ],
        "Proyecto 2": [
            st.Page("pages/02_ml.py",
                    title="Presentación_02",
                    icon="👾"),
        ],
        "Proyecto 3": [
            st.Page("pages/03_info.py",
                    title="Presentación_03",
                    icon="🖖"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    main()