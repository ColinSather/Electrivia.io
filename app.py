#!/usr/bin/env python3
from flask import Flask
import RPi.GPIO as GPIO
import time, json, random

app = Flask(__name__)

# Tens unit activates for 2s
def tazed():
    led1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()

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

