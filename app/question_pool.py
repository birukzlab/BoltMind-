import json
import random

def load_questions():
    with open('questions.json', 'r') as f:
        questions = json.load(f)
    return questions

def get_random_question():
    questions = load_questions()
    question_data = random.choice(questions)
    return question_data['question'], question_data['answer'], question_data['difficulty']
