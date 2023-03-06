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
    
def show_guess(guesses,word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """
    for guess in guesses:
        styled_guess = []
        for letter, correct  in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")


        console.print("".join(styled_guess), justify="center")
    # if guess == word:
    #     return True
    # else:
    #     correct_letters = { letter for letter, correct in zip(guess, word) if letter == correct }
    #     misplaced_letters = set(guess) & set(word) - correct_letters
    #     wrong_letters = set(guess) - set(word)

    #     print("Correct letters:", ", ".join(sorted(correct_letters)))
    #     print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    #     print("Wrong letters:", ", ".join(sorted(wrong_letters)))
        
def end_game(guesses, word, guessed_correctly=False):
    
    refresh_page(headline="Game Over")
    show_guess(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word is {word}[/]")
    # if win:
    #     print(f"CORRECT! The Secret word was {word}")
    # else:
    #     print(f"LOSER! The Secret word was {word}")

def main():
    
    #Pre-Process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n")) 
    guesses = ["_" * 5] * 6

    #Main Process
    guessed_correctly = False
    for guess_count in range(6):

        refresh_page(headline=f"Guess {guess_count + 1}")
        show_guess(guesses, word) 
        print(f"Secret word is {word}")

        guesses[guess_count] = input("\nGuess word: ").upper() 
        if guesses[guess_count] == word:
            guessed_correctly = True
            break
    #Post-Process
    end_game(guesses, word, guessed_correctly)

def valid_input(guess):
    for i in guess:
        if ord(i.lower()) in range(97,123):
            return True

if __name__ == '__main__':
    main()
