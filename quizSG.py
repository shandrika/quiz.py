#Import File Of Data
from quizDataSG import *

#Global Variable
grade = 0

#Custom function
def run_quest(quest,check,ansU,ansR):
    while check == False:
        try:
            ansU = int(input(quest))
            if ansU == ansR:
                global grade
                grade += 1
                check = True
            elif 0 < ansU < 5:
                check = True
            else:
                print("Please type a whole number between 1 and 4. ")
        except ValueError:
            print("Seriously? Please put a WHOLE POSITIVE INTEGER between 1 and 4")



#Run Program
run_quest(q1t, q1choice, q1a, q1c)
run_quest(q2t, q2choice, q2a, q2c)
run_quest(q3t, q3choice, q3a, q3c)
run_quest(q4t, q4choice, q4a, q4c)
run_quest(q5t, q5choice, q5a, q5c)
run_quest(q6t, q6choice, q6a, q6c)
run_quest(q7t, q7choice, q7a, q7c)
run_quest(q8t, q8choice, q8a, q8c)
run_quest(q9t, q9choice, q9a, q9c)
run_quest(q10t, q10choice, q10a, q10c)

#User's Score

if -1 < grade < 4:
    print ("Jesus... You got",grade * 10,"% right! Learn your colours!")

elif 3 < grade < 7:
    print(" Hmm.. Not Bad. Your got",grade * 10,"% right!")
            
elif 6 < grade < 11:
    print( "Congrats! You got",grade * 10,"% right! Smarty Pants!")
