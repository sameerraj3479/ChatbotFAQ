import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("data/faqs.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

questions = [item["question"] for item in faq_data]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_response(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity.argmax()

    score = similarity[0][best_match_index]

    if score > 0.15:
        answer = faq_data[best_match_index]["answer"]
        confidence = round(score * 100, 2)

        return f"{answer}\n\nConfidence Score: {confidence}%"

    return """
Sorry, I couldn't find an exact answer.

Try asking about:
• AI
• Machine Learning
• Deep Learning
• Python
• OOP
• CPU
• RAM
• Database
"""