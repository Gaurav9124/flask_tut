from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gaurav'}
    collection = [
    { "author": "Tuco Salamanca", "body": "Tight, tight, tight... Blue, Yellow, Pink—whatever man, just bring me that." },
    { "author": "Walter White", "body": "I am the danger. A guy opens his door and gets shot, and you think that of me? No. I am the one who knocks!" },
    { "author": "Jesse Pinkman", "body": "Yeah, science! Magnets, bitch!" },
    { "author": "Saul Goodman", "body": "You don’t want a criminal lawyer... you want a criminal lawyer." },
    { "author": "Gus Fring", "body": "I hide in plain sight, just like you." },
    { "author": "Hank Schrader", "body": "Jesus Christ, Marie! they are Minerals." },
    { "author": "Mike Ehrmantraut", "body": "No more half-measures." },
    { "author": "Lalo Salamanca", "body": "You’re guessing, am I right? But you don’t know." },
    { "author": "Skyler White", "body": "Someone has to protect this family from the man who protects this family." },
    { "author": "Todd Alquist", "body": "Yeah, sorry for your loss." }
]

    return render_template("index.html", user=user, title="TheOGBlog YO!", posts=collection)