from flask import Blueprint, render_template, request

quiz = Blueprint('quiz', __name__)


class Question:
    q_id = -1
    question = ""
    option1 = 1
    option2 = 2
    option3 = 3
    option4 = 4
    option5 = 5

    def __init__(self, q_id, question, option1, option2, option3, option4, option5):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5

q1 = Question(1,"Is talkative", 1, 2, 3, 4, 5)
q2 = Question(2,"Tends to find fault with others ", 1, 2, 3, 4, 5)

questions_list = [q1, q2]

@quiz.route("/test")
def test():
    return render_template("quiz.html", questions_list= questions_list)

@quiz.route("/submittest", methods=['POST', 'GET'])
def submit():
    for question in questions_list:
        selected_option = request.form[q_id]
        
    return value

