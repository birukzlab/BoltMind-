from flask import render_template, request
from app import app
from app.question_pool import get_random_question

@app.route('/')
def index():
    # Get a random question and its answer
    question, correct_answer, difficulty = get_random_question()
    return render_template('index.html', question=question, correct_answer=correct_answer, difficulty=difficulty)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form['answer'].strip().lower()
    correct_answers = request.form.getlist('correct_answer[]')

    # Normalize and compare answers
    correct_answers = [ans.strip().lower() for ans in correct_answers]
    
    # Check if the user's answer is in the list of correct answers
    if user_answer in correct_answers:
        feedback = "Correct!"
    else:
        feedback = f"Incorrect. The correct answers are {', '.join(correct_answers)}."

    # Get a new random question
    question, correct_answer, difficulty = get_random_question()
    return render_template('index.html', question=question, feedback=feedback, correct_answer=correct_answer, difficulty=difficulty)




