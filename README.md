# Smart FAQ Assistant

## Project Overview

Smart FAQ Assistant is a web-based chatbot developed to answer frequently asked questions related to Artificial Intelligence, Machine Learning, Python Programming, and Computer Science fundamentals.

The system uses Natural Language Processing techniques to understand user queries and identify the most relevant answer from a predefined knowledge base. Instead of relying on exact keyword matching, the chatbot compares the user's question with stored FAQ entries and returns the closest matching response.

The project was developed as part of the CodeAlpha Artificial Intelligence Internship program and demonstrates the practical use of NLP, text vectorization, similarity matching, and interactive web application development.

---

## Problem Statement

Users often need quick answers to common technical questions. Searching through documentation or multiple web pages can be time-consuming. This project provides a simple interface where users can ask questions and receive instant responses from a curated FAQ database.

---

## Objectives

* Build an intelligent FAQ-based chatbot.
* Apply Natural Language Processing techniques.
* Implement similarity-based question matching.
* Create a user-friendly web interface.
* Provide instant responses from a structured knowledge base.

---

## Features

* Interactive web interface built with Streamlit.
* FAQ-based question answering system.
* Supports topics related to AI, Machine Learning, Python, and Computer Science.
* Uses TF-IDF vectorization for text representation.
* Uses Cosine Similarity to identify the best matching question.
* Maintains chat history during the session.
* Displays confidence score for matched responses.
* Clear Chat functionality.

---

## Technologies Used

```text
Programming Language
--------------------
Python

Frontend Interface
------------------
Streamlit

Machine Learning Library
------------------------
Scikit-Learn

NLP Technique
-------------
TF-IDF Vectorization

Similarity Algorithm
--------------------
Cosine Similarity

Data Storage
------------
JSON
```

---

## Project Structure

```text
CodeAlpha_ChatbotFAQ
│
├── app.py
├── chatbot.py
├── README.md
├── requirements.txt
│
├── data
│   └── faqs.json
│
└── screenshots
```

---

## Working Process

### Step 1: User Input

The user enters a question through the Streamlit interface.

### Step 2: Text Processing

The entered question is converted into a numerical representation using TF-IDF Vectorization.

### Step 3: Similarity Calculation

Cosine Similarity is used to compare the user's question with all questions stored in the FAQ database.

### Step 4: Best Match Selection

The system identifies the FAQ with the highest similarity score.

### Step 5: Response Generation

If the similarity score is above the predefined threshold, the corresponding answer is displayed. Otherwise, the chatbot informs the user that no suitable answer was found.

---

## Knowledge Domains Covered

```text
Artificial Intelligence
Machine Learning
Deep Learning
Natural Language Processing
Python Programming
Object-Oriented Programming
Data Science
Computer Fundamentals
Database Concepts
Cyber Security Basics
```

---

## Installation

### Clone the Repository

```bash
git clone <repository_link>
cd CodeAlpha_ChatbotFAQ
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Sample Questions

```text
What is AI?
What is Machine Learning?
What is Deep Learning?
What is Python?
What is OOP?
What is CPU?
What is RAM?
What is SQL?
What is Cyber Security?
```

---

## Future Improvements

* Voice-based question input.
* Multi-language support.
* Larger FAQ knowledge base.
* Database integration.
* Advanced NLP preprocessing.
* User authentication and personalization.

---

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning techniques can be used to build an efficient FAQ assistant. By combining TF-IDF Vectorization, Cosine Similarity, and an interactive Streamlit interface, the system provides quick and accurate responses to user queries while maintaining a simple and user-friendly experience.
