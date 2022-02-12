# Libaries:
import random
import sys

# Variables:
answer = str()      # String used for various things
x = int()           # Integer used for various things
money = int(100)    # How much cash you have...
Marilyn = str()

# Functions:
def colour():      # Colour bet
    global money
    answer = str(input("Red or Black chip?")).lower()
    
    bet = int(input("What is your bet?"))
    
    if bet > money:
        print("You don't have enough money")
        return
    
    x = random.randint(0, 1)    # Picks either 0 or 1 to see who wins
    
    if answer == "red" and x == 0 or answer == "black" and x == 1:
        print("🎉🎉 You win", bet, "money 🎉🎉")
        money = money + bet
    else:
        print("🤡🤡 You lose", bet, "money 🤡🤡")
        money = money - bet

def number():       # Number bet
    print("Number code coming soon")

def checkbankrupt():
    if money <= 0 :
        print("😨 🔫😡 Get out my casino punk.")
        sys.exit()

# Start of main code!: ----------------------------------------------------------

print("GAMBLING SIMULATOR")

while True:
    checkbankrupt()
    print("\n")
    print(" --------------------------------------- ")
    print("| Colour or number?", Marilyn, "You have", money, "money |")
    print(" -------------------------------------- ")
    print("\n")
    
    answer = input()
    if answer.lower() == "/c" or answer.lower() == "colour":
        colour()
    elif answer.lower() == "/n" or answer.lower() == "number":
        number()
    elif answer.lower() == "sheep":
        Marilyn = "🐑"
        print("Marilyn observes you. Marilyn will accompany you on your journey.")
    else:
        print("Pick /c or /n")