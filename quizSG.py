#Fix Looping Issue + Add Score

#Identify Variables
qA = int()
choice = False
score = int(0)

q1t = ("""Which one of these colours are the primary colours?
1.Yellow
2.Green
3.Orange
4.Purple
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
            print("Please type a positive number between 1 and 4. ")

    except ValueError:
        print("Seriously? Please put a WHOLE POSITIVE INTEGER between 1 and 4. ")

print("you have", score,"point(s).")   
