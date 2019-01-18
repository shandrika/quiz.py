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


#Identify Variables
q1a = int()
q1choice = False
q1t = ("""Which one of these colours are the primary colours?
1.Yellow
2.Green
3.Orange
4.Purple
Answer:  """)
q1c = 1

q2a = int()
q2choice = False
q2t = ("""What colours make pink?
1.Red + Blue
2.Purple + Blue
3.Yellow + Red
4.Red + White
Answer:  """)
q2c = 4

q3a = int()
q3choice = False
q3t = ("""What colours make the American Flag?
1.Red + Black + White
2.Purple + Blue + Green
3.Yellow + Red + Green
4.Red + White + Blue
Answer:  """)
q3c = 4

q4a = int()
q4choice = False
q4t = ("""What colour is blood before oxidation?
1.Red 
2.Blue
3.Purple
4.Green
Answer:  """)
q4c = 1

q5a = int()
q5choice = False
q5t = ("""There's a red house to the left and a blue house to the right. Where's the White House?
1.In The Middle
2.Behind Them
3.D.C.
4.That Makes No Sense
Answer:  """)
q5c = 3

q6a = int()
q6choice = False
q6t = ("""What colour is not originally on the rainbow?
1.Red 
2.Blue
3.Pink
4.Green
Answer:  """)
q6c = 3

q7a = int()
q7choice = False
q7t = ("""You're driving a bus. There are 12 cows with 7 legs, 3 mice with blue eyes, green dogs with one ear, and a cat.
What colour is the bus driver's eyes? 
1.Blue
2.Green
3.Hazel
4.Your eye colour
Answer:  """)
q7c = 4

q8a = int()
q8choice = False
q8t = ("""What colour is on the UA Maker Logo?
1.Wait, we have a logo?
2.Purple 
3.Red
4.Brown
Answer:  """)
q8c = 2

q9a = int()
q9choice = False
q9t = ("""What colour is Shandrika's favorite?
1.Blue
2.Purple
3.Yellow
4.ALL OF THE ABOVE
Answer:  """)
q9c = 3

q10a = int()
q10choice = False
q10t = ("""How many colours does it take to make a blind man confused?
1.Just One
2.All of them
3.None, He can't see
4.This makes no sense
Answer:  """)
q10c = 3






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
