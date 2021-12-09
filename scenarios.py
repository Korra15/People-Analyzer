from flask import Blueprint, render_template, url_for
from flask_login import login_required, logout_user
from werkzeug.utils import redirect


scenarios = Blueprint('scenarios', __name__)

@scenarios.route('/scenario', methods=['GET', 'POST'])
@login_required
def scenario():
    return render_template('scenarios.html')


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
