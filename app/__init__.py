import logging
import os
import requests
import hashlib
from flask import Flask, jsonify, redirect, render_template, request, url_for
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
host=os.getenv("MYSQL_HOST"),
port=int(os.getenv("MYSQL_PORT", 3306)))


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

try:
    mydb.connect()
    logger.info("Successfully connected to database.")
    mydb.create_tables([TimelinePost])
    logger.info("Tables created successfully")
except Exception as e:
    logger.error("Error connecting to the database: s%", e)
    raise e


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
    return render_template('about.html', title="H, I'm Sammi 👋", url=os.getenv("URL"), education=education)

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




@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
    try:
        timeline_post = TimelinePost.get_by_id(id)
        timeline_post.delete_instance()
        return jsonify({"success": "Post deleted successfully"})
    except TimelinePost.DoesNotExist:
        return jsonify({"error": "Post not found", "id": id}), 404


GRAVATAR_BASE_URL = "https://www.gravatar.com/avatar/"
GRAVATAR_API_KEY = os.getenv('GRAVATAR_API_KEY')


def get_gravatar_profile(email, default_avatar_url):
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    gravatar_url = f"{GRAVATAR_BASE_URL}{email_hash}?d=404" 

    response = requests.get(gravatar_url)
    if response.status_code == 200:
        return gravatar_url
    else:
        return default_avatar_url
    
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline', methods=['GET', 'POST'])
def timeline():
    default_avatar_url = url_for('static', filename='img/default-profile.jpg', _external=True)
    user_avatar = None
    if request.method == 'POST':
        response = requests.post(
            url_for('post_time_line_post', _external=True),
            data={
                'name': request.form['name'],
                'email': request.form['email'],
                'content': request.form['content']
            }
        )
        if response.status_code == 200:
            return redirect(url_for('timeline'))
        user_avatar = get_gravatar_profile(request.form['email'], default_avatar_url)
        
    response = requests.get(url_for('get_time_line_post', _external=True))
    posts = response.json().get('timeline_posts', [])

    for post in posts:
        post['avatar_url'] = get_gravatar_profile(post['email'], default_avatar_url)

    return render_template('timeline.html', title="Timeline", posts=posts, user_avatar=user_avatar)

    


    