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

    # this is called a walrus operator := it is a form of assignment expression
    if words := [
        word.upper()
        for word in wordlist
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(words)
    else:
        console.print("No words of length of 5 in the word list", style="warning")
        raise SystemExit()

def guess_word(previous_guesses):
    
    guess = console.input("\nGuess word: ").upper()
    
    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)

    if len(guess) < 5:
        console.print(f"Guess must be 5 letters\nYour guess '{guess}' was {5 - len(guess)} letters short")
        return guess_word(previous_guesses)
    elif len(guess) > 5:
        console.print(f"Guess must be 5 letters\nYour guess '{guess}' was {len(guess) - 5} letters long")
        return guess_word(previous_guesses)
    elif type(guess) != str:
        console.print(f"{guess}")
    else:
        return guess

    
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
        
def end_game(guesses, word, guessed_correctly=False):
    
    refresh_page(headline="Game Over")
    show_guess(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word is {word}[/]")

def valid_input(guess):
    breakpoint()
    for i in guess:
        if ord(i.lower()) in range(97,123):
            return True

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

        guesses[guess_count] = guess_word(previous_guesses=guesses[:guess_count])
        if guesses[guess_count] == word:
            guessed_correctly = True
            break
    #Post-Process
    end_game(guesses, word, guessed_correctly)

if __name__ == '__main__':
    main()
