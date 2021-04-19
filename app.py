#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
import RPi.GPIO as GPIO
import time, json, random, requests, base64
from models.choice_interface import ChoiceInterface

app = Flask(__name__)
interface = ChoiceInterface()


def taze():
    """ Opens relay for 2 secs"""
    led1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()


def convert_base64_hm(paramd):
    """
    Converts a base64 JSON hash map into a plain text JSON hash map
    paramd [type: hashmap]: base64 data with plain text keys
    """
    hm = {}
    incorrect_answers = []
    for x in paramd["results"]:
        for k in x.keys():
            if k != "incorrect_answers":
                b = bytes(x[k], "utf-8")
                b = base64.b64decode(b)
                hm[k] = b.decode()
            
            elif k == "incorrect_answers":
                for choice in x[k]:
                    b = bytes(choice, "utf-8")
                    b = base64.b64decode(b)
                    incorrect_answers.append(b.decode())
                hm[k] = incorrect_answers
    return hm


@app.route("/check-answer", methods=['POST'])
def check_answer():
    """
    Sends result of the question attempt to the results view.
    """
    user_inp = str(request.values["choice"])
    data = interface.getPossibilities()
    ans = []
    ans.append(data["question"])
    ans.append(data["correct_answer"])
    ans.append(user_inp)

    # show the player their results and taze if incorrect
    if data["correct_answer"] != user_inp:
        taze()
        return render_template("result.html", ans=ans)
    else:
        return render_template("result.html", ans=ans)


@app.route("/rq")
def random_question():
    """
    returns a webpage of a random trivia question from opentdb
    """
    # ENHANCEMENT: use web sockets to enable each end user to view the same question
    api = "https://opentdb.com/api.php?amount=1&encode=base64"
    req = requests.get(api)
    raw_data = req.json()
    raw_data = dict(raw_data)
    params = convert_base64_hm(raw_data)
    interface.setPossibilities(params)
    return render_template("trivia.html", params=params)


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
