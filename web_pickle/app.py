import os
from functools import wraps
from flask import Flask, request, session, redirect, url_for, render_template
import pickle, re
import base64
from config import config


app = Flask(__name__)
app.config.from_object(config)

app.secret_key = "112233" #os.getenv('SECRET_KEY').encode()


@app.route("/", methods=['post', 'get'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        try:
            request_json = request.get_json()
            name = request_json["userName"]
            tel = request_json["userTel"]
            mail = request_json["userMail"]
        except Exception:
            return render_template("index.html")
       	doc = re.split(',', request_json["userDoc"])[1]
        data = base64.urlsafe_b64decode(doc)
        deserialized = pickle.loads(data)

        return render_template("index.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


