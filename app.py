from flask import Flask
import auth 
import main  
import quiz 



#from flask_sqlalchemy import SQLAlchemy 
#from flask_login import LoginManager 

#db = SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #db.init_app(app)
    

    app.register_blueprint(auth.auth)

    app.register_blueprint(main.main)

    app.register_blueprint(quiz.quiz)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)