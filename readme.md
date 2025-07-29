# 🤖 Sentiment-Aware Chatbot using Flask & TextBlob

##  Project Overview

This is a simple sentiment-aware chatbot built with **Python**, **Flask**, and **TextBlob**. The chatbot analyzes the emotional tone (sentiment) of user messages and responds with a customized reply depending on whether the input is **positive**, **negative**, or **neutral**.

---

##  Features

- Real-time chat interface with AJAX (no page refresh)
- Sentiment detection (Positive, Negative, Neutral)
- Dynamic replies based on detected sentiment
- Chat bubbles and fade-in animations
- Lightweight and beginner-friendly NLP with TextBlob

---

##  Tech Stack

- Python
- Flask (Backend Web Framework)
- TextBlob (NLP for sentiment)
- HTML, CSS, JS (Frontend)

---

##  Setup Instructions

### 1. Clone the repository or unzip the folder:
```bash
git clone https://github.com/ahmed123ya/internshiptask16
.git
cd internshiptask16

## Install dependencies:

pip install -r requirements.txt
python -m textblob.download_corpora

## Run the Flask App:

python app.py

## Visit in browser:

http://127.0.0.1:5000

Sentiment Classification Logic
We use TextBlob's built-in sentiment analyzer which returns polarity between -1.0 to 1.0:

> 0.1: Positive

< -0.1: Negative

Between -0.1 and 0.1: Neutral