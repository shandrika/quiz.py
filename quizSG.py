#Fix Looping Issue + Add Score

#Identify Variables
qA = int()
qA2 = int()
choice = False
choice2 = False
score = int(0)

q1t = ("""Which one of these colours are the primary colours?
1.Yellow
2.Green
3.Orange
4.Purple
Answer:  """)


q2t = ("""What colours make pink?
1.Red + Blue
2.Purple + Blue
3.Yellow + Red
4.Red + White
Answer:  """)

#While Loop
while choice == False:
    try:
        qA = int(input(q1t))
        
        if qA == 1:
            score += 1
            choice = True

        elif 0 < qA < 5:
            choice = True

        else:
            print("Please type a whole number between 1 and 4. ")

    except ValueError:
        print("Seriously? Please put a WHOLE POSITIVE INTEGER between 1 and 4. ")


while choice2 == False:
    try:
        qA2 = int(input(q2t))
        
        if qA2 == 4:
            score += 1
            choice2 = True

        elif 0 < qA2 < 5:
            choice2 = True

        else:
            print("Please type a whole number between 1 and 4. ")

    except ValueError:
        print("Seriously? Please put a WHOLE POSITIVE INTEGER between 1 and 4. ")

print("you have", score,"point(s).")   
