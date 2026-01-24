# Configuration
LETTERS = {"A", "I", "P", "C", "R", "H", "G"}
CENTER = "A"

# Embedded dictionary (50 words)
WORD_LIST = [
    "AGAR", "AGARIC", "AGRA", "ARCHAIC", "ARCH", "ARGAL", "ARGIL",
    "GAR", "GARCIA", "GARLIC", "GARI", "GIRA",
    "HAIR", "HAIRCAP", "HAIRGRIP",
    "HARP", "HARPICA", "HARPIC",
    "CHAR", "CHAIR", "CHAIRING", "CHARA",
    "CHIRP", "CHIRAGRA",
    "CRAG", "CRAIG",
    "CIGAR", "CIGARAH",
    "GRAIL", "GRAPH", "GRAPHIC",
    "GRIP", "GRIPACH", "GRIPCHAR",
    "PARCH", "PARCHA", "PARCHIG", "PARCHIGRA",
    "PAIR", "PAIRING",
    "PIRACHA", "PIRACH",
    "RACH", "RACHIAL", "RACHIALGIA"
]


def load_words():
    """Filter embedded words based on puzzle rules."""
    valid = set()
    for word in WORD_LIST:
        if (
            len(word) >= 4
            and set(word).issubset(LETTERS)
            and CENTER in word
        ):
            valid.add(word)
    return valid


def score_word(word):
    """Return score for a given word."""
    if len(word) == 4:
        return 1
    if set(word) == LETTERS:
        return len(word) + 7  # pangram bonus
    return len(word)


def main():
    print("Welcome to Spelling Bee")
    print(f"Your letters are: {' '.join(sorted(LETTERS))}")
    print(f"Center letter: {CENTER}")
    print("Type QUIT to stop.\n")

    words = load_words()
    found = set()
    total_score = 0

    while True:
        guess = input("Guess a word: ").strip().upper()

        if guess == "QUIT":
            break

        if not guess.isalpha():
            print("Only letters allowed.")
            continue

        if CENTER not in guess:
            print(f"Your word must include the center letter: {CENTER}")
            continue

        if not set(guess).issubset(LETTERS):
            print("You used letters not in the puzzle.")
            continue

        if guess not in words:
            print("Not in the word list.")
            continue

        if guess in found:
            print("Already found that one.")
            continue

        points = score_word(guess)
        total_score += points
        found.add(guess)

        print(f"Good job! {guess} is worth {points} points.")
        print(f"Total score: {total_score}\n")

    print("\nThanks for playing!")
    print(f"You found {len(found)} words and scored {total_score} points.")


if __name__ == "__main__":
    main()
