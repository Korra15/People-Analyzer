from flask import Blueprint, render_template, request

quiz = Blueprint('quiz', __name__)

class Question:
    qid = -1
    question = ''
    option1 = ''
    option2 = ''
    option3 = ''
    option4 = ''
    option5 = ''

    def __init__(self, qid, question):
        self.qid = qid
        self.question = question
        self.option1 = "Strongly disagree"
        self.option2 = "Disagree"
        self.option3 = "Neither"
        self.option4 = "Agree"
        self.option5 = "Strongly agree"
 

    def get_option_value(self, optValue):
        if optValue == "Strongly disagree":
            return 1
        elif optValue == "Disagree":
            return 2
        elif optValue == "Neither":
            return 3
        elif optValue == "Agree":
            return 4
        elif optValue == "Strongly agree":
            return 5



import json

f = open('data.json')
j = json.load(f)
questions_list = []
for i in j['questions_list']:
    q = Question(**i)
    questions_list.append(q)
f.close()


@quiz.route("/quiz", methods=['POST', 'GET'])
def personalityTest():
    return render_template('quiz.html', questions_list = questions_list)


@quiz.route("/submitquiz", methods=['POST', 'GET'])
def submitTest():
    result = 0
    for question in questions_list:
        selected_option = request.form.get(str(question.qid), False)
        temp = question.get_option_value(selected_option)
        result += temp
    result = str(result)
    return render_template('submittest.html', result=result)




