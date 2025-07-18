import json
import requests
import pprint as p
import html
import random

def quiz():
    correct = 0
    while(True):
        r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")      #API request
        if (r.status_code != 200):
            break
        question = json.loads(r.text)                                                               #Converting .json into dictionary
        
        print("The question is :",html.unescape(question["results"][0]["question"])) 

        options = [html.unescape(opt) for opt in question["results"][0]["incorrect_answers"]]
        correct_answer =  html.unescape(question["results"][0]["correct_answer"])
        options.append(correct_answer)

        random.shuffle(options)                                                                     #To shuffle the options             
        
        ans = input(f'''    1. {options[0]}
    2. {options[1]}
    3. {options[2]}
    4. {options[3]} 
        ''')
        if ans in ['1', '2', '3', '4']:
            user_answer = options[int(ans)-1]
        else:
            user_answer = 0
        if user_answer == correct_answer:
            print("Correct answer...")
            correct+=1
        else:
            print("Wrong answer...")

        choice = input("Next question? (y/n) ")               #For quitting

        if choice.lower() == 'n':
            break

    print("Your correct answers :", correct)

quiz()

