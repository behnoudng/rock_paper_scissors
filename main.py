import os
gamer1 = input("Enter your choice: ")
os.system("clear")
gamer2 = input("It's your turn: ")
r, p, s = "rock", "paper", "scissors"
if gamer1 == r and gamer2 == p :
    print("gamer2 is the winner")
elif gamer1 == r and gamer2 == s :
    print("gamer1 is the winner")
elif gamer1 == p and gamer2 == r :
    print("gamer1 is the winner")
elif gamer1 == p and gamer2 == s :
    print("gamer2 is the winner")
elif gamer1 == s and gamer2 == r :
    print("gamer2 is the winner")
elif gamer1 == s and gamer2 == p :
    print("gamer1 is the winner")
elif gamer1 == gamer2 :
    print("draw")


