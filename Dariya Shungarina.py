import streamlit as st
import pandas as pd
import json
import os

# 1. Настройка файла для хранения данных
DATA_FILE = "expenses.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 2. Интерфейс приложения
st.title("💰 Мой трекер расходов")

# Функция добавления (Функция №1 по заданию)
st.subheader("Добавить новый расход")
amount = st.number_input("Сумма", min_value=0)
category = st.selectbox("Категория", ["Еда", "Транспорт", "Развлечения", "Учеба", "Другое"])

if st.button("Сохранить"):
    if amount > 0:
        data = load_data()
        data.append({"Сумма": amount, "Категория": category})
        save_data(data)
        st.success("Данные сохранены!")
    else:
        st.warning("Введите сумму больше 0")

# Функция просмотра (Функция №2 по заданию)
st.subheader("История расходов")
current_data = load_data()
if current_data:
    df = pd.DataFrame(current_data)
    st.table(df) # Показываем таблицу
    
    # Бонус: простой график
    if st.checkbox("Показать график"):
        chart_data = df.groupby("Категория")["Сумма"].sum()
        st.bar_chart(chart_data)
else:
    st.info("Расходов пока нет.")
