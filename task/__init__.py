from flask import Flask, request
from dotenv import load_dotenv
import os
from enum import Enum
import json
from .data import json_example

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
    if request.methods == 'POST':
        new_data = input()
        dictionary = json.loads(new_data)
        value_x=dictionary['x']
        value_y = dictionary['y']
        operator=dictionary['operation_type']
        class calc(Enum):
            ADD = 'add'
            SUB = 'subtract'
            MULT = 'multiply'
        operations = [item.value for item in calc]
        try:
            if operator in operations:
                if operator == 'add':
                    result = value_x + value_y
                if operator == 'subtract':
                    result = value_x - value_y
                if operator == 'multiply':
                    result = value_x * value_y
            print(result)
        except:
            print('Use add, subract or multiply for operation type')
        myjson={
                'slackUsername': os.getenv('SLACK_USERNAME'),
                'operation_type': operator,
                'result': result
            }
        return(myjson)