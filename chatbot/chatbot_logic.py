import spacy
from chatbot.faq_data import faq_data  # Assuming faq_data is a list of FAQs with questions and answers

# Load the SpaCy model for NLP
nlp = spacy.load("en_core_web_sm")

# Function to generate a response based on user input and conversation history
def get_response(user_input, conversation_history):
    user_input_doc = nlp(user_input)  # Process the user input using SpaCy

    # Initialize variables for the best matching FAQ
    best_match = None
    highest_similarity = 0

    # Iterate over the FAQs and compare each one to the user input
    for faq in faq_data:
        faq_doc = nlp(faq['question'])  # Process each FAQ question
        similarity = user_input_doc.similarity(faq_doc)  # Calculate the similarity

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = faq

    # Return the best match response or a fallback message
    if best_match:
        return best_match['answer']
    else:
        return "Sorry, I couldn't understand that. Can you ask in another way?"
