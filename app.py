#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import RPi.GPIO as GPIO
import time, json, random, requests
from models.choice_interface import ChoiceInterface


app = Flask(__name__)
interface = ChoiceInterface()

# Tens unit activates for 2s
def tazer():
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
