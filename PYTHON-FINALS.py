import math

print("\tWelcome to the Probability Calculator \n\t\tfor Dice, Coin, and Cards!")
print("")

print("Choose an option")
print("0. Exit program")
print("1. Dice probability")
print("2. Coin probability")
print("3. Cards probability")
print("")

choice = 1

while choice != 0:
    choice = int(input("Please enter your choice: "))
    print("")

    if choice == 0:
        print("Thanks for using the Probability Calculator for Dice, Coin and Cards!")
        break

    elif choice == 1:
        print("\tDice Probability")
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on the die: "))
        desired_outcome= int(input("Enter the desired outcomes: "))
        probability = round(desired_outcome/(num_sides)**num_dice, 2)

        print("The probability of rolling a", desired_outcome, "on a", num_sides, "sided die is", probability)
        print("")
        break

    elif choice == 2:
        print("\tCoin Probability")
        num_toss = int(input("Enter the number of coin toss: "))
        desired_outcomes = input('Enter the desired outcomes (heads/tails): ')
        probability = round(0.5 ** num_toss, 2)

        print("The probability of getting", desired_outcomes, "on", num_toss, "coin toss is", probability)
        print("")
        break

    elif choice == 3:
          print("\tCards Probability")
          num_cards = 52
          desired_card = int(input("Enter the desired card (1-13): "))
          face_card = ""
          
          if desired_card == 1:
                face_card = "Ace"
          elif desired_card == 11:
                face_card = "Jack"
          elif desired_card == 12:
                face_card = "Queen"
          elif desired_card == 13:
                face_card = "King"
          else:
                 face_card = str(desired_card)
          
          desired_suit = input("Enter the desired suit (e.g spade): ")
          suits = 13

          if desired_suit == "spade":
                suits = 13
          elif desired_suit == "diamond":
                suits = 13
          elif desired_suit == "heart":
                suits = 13
          elif desired_suit == "club":
                suits = 13
          else:
                print("Please try again")
          
          probability = round((1/suits) * (desired_card/num_cards), 2)
          
          print("The probability of drawing a", face_card, "of", desired_suit, "from a deck of", num_cards, "cards is", probability)
          print("")
          break


    else:
        print("Invalid input. Please try again.")