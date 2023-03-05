# wyrdle.py

import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def get_random_word(wordlist):
    """get a random word with length of 5 from list of strings
    
    ## Example:

    >>> get_random_word(["snake","dogs","pickle'd"])
    'SNAKE'
    """ 

    words = [
        word.upper()
        for word in wordlist
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    return random.choice(words)
    
def show_guess(guess,word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """

    if guess == word:
        return True
    else:
        correct_letters = { letter for letter, correct in zip(guess, word) if letter == correct }
        misplaced_letters = set(guess) & set(word) - correct_letters
        wrong_letters = set(guess) - set(word)

        print("Correct letters:", ", ".join(sorted(correct_letters)))
        print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
        print("Wrong letters:", ", ".join(sorted(wrong_letters)))
        
def end_game(word,win):
    
    if win:
        print(f"CORRECT! The Secret word was {word}")
    else:
        print(f"LOSER! The Secret word was {word}")

def main():
    
    #Pre-Process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n")) 
    print(f"Secret word is {word}")

    #Main Process
    for guess_count in range(1,7):
        guess = input(f"\nGuess {guess_count}: ").upper()
        if show_guess(guess,word):
            end_game(word,win=True)
            break

    #Post-Process
    else:
        end_game(word,win=False)

if __name__ == '__main__':
    main()
