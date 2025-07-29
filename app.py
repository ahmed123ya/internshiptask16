from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
     return "Positive"
    elif polarity < 0.0:
     return "Negative"  
    else:
     return "Neutral"


def generate_response(sentiment):
    if sentiment == "Positive":
        return "That's great to hear! Keep up the positive vibes! 😊"
    elif sentiment == "Negative":
        return "I'm here for you. Things will get better soon. 🌈"
    else:
        return "Thanks for sharing. How can I assist you today? 🙂"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chat():
    user_message = request.form['message']
    sentiment = detect_sentiment(user_message)
    bot_response = generate_response(sentiment)
    return jsonify({
        "response": bot_response,
        "sentiment": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True) 