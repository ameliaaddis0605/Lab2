"""
Match Coin Game 
Amelia Addis
This program is an interactive coin toss game.
09-29-2026
"""
from player import Player 

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    choice = ""
    print("--- Coin Match Game ---")
    print("Player 1 has",player1.get_wallet())
    print("Player 2 has",player2.get_wallet())
    choice = input("Do you want to toss the coins? (y/n): ")
    

    while choice == "y" or choice == "Y":
        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        print("Tossing...")
        print("Player 1 has",side1)
        print("Player 2 has", side2)


        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin")
            
            print("Player 1 has",player1.get_wallet())
            print("Player 2 had",player2.get_wallet())
            choice = input("Do you want to toss the coins? (y/n: ")
        

 print("--- Final Score ---")
 print("Player 1:",player1.get_wallet())
 print("Player 2:",player2.get_wallet())

 if player1.get_wallet() > player2.get_wallet():
            print("Player 1 has more coins!")
        elif player1.get_wallet() < player2.get_wallet():
            print("Player 2 has more coins!")
        else player1.get_wallet() == player2.get_wallet():
            print("It's a draw!")
        
                  




