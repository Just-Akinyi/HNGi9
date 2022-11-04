from flask import Flask, request
from dotenv import load_dotenv
import os
from enum import Enum
import json


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
load_dotenv()

@app.route('/')
def index():
    about_me={
        'slackUsername': os.getenv('SLACK_USERNAME'),
        'backend': bool(os.getenv('BACKEND')),
        'age': int(os.getenv('AGE')),
        'bio': os.getenv('BIO')
    }

    return about_me
    
@app.route('/json-example', methods=['GET','POST'])
def calculation():
    if request.method == 'POST':
        # new_data = request.get_json(force=False,silent=False,cache=True)
        value_x = request.json['x']
        value_y = request.json['y']
        operator = request.json['operation_type']
        class calc(Enum):
            ADD = 'add'
            SUB = 'subtract'
            MULT = 'multiply'
        operations = [item.value for item in calc]
        myjson={
                    'slackUsername': os.getenv('SLACK_USERNAME'),
                    'operation_type': operator,
                    'result': result
                    }
        if operator in operations:
            if operator == 'add':
                result = value_x + value_y
                return myjson
            if operator == 'subtract':
                result = value_x - value_y
                return myjson
            if operator == 'multiply':
                result = value_x * value_y
                return myjson
    return 'myjson'