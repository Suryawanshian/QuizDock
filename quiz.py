#!/usr/bin/python
from pathlib import Path
import json
with open(Path('quiz.json'),'r') as f:
   config =json.load(f)
#config = json.loads(open(Path('G:\\Softwares\\Docker\\quiz\\quiz.json')).read())
print(config)
sportcorrect=0
sportincorrect=0
mathscorrect=0
mathsincorrect=0
print("Welcome to Quiz !!!")
print("1. Sports \n2. Maths")

group=input("Choose your Group 1 or 2 ?")

"""def clear():
    if name == 'nt' :
        _ = system('cls')
clear()"""

if (group == "1"):
    print("You Chose Sports")
    print(config['quiz']['sport']['q1']['question'])
    print("1."+config['quiz']['sport']['q1']['options'][0])
    print("2."+config['quiz']['sport']['q1']['options'][1])
    print("3."+config['quiz']['sport']['q1']['options'][2])
    print("4."+config['quiz']['sport']['q1']['options'][3])
    choice = int(input("Please Choose your option:"))
    if choice == 4 :
        print("Your Choice is " + str(choice))
        print("Correct Answer")
        sportcorrect+=1
    else:
        print("Your choice is " + str(choice))
        print("Incorrect Answer")
        sportincorrect+=1

    #print(config['quiz']['sport']['q1']['answer'])
    print("Number of correct answers " ,sportcorrect)
    print("number of incorrect answers " ,sportincorrect)


else:
    print("You chose Maths")
    print("1. "+ config['quiz']['maths']['q1']['question'])
    print("1. "+ config['quiz']['maths']['q1']['options'][0])
    print("2. "+ config['quiz']['maths']['q1']['options'][1])
    print("3. "+ config['quiz']['maths']['q1']['options'][2])
    print("4. "+ config['quiz']['maths']['q1']['options'][3])
    choice = int(input("Please Choose your option:"))

    if choice == 3:
     #def incr():
      #  global count
       # count + 1
        #print("correct answer :" + str(count))
        #print()
        print("Your choice is " + str(choice))
        print("Correct answer")
        mathscorrect+=1
       # print(count)
    else:

        print("Your choice is " + str(choice))
        print("Incorrect answer")
        mathsincorrect+=1
    print("2. " + config['quiz']['maths']['q2']['question'])
    print("1. " + config['quiz']['maths']['q2']['options'][0])
    print("2. " + config['quiz']['maths']['q2']['options'][1])
    print("3. " + config['quiz']['maths']['q2']['options'][2])
    print("4. " + config['quiz']['maths']['q2']['options'][3])
    opt = int(input("Please Choose your option:"))
    if opt == 4:
     #   count + 1
        print("Your choice is " + str(opt))
        print("Correct Answer")
        mathscorrect+=1
    else:
      #  cnt + 1
        print("Your choice is " + str(opt))
        print("Incorrect Answer")
        mathsincorrect+=1

#print("correct answer :"+str(count))
#print()

#print("incorrect answer : "+str(cnt))
#print()

    print("Number of correct answers " , mathscorrect)
    print("Number of incorrect answers " ,mathsincorrect)


#Sports = input("Sports")
#Maths = input("Maths") '''




