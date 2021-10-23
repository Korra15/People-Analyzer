from flask import Blueprint, render_template, request

quiz = Blueprint('quiz', __name__)


questions = [
    {
        "id": "1",
        "question": "Is talkative",
        "answers": ["a) Strongly disagree", "b) Disagree", "c) Neither", "d) Agree", "e)Strongly agree"],
        "values": [1 , 2, 3, 4, 5]
    },
    {
        "id": "2",
        "question": "Tends to find fault with others",
        "answers": ["a) Strongly disagree", "b) Disagree", "c) Neither", "d) Agree", "e)Strongly agree"],
        "values":[1 , 2, 3, 4, 5]
    },
    {
        "id": "3",
        "question": "How many counties are there in England?",
        "answers": ["a) Strongly disagree", "b) Disagree", "c) Neither", "d) Agree", "e)Strongly agree"],
        "values":[1 , 2, 3, 4, 5]
    }
]

@quiz.route("/quiz", methods=['POST', 'GET'])
def personalityTest():

    if request.method == 'GET':
        return render_template("quiz.html", data=questions)
    if request.method == 'POST':
        for question in questions:
            result=request.form
    return render_template('submittest.html', result=result)



