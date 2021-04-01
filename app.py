#!/usr/bin/env python3

from flask import Flask, render_template
import RPi.GPIO as GPIO
import time, json, random, requests


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
    return render_template("home.html")


@app.route("/check-answer")
def check_answer():
    pass


@app.route("/rq")
def show_question():
    # allow this api call to be shared
    api = "https://opentdb.com/api.php?amount=1"
    res = requests.get(api)
    params = res.json()["results"][0]
    params = [dict(params)]
    return render_template("trivia.html", params=params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
