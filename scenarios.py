from flask import Blueprint, render_template, url_for
from flask_login import login_required, logout_user
from werkzeug.utils import redirect


scenarios = Blueprint('scenarios', __name__)

@scenarios.route('/scenario', methods=['GET', 'POST'])
@login_required
def scenario():
    return render_template('scenarios.html')

#Conscientiousness
@scenarios.route('/Conscientiousness', methods=['GET', 'POST'])
@login_required
def consi():
    return render_template('consciMain.html')


@scenarios.route('/Conscientiousness1O1', methods=['GET', 'POST'])
@login_required
def consi1():
    return render_template('consi1.html')


@scenarios.route('/Conscientiousness1O2', methods=['GET', 'POST'])
@login_required
def consi2():
    return render_template('consi2.html')


#Openness
@scenarios.route('/Openness', methods=['GET', 'POST'])
@login_required
def open():
    return render_template('openMain.html')


@scenarios.route('/Openness101', methods=['GET', 'POST'])
@login_required
def open1():
    return render_template('open1.html')


@scenarios.route('/Openness102', methods=['GET', 'POST'])
@login_required
def open2():
    return render_template('open2.html')


#Extraversion
@scenarios.route('/Extraversion', methods=['GET', 'POST'])
@login_required
def extra():
    return render_template('extraMain.html')


@scenarios.route('/Extraversion101', methods=['GET', 'POST'])
@login_required
def extra1():
    return render_template('extra1.html')


@scenarios.route('/Extraversion102', methods=['GET', 'POST'])
@login_required
def extra2():
    return render_template('extra2.html')

#Agreeableness
@scenarios.route('/Agreeableness', methods=['GET', 'POST'])
@login_required
def agree():
    return render_template('agreeMain.html')



