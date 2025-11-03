import random

# List of possible words
word_list = [
    "python", "hangman", "challenge", "programming", "artificial", 
    "intelligence", "developer", "computer", "algorithm", "variable"
]

# Hangman stages for visual display
stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """
]

def hangman():
    word = random.choice(word_list).lower()
    word_letters = set(word)
    guessed_letters = set()
    attempts = len(stages) - 1

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0 and word_letters:
        print(stages[attempts])
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts}")

        # Display current word progress
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word:", " ".join(word_display))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("❗ You've already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!\n")
        else:
            attempts -= 1
            print("❌ Wrong guess!\n")

    # Game over
    if not word_letters:
        print(f"🎉 You guessed the word '{word}' correctly! You win!")
    else:
        print(stages[0])
        print(f"💀 Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
