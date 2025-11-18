from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.json
    text = data.get("text", "")
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    sentiment_result = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    
    return jsonify({
        "text": text,
        "polarity": polarity,
        "sentiment": sentiment_result
    })

@app.route("/", methods=["GET"])
def home():
    return "Sentiment Analysis API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
