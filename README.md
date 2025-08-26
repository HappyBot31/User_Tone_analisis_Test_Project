Этот минимальное веб-приложение для анализа телефонных разговоров.  
Цель автоматически оценивать **тон общения** (положительный / нейтральный / отрицательный) и предлагать **краткие рекомендации** для улучшения разговора.

---

## Model

Используется готовая модель с Hugging Face:

- **Модель:** [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)  это модель с поддержкой русского языка, так как рекомендованная вами работала только с текстом на английском
- **Архитектура:** XLM-RoBERTa  
- **Поддерживаемые языки:** многоязычная модель 
- **Классы:** `negative`, `neutral`, `positive`  

---

## Tools and libraries used
- [Python 3](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) — веб-интерфейс  
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)  
- [PyTorch](https://pytorch.org/) — работа модели  
- [SentencePiece](https://github.com/google/sentencepiece) — токенизация  

---

## Installation

1. Склонировать репозиторий или создать папку проекта.
2. Установить зависимости:

```bash
pip install -r requirements.txt
```
### Файл requirements.txt:
```
streamlit
transformers
torch
sentencepiece
```
---
### Как это работает :

1) Запускаем файл Run_app.bat

2) Пользователь вставляет текст расшифровки звонка в поле ввода.

3) Модель Hugging Face оценивает тональность (positive, neutral, negative).

4) Приложение показывает точность предсказания.

5) В зависимости от тона выводятся 1–2 рекомендации, как улучшить общение. Конец.

## Автор
### Shokirov Said
