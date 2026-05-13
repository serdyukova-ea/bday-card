import json
import streamlit as st
from streamlit_lottie import st_lottie

# 1. Настройка страницы
st.set_page_config(page_title="С днём рождения!", page_icon="❤️", layout="centered")

# 2. Функция для загрузки локального JSON-файла анимации
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Загружаем файл котика
lottie_cat = load_lottiefile("cat.json")
lottie_bear = load_lottiefile("Floss_Bear.json")


# 3. Кастомизация через CSS (только градиент на весь экран)
st.markdown("""
    <style>
    /* Делаем фон всего сайта абсолютно белым */
    .stApp {
        background-color: white !important;
        background: white !important;
    }

    /* Гарантируем прозрачность контейнеров для анимаций */
    iframe, [data-testid="stLottie"], .main .block-container {
        background-color: white !important;
        background: white !important;
    }

    /* Основной текст делаем черным и центрируем */
    h1, p {
        color: #000000 !important;
        text-align: left;
    }

     /* !!! ИСПРАВЛЕНО: Применяем стили ко ВСЕМ внутренним элементам подписи под фото !!! */
    div[data-testid="stImageCaption"],
    div[data-testid="stImageCaption"] *,
    div[class*="caption"] * {
        color: #000000 !important;        /* Глубокий черный цвет */
        text-align: center !important;     /* Строго по центру */
        font-weight: normal !important;    /* Обычный шрифт, не жирный */
    }
    
    /* Центрируем контейнер кнопки */
    div.stButton {
        text-align: center !important;
    }

    /* Стили для кнопки (Нежно-голубая по умолчанию) */
    div.stButton > button {
        background-color: #cce2ff !important; /* Нежно-голубой */
        color: #1c3d5a !important;           /* Тёмно-синий текст */
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
        display: inline-block !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03) !important;
    }

    /* Эффект при наведении (Кнопка становится нежно-розовой) */
    div.stButton > button:hover {
        background-color: #ffcce2 !important; /* Нежно-розовый */
        color: #5a1c3d !important;           /* Темно-бордовый текст */
        transform: scale(1.05);               
    }

    /* ИСПРАВЛЕНО: Перекрашиваем зеленую плашку st.success в нежно-голубой цвет */
    div[data-testid="stAlert"], div.stAlert {
        background-color: #cce2ff !important; /* Тот же нежно-голубой */
        border: none !important;
        border-radius: 10px !important;
    }
    
    /* Текст внутри нежно-голубого уведомления */
    div[data-testid="stAlert"] p {
        color: #1c3d5a !important;
        text-align: center !important;        /* По центру */
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ВЕРНУЛИ ЗАГОЛОВОК
st.title("С днём рождения, Савелий! 😽")

# ВЕРНУЛИ ВЫЗОВ АНИМАЦИИ (теперь котик отобразится сверху)
st_lottie(lottie_cat, height=400, key="main_cat")

st.write("""
Любимый, в тебе есть столько качеств, которые я люблю. Пусть они всегда остаются с тобой, несмотря на возраст.
Люблю тебя за юмор и шутки, за искренность и честность, за доброту и ум. Спасибо тебе, что ты есть! ❤️
""")

# 5. Фотогалерея
col1, col2 = st.columns(2)
with col1:
    st.image("tom_yam.jpg", caption="Любитель Фо-Бо")
with col2:
    st.image("lima.jpg", caption="и просто вкусненько покушать")

col3, col4 = st.columns(2)
with col3:
    st.image("relax.jpg", caption="Просто чилловый парень")
with col4:
    st.image("poza.jpg", caption="который рожден для вестерна 😎")

col5, col6 = st.columns(2)
with col5:
    st.image("buterfly.jpg", caption="Парень с красивыми глазами")
with col6:
    st.image("ny.jpg", caption="и милой улыбкой")

col7, col8 = st.columns(2)
with col7:
    st.image("sleep.jpg", caption="Парень, который любит поспать")
with col8:
    st.image("chips.jpg", caption="и чипсеки с медовушкой")

col9, col10 = st.columns(2)
with col9:
    st.image("dif.jpg", caption="Ты можешь быть разным")
with col10:
    st.image("wow.jpg", caption="ОЧЕНЬ разным")

col11, col12 = st.columns(2)
with col11:
    st.image("adv.jpg", caption="Любитель путешествий")
with col12:
    st.image("kiss.jpg", caption="и прогулок")

col13, col14 = st.columns(2)
with col13:
    st.image("game.jpg", caption="Профи в настолках")
with col14:
    st.image("kviz.jpg", caption="и квизах")

col_centr = st.columns(1)[0]
with col_centr:
    st.image("trio.jpg", caption="Взрослеем только снаружи — внутри остаемся прежними")

# 6. Интерактив
st.divider()
if st.button("Нажми, чтобы загадать желание"):
    st.balloons()
    # Вызываем мишку через правильный st_lottie
    st_lottie(lottie_bear, height=300, key="bear_button")
    st.success("Пусть все твои мечты сбываются!✨")