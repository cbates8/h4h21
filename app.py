import os
import urllib.parse
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()
KEY = os.getenv('SECRET_KEY')
PARAMS = os.getenv('CONNECTION_PARAMS')

#configure Database URI:
params = urllib.parse.quote_plus(PARAMS)
conn_str = f'mssql+pyodbc:///?odbc_connect={params}'
engine_azure = create_engine(conn_str, echo=True)


#initialization
app = Flask(__name__, static_folder = 'templates/static', static_url_path = '')
app.config['SECRET_KEY'] = KEY
#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

id_var = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        global id_var
        email = request.form["email"]
        u = users(id_var, email)
        id_var += 1
        print(f'User {u.usr_email} added to database')
        return render_template("index.html")
    return render_template("user.html")

if __name__ == "__main__":
    #db.drop_all()
    db.create_all()
    app.run()
