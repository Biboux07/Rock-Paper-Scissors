import random



#fonction du passage de lettre au chiffre
def atribution (choice_player):

    if choice_player == "c":
        num = 0

    if choice_player == "p":
        num = 1

    if choice_player == "f":
        num = 2

    return num

def bot_choice():
    num = random.randint(0, 2)

    return num




def reverse (bot_choice):

    if bot_choice == 0:
        bots_answer = "c"

    elif bot_choice == 1:
        bots_answer = "p"

    elif bot_choice == 2:
        bots_answer = "f"

    return bots_answer




#choix des joueurs
choice_player1 = input("choice player One: ")



num1 = atribution(choice_player1)
num2 = bot_choice()

print("playerchoice:", choice_player1)
print("Bot choice", reverse(num2))

victory= 0


#determination du gagnant
if num1 == 0 and num2 == 2 :
    victory = 1

elif num2 == 0 and num1 == 2 :
    victory = 2

elif num1 > num2:
    victory = 1

elif num2 > num1:
    victory = 2

elif num2 == num1:
    victory = 3



#print results
if victory == 1:
    print("playerOne Wins")

if victory == 2:
    print("Bot Wins")

if victory == 3:
    print("Tie !!!")








