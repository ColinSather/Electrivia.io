#!/usr/bin/env python3
"""
This script is only for testing new concepts/ideas
"""
import RPi.GPIO as GPIO
import time, random, base64, json, requests

api = "https://opentdb.com/api.php?amount=1&encode=base64"

def tazed():
    led1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()


def based(message):
    hm = {}
    incorrect_answers = []
    for x in message["results"]:
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


if __name__ == "__main__":
    res = requests.get(api)
    quiz = res.json()
    quiz = dict(quiz)
    #based(bytes(q[0]['question'], "utf-8"))
    based(quiz)
    """
    for q in quiz['results']:
        print(q['question'])
        based(q['question'])
        ans = q['correct_answer']
        choices = q['incorrect_answers']
        choices.append(ans)
        random.shuffle(choices)
        # mix around choices, answer can't always be last
        for c in choices:
            print(c)

        print("Enter the choice number to represent ur answer (0-3)")
        s = input()

        if choices[int(s)] == q['correct_answer']:
            print("Correct!")
        else:
            print("Wrong u dumbass...")
            tazed()
    """
