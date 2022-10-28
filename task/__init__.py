from flask import Flask
from dotenv import load_dotenv
import os

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