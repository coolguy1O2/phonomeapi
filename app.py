from flask import Flask, request, jsonify
import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict

app = Flask(__name__)
cmu = cmudict.dict()

@app.route("/")
def home():
    return "Phoneme API is running"

@app.route("/tts", methods=["GET"])
def tts():
    text = request.args.get("text", "").lower()
    words = text.split()
    result = {}
    for word in words:
        if word in cmu:
            result[word] = cmu[word][0]  # Get first phoneme variant
        else:
            result[word] = ["?"]
    return jsonify(result)

# Required for Replit to run it
app.run(host="0.0.0.0", port=81)
