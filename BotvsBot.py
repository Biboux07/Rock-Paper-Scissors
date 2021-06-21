import random


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


#determination du gagnant

def Whowins(num1, num2):

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

    return victory

Bot1wins= 0
Bot2wins= 0
BotTie= 0
i= 0
numpart =  10000000 

while True:

    num1 = bot_choice()
    num2 = bot_choice()

    victory = Whowins(num1, num2)

    if victory == 1:
        Bot1wins = Bot1wins + 1

    elif victory == 2:
        Bot2wins = Bot2wins + 1

    elif victory == 3:
        BotTie = BotTie +1

    if i == numpart:
        break

    i = i + 1


pourcentb1 = (Bot1wins/numpart)*100
pourcentb2 = (Bot2wins/numpart)*100
pourcentie = (BotTie/numpart)*100




print("BotOne Wins =", round(pourcentb1, 2), "%")
print("BotTwo Wins=", round(pourcentb2, 2) , "%")
print("Tie = ", round(pourcentie, 2), "%")








