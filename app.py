from flask import Flask, request, jsonify
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches

# Initialize Flask app
app = Flask(__name__)

# Load FAQ data
with open('faq_data.json') as f:
    faq_data = json.load(f)

# Preprocess user input
def preprocess(text):
    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word not in stop_words]

# Find the closest matching question
def get_answer(user_input):
    processed_input = preprocess(user_input)
    possible_questions = faq_data.keys()
    matches = get_close_matches(' '.join(processed_input), possible_questions, n=1, cutoff=0.5)
    if matches:
        return faq_data[matches[0]]
    else:
        return "Sorry, I don't have an answer for that."

# Define chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = get_answer(user_message)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
