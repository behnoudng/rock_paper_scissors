import os
def rock_paper_scissors():
    score1, score2 = 0, 0
    exit = False
    while exit == False :
        gamer1 = input("Enter your choice: ")
        # os.system("clear")

        if (gamer1 == "exit"):
            print("gamer1 score : ", score1 )
            print("gamer2 score : ", score2 )
            exit = True
        gamer2 = input("It's your turn: ")



        r, p, s = "rock", "paper", "scissors"
        if gamer1 == r and gamer2 == p :
            print("gamer2 is the winner")
            score2 += 1
        elif gamer1 == r and gamer2 == s :
            print("gamer1 is the winner")
            score1 += 1
        elif gamer1 == p and gamer2 == r :
            print("gamer1 is the winner")
            score1 += 1
        elif gamer1 == p and gamer2 == s :
            print("gamer2 is the winner")
            score2 += 1
        elif gamer1 == s and gamer2 == r :
            print("gamer2 is the winner")
            score2 += 1
        elif gamer1 == s and gamer2 == p :
            print("gamer1 is the winner")
            score1 += 1
        elif gamer1 == gamer2 :
            print("draw")



rock_paper_scissors()




