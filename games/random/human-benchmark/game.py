import random
import time

WORDS = ["python","resting","flying","beautiful","success","lucky","racing","accurate","typing"]
AUTHOR = "giandab"

def run():

    print("=== 🏋️  Human Benchmark 🏋️ ===")
    print(f"Welcome to this typing benchmark by {AUTHOR}!\n")
    print("You will be given a random word and will have to type it out as fast as you can. You will be scored on accuracy and speed")
    input("Press any button to start ...")

    word = WORDS[random.randint(0,6)]

    start_time = time.time()
    print("The word is: ",word)
    response = input("")
    end_time = time.time()

    correct = 0
    wrong = 0

    shortest = min([word,response],key=len)
    longest = max([word,response],key=len)

    wrong += len(longest) - len(shortest)

    for i in range(len(shortest)):

        if word[i] == response[i]:
            correct += 1
        else:
            wrong += 1 
    
    accuracy = round(((correct/(correct+wrong))*100),2)
    speed = round(end_time-start_time,2)

    if accuracy == 100.0:
        print("Your accuracy was: ",accuracy, ". That's a perfect accuracy! 🥇")
    elif accuracy>= 80.0:
        print("Your accuracy was: ",accuracy, ". That's close! 🥈")
    else:
        print("Your accuracy was: ",accuracy, ". Oops! 🥉")

    if speed > 3.0:
        print("Your speed was ",speed,". That's a little slow 🙁 ")
    elif speed > 2.0:
        print("Your speed was ",speed,". That's pretty good! 🙂 ")
    else:
        print("Your speed was ",speed,". Very impressive! 😍 ")

    print("Thank you for playing!")
