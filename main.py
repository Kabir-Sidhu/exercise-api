from flask import Flask, jsonify
from exercises import getExercise, searchExercises

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return "Welcome to the exercise API! API made by Kabir Sidhu."

@app.route('/<name>')
def details(name):
    if name == "favicon.ico":
        return

    return jsonify(getExercise(name))

@app.route('/search/<query>')
def search(query):
    return jsonify(searchExercises(query))

app.run()