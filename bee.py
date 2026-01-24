WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to Spelling Bee")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word: ").upper()

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
            break

        if guess in WORDS:
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
        else:
            print("Not in the list.")

if __name__ == "__main__":
    main()
