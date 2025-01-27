import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple set of predefined responses
responses = {
    "What products do you sell?": "We sell a wide range of products, including electronics, clothing, home goods, beauty products, and more.",
    "How can I contact customer support?": "You can contact our customer support team by emailing support@shopping.com or calling our helpline at +1-800-123-4567.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries. Shipping fees may vary based on location.",
    "What is your return policy?": "We offer a 30-day return policy. You can return most items in new condition within 30 days for a full refund. Some exclusions apply.",
    "How do I track my order?": "Once your order has been shipped, you will receive an email with a tracking number. You can use this number to track your order on our website.",
    "How do I make a payment?": "We accept various payment methods including credit cards, debit cards, PayPal, and other secure payment gateways.",
    "Can I modify or cancel my order after placing it?": "Orders can only be modified or canceled within an hour of placing them. After that, they are processed for shipping.",
    "default": "Sorry, I don't understand that question. Can you please ask something else?"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input'].strip().lower()  # Normalize input by trimming and converting to lowercase

    # Loop through the responses dictionary and check for a match using regex
    for question, answer in responses.items():
        if re.search(question.lower(), user_input):
            return jsonify({'response': answer})

    # If no match is found, return the default response
    return jsonify({'response': responses["default"]})


if __name__ == '__main__':
    app.run(debug=True)
