#Custom Function Added, Score Commented Out

#Custom fucntion
def run_quest(quest,check,ansU,ansR):
    print(quest)
    while check == False:
        try:
            ansU = int(input(quest))
            if ansU == ansR:
                #score += 1
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

q2a = int()
q2choice = False
q2t = ("""What colours make pink?
1.Red + Blue
2.Purple + Blue
3.Yellow + Red
4.Red + White
Answer:  """)

