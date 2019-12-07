#!/usr/bin/python

import json

#Loading json file data
config =json.loads(open('quiz.json').read())


groups = list(config['quiz'].keys())
print("Welcome to Quiz !!!")
# Display quiz of group names

for i in range(len(groups)):
    print(str(i+1) + '. ' + str(groups[i]))
group = int(input("Choose your Group:"))


if group in range(1, len(groups)+1):
    selected_group = groups[group-1]
    num_correct, num_wrong = (0,0)

    for question_id, question_info in config['quiz'][selected_group].items():
        print(question_id)
        print(question_info['question'])
        for l in range(0, 4):
            print(str(l + 1), end=" ")
            print(question_info['options'][l])

        choice = int(input("Please Choose your option:"))
        if question_info['options'][choice-1] == question_info['answer']:
            num_correct += 1
            print("Correct Answer")
        else:
            num_wrong += 1
            print("Incorrect Answer")
            print("Correct answer is: ", question_info['answer'])

    # Printing the result
    print("Number of correct answers ", num_correct)
    print("Number of incorrect answers ", num_wrong)
else:
    print("Please choose valid option")
