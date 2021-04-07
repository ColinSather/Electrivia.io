#!/usr/bin/env python3
<<<<<<< HEAD

from flask import Flask, render_template, request, redirect
import RPi.GPIO as GPIO
import time, json, random, requests
from models.choice_interface import ChoiceInterface


app = Flask(__name__)
interface = ChoiceInterface()

# Tens unit activates for 2s
def tazer():
=======
from flask import Flask
import RPi.GPIO as GPIO
import time, json, random

app = Flask(__name__)

# Tens unit activates for 2s
def tazed():
>>>>>>> d9efcf62fb4aac2b349d398a0d6c2688c61fdaca
    led1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()

<<<<<<< HEAD

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/check-answer", methods=['POST'])
def check_answer():
    user_inp = str(request.values["choice"])
    data = interface.getPossibilities()
    
    if data[0]["correct_answer"] != user_inp:
        print("USER'S ANSWER:", user_inp)
        print("CORRECT ANSWER:", data[0]["correct_answer"])
        tazer()
    else:
        print("USER'S ANSWER:", user_inp)
        print("CORRECT ANSWER:", data[0]["correct_answer"])

    return redirect("/rq")


@app.route("/rq")
def show_question():
    # returns a webpage of a random trivia question
    api = "https://opentdb.com/api.php?amount=1"
    res = requests.get(api)
    params = res.json()["results"][0]
    params = [dict(params)]
    interface.setPossibilities(params)
    return render_template("trivia.html", params=params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
@app.route("/")
def index():
    intro = "<h1>Welcome to Orwellian Trivia</h1>"
    intro += "<h2>Available quizes</h2>"
    with open("data/quizes.json", "r") as f:
        data = json.load(f)
        for quiz in data:
            qdata = data[quiz]
            title = qdata[0]
            title = title["category"] + " " + title["difficulty"]
            option = "<a href='/{}'>{}</a>".format(quiz, title)
            intro += option
            intro += "<br>"
    return intro


@app.route("/<string:quiz>")
def get_quiz(quiz):
    qdata = "<h1>{}</h1>".format(quiz)
    qdata += "<a href='/'>Return to the homepage</a>"
    with open("data/quizes.json", "r") as f:
        data = json.load(f)
        count = 1
        for d in data[quiz]:
            qdata += "<p><b>{}. </b>{}</p>".format(str(count), d["question"])
            choices = d["incorrect_answers"]
            choices.append(d["correct_answer"])
            random.shuffle(choices)

            qdata += "<form>"
            for choice in choices:
                qdata += "<label><input type='radio' value='{}' name='choice'/>".format(choice)
                qdata += "{}</label>".format(choice)
                qdata += "<br>"
            
            qdata += "<br>"
            qdata += "<button type='submit' value='{}'>Submit Answer</button>".format(str(count))
            qdata += "</form>"
            count += 1
    return qdata

# TODO: Display quiz question one by one

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

>>>>>>> d9efcf62fb4aac2b349d398a0d6c2688c61fdaca
