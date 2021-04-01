import RPi.GPIO as GPIO
import time, random

quiz = {
    "response_code":0,
    "results":[
        {
            "category":"Entertainment: Film",
            "type":"multiple",
            "difficulty":"medium",
            "question":"In the movie &ldquo;The Iron Giant,&rdquo; this character is the protagonist.",
            "correct_answer":"Hogarth Hughes",
            "incorrect_answers":[
                "Kent Mansley",
                "Dean McCoppin",
                "Annie Hughes"
            ]
        }
    ]
}

def tazed():
    led1 = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    for q in quiz['results']:
        print(q['question'])
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
