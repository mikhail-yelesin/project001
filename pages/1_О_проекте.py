import streamlit as st

st.set_page_config(page_title="О проекте", layout="wide")

st.title("ℹ️ О проекте")
st.write("Это моя первая многостраничная Streamlit-аппа.")


tab1, tab2, tab3 = st.tabs([
    "Информация о файле",
    "Выравнивание изображения",
    "Бинаризация"
])

with tab1:
    st.write("Информация о файле")

with tab2:
    st.write("Настройки выравнивания")

with tab3:
    st.write("Бинарное изображение")