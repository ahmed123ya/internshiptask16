# 🤖 Sentiment-Aware Chatbot using Flask & TextBlob

##  Project Overview

This is a simple sentiment-aware chatbot built with **Python**, **Flask**, and **TextBlob**. The chatbot analyzes the emotional tone (sentiment) of user messages and responds with a customized reply depending on whether the input is **positive**, **negative**, or **neutral**.

---

##  Features

- Real-time chat with AJAX (no page reload)
- Sentiment analysis using **VADER** (default) or **TextBlob**
- Custom replies for each sentiment
- Chat bubbles for both user and bot
- Typing animation for Sentie
- Initial greeting on page load
- Clean UI with optional model selection

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
pip install flask textblob vaderSentiment
## Run the Flask App:

python app.py

## Visit in browser:

http://127.0.0.1:5000

Sentiment Classification Logic
We use TextBlob's built-in sentiment analyzer which returns polarity between -1.0 to 1.0:

> 0.1: Positive

< -0.1: Negative

Between -0.1 and 0.1: Neutral