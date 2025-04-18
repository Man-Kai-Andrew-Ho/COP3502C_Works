import p1_random as p1
rng = p1.P1Random()

menu = "1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit"
games = 1
wins = 0
losses = 0
ties = 0

def check():
    card = rng.next_int(13) + 1
    if card == 1:
        print("Your card is a ACE!")
        return 1
    elif card == 11:
        print("Your card is a JACK!")
        return 10
    elif card == 12:
        print("Your card is a QUEEN!")
        return 10
    elif card == 13:
        print("Your card is a KING!")
        return 10
    else:
        print(f"Your card is a {card}!")
        return card

def win():
    global wins
    global losses
    global ties
    if player_hand == dealer_cards:
        print("It's a tie! No one wins!\n")
        ties += 1
    elif dealer_cards > 21 or player_hand > dealer_cards:
        print("You win!\n")
        wins += 1
    elif player_hand < dealer_cards:
        print("Dealer wins!\n")
        losses += 1

while True:
    print(f"START GAME #{games}\n")

    player_hand = check()
    print(f"Your hand is: {player_hand}\n")

    while True:
        print(menu)
        print("")
        option = int(input("Choose an option:"))

        if option == 1:
            print("")
            player_hand += check()
            print(f"Your hand is: {player_hand}\n")

            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                games += 1
                wins += 1
                break
            elif player_hand > 21:
                print("You exceeded 21! You lose.\n")
                games += 1
                losses += 1
                break
        elif option == 2:
            print("")
            dealer_cards = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_cards}")
            print(f"Your hand is: {player_hand}\n")
            win()
            games += 1
            break
        elif option == 3:
            games -= 1
            print("")
            print(f"Number of Player wins: {wins}")
            print(f"Number of Dealer wins: {losses}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {games}")
            percent = wins / games * 100
            print(f"Percentage of Player wins: {percent:.1f}%\n")
        elif option == 4:
            print("")
            exit()
        else:
            print("")
            print(f"Invalid input!")
            print(f"Please enter an integer value between 1 and 4.\n")
            games -= 1
            continue
