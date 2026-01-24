def main():
    difficulty = input("Difficult or Casual? ").strip().title()
    players = input("Multiplayer or Single-player? ").strip().title()

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommended("Poker")
        elif players == "Single-Player":
            recommended("Klondike")
        else:
            print("Enter a valid number of players")

    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommended("Hearts")
        elif players == "Single-Player":
            recommended("Clock")
        else:
            print("Enter a valid number of players")

    else:
        print("Enter a valid difficulty")


def recommended(game):
    print("You might like", game)


main()


def recomended(game):
    print("You might like", game)


main()
