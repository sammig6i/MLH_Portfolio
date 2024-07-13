from crypt import methods
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
host=os.getenv("MYSQL_HOST"),
port=3306)

class TimeLinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimeLinePost])


@app.route('/')
def index():
    class Education:
        def __init__(self, school, degree, logo):
            self.school = school
            self.degree = degree
            self.logo = logo
    education = [
        Education("Western Governor's Uni", "Computer Science", "../static/img/wgu.png"),
        Education("Boise State University", "Accounting, Minor in IT", "../static/img/bsu.jpeg")
    ]
    return render_template('about.html', title="Hi, I'm Sammi 👋", url=os.getenv("URL"), education=education)

@app.route('/experience')
def experience():
    class Experience:
        def __init__(self, dates, position, description):
            self.dates = dates
            self.position = position
            self.description = description

    experiences = [
        Experience("2024 - Now", "Meta PE Fellow @ MLH", "Collaborating with fellows and being mentored by Meta PEs."),
        Experience("2021 - 2023", "Accountant", "Worked 2 years in public accounting."),
        Experience("2019 - 2021", "Bookkeeper", "Worked as a bookkeeper for a local coffee shop in Boise, ID."),
    ]
    return render_template('experience.html', title="My Experience", url=os.getenv("URL"), experiences=experiences)


@app.route('/hobbies')
def hobbies():
    class Hobby:
        def __init__(self, title, description, image, link=None):
            self.title = title
            self.description = description
            self.image = image
            self.link = link

    hobbies = [
        Hobby("Basketball", "This is my first love. I have played all my life and won't stop!", "../static/img/basketball.jpg"),
        Hobby("Music", "I like to make beats.", "../static/img/music.jpg", "https://www.youtube.com/channel/UCInam7nBGvlM7qJSe45AMTw"),
        Hobby("Cooking", "My passion is eating, but I love to cook.", "../static/img/cooking.jpg"),
        Hobby("Hiking", "I love to be outside.", "../static/img/hiking.jpg")
    ]
    return render_template('hobbies.html', title="My Hobbies", url=os.getenv("URL"), hobbies=hobbies)


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimeLinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline posts': [
            model_to_dict(p)
            for p in
            TimeLinePost.select().order_by(TimeLinePost.created_at.desc())
        ]
    }



    