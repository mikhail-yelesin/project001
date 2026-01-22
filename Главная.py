import streamlit as st

st.set_page_config(page_title="Учусь Streamlit", layout="wide")

st.title("🚀 Мой первый Streamlit-проект!!!!!")

name = st.text_input("Как тебя зовут?")

if name:
    st.success(f"Привет, {name}!")

if st.button("Проверка"):
    st.write("VS Code + Streamlit работают!!! 🎉")

#with st.sidebar:
st.header("⚙️ Настройки")
threshold = st.slider("Порог", 0, 100, 50)
st.write("Текущий порог:", threshold)