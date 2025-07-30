from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import time

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# Sentiment detection logic
def detect_sentiment(text, method="vader"):
    if method == "vader":
        score = analyzer.polarity_scores(text)
        compound = score['compound']
        if compound >= 0.05:
            return "Positive"
        elif compound <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    else:  # Use TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"

# Generate response based on sentiment
def generate_response(sentiment):
    if sentiment == "Positive":
        return "That's great to hear! Keep up the positive vibes! 😊"
    elif sentiment == "Negative":
        return "I'm here for you. Things will get better soon. 🌈"
    else:
        return "Thanks for sharing. How can I assist you today? 🤝"

@app.route("/")
def index():
    return render_template("index.html")

# Initial greeting message when chat loads
@app.route("/get_greeting", methods=["GET"])
def get_greeting():
    greeting = {
        "reply": "👋 Hi! I’m Sentie, your sentiment-savvy assistant. How are you feeling today?",
        "sentiment": "Neutral"
    }
    return jsonify(greeting)

# Handle user message and return sentiment-aware reply
@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data.get("message")
    model_choice = data.get("model", "vader")  # Default to VADER

    if not user_message:
        return jsonify({"reply": "Please enter a message.", "sentiment": "Neutral"})

    sentiment = detect_sentiment(user_message, method=model_choice)
    time.sleep(1)  # Typing delay
    bot_reply = generate_response(sentiment)

    return jsonify({
        "reply": bot_reply,
        "sentiment": sentiment
    })

if __name__ == "__main__":
    app.run(debug=True)
