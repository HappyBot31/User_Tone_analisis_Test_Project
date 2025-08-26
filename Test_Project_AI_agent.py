import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment" # Загрузка готовой модели Hugging Face с поддержкой русского языка
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast = False) # токенизация
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = ["negative", "neutral", "positive"]

def analyze_sentiment(text: str): # Функция вычесления тона
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True) # Преобразование текста 
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1) # Прогнозирование
    label_id = torch.argmax(probs, dim=1).item()
    confidence = probs[0][label_id].item() # Выдача точности модели
    return labels[label_id], confidence # Возвращение вычесленной тональности

def give_recommendations(sentiment: str): # Функция выдачи рекомендации (бесплатная версия без индивидуальных отзывов)
    if sentiment == "negative":
        return [
            "Попробуйте смягчить выражения и использовать более нейтральные слова. Сосредоточьтесь на конструктивных предложениях вместо критики."
        ]
    elif sentiment == "neutral":
        return [
            "Можно добавить больше положительных эмоций, чтобы поддержать собеседника. Попробуйте использовать примеры или похвалу, чтобы оживить разговор."
        ]
    elif sentiment == "positive":
        return [
            "Отличный тон! Продолжайте выражать поддержку и доброжелательность. Можно добавить благодарность или комплимент для усиления эффекта."
        ]
    return []

# Интерфейс на Streamlit
st.title("Анализ тона общения ")

user_input = st.text_area("Введите текст :")

if st.button("Начать Проверку"):
    if user_input.strip():
        sentiment, conf = analyze_sentiment(user_input)
        st.write(f"**Тон:** {sentiment}")
        st.write(f"**Точность:** {conf:.2f}")

        st.subheader("Рекомендации для улучшения общения:")
        for rec in give_recommendations(sentiment):
            st.write(f"- {rec}")
    else:
        st.warning("Введите текст для анализа")