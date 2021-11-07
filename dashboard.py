from flask import Blueprint, render_template, url_for
from flask_login import login_required, logout_user
from werkzeug.utils import redirect


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET', 'POST'])
@login_required
def mainPage():
    return render_template('dashboard.html')

@dashboard.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
    
    
@dashboard.route('/about')
@login_required
def about():
    return render_template('about.html')

