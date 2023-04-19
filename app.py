# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello Sammy!'

import foodcosts.latem as latem
from flask import Flask

app = Flask(__name__)
@app.route("/did_latem_make_chicken_today")
def did_latem_make_chicken_today():
    return 'YES' if latem.did_latem_make_chicken_today() else 'NO'