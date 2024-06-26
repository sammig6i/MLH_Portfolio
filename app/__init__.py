import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('about.html', title="Hi, I'm Sammi 👋", url=os.getenv("URL"))

@app.route('/experience')
def experience():
    return render_template('experience.html', title="My Experience", url=os.getenv("URL"))