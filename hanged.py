import curses
from curses import wrapper
import random
import time

# Hi leoleo again, i just added the code that i used to create the hangman
# curses if basically a wrapper for the ncurses library that is used to create a terminal interface and it's used to create the hangman
# enjoy the code

lives = 7
fails = 0

hanged_parts = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""
]
# Here i just created a list of strings that will be used to print the hangman as the game progresses

words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
# Here i just created a list of words that will be used to play the game and i randomly chose one of them

def draw_hangman(fails, stdscr):
    global hanged_parts
    # takes the amount of fails and iteartes through the list of strings to print the hangman except that it's reversed because the list is in the order of the hangman's parts being added
    for i in range(fails):
        stdscr.addstr(5, 0, hanged_parts[6 - i])
    stdscr.refresh()
    # Here i just printed the hangman according to the number of fails

def main(stdscr):
    global lives
    global fails
    global word
    global hanged_parts
    global words

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(1)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()

    word_to_guess = list("-" * len(word))
    guessed_letters = []
    # Here i created a list of dashes that will be used to print the word to guess and a list of letters that will be used to print the letters that the user has already guessed

    while True and lives > 0:
        stdscr.clear()
        stdscr.addstr(2, 0, " ".join(word_to_guess))
        stdscr.addstr(25, 0, "Input a letter: ")
        stdscr.addstr(26, 0, "".join(guessed_letters))
        stdscr.refresh()
        draw_hangman(lives, stdscr)
        key = stdscr.getch()
        if key not in range(97, 123):
            continue
        # Here i just printed the word to guess and the letters that the user has already guessed
        for i in range(len(word)):
            if chr(key) == word[i]:
                word_to_guess[i] = chr(key)
        # Here i checked if the letter that the user has inputted is in the word to guess and if it is i replaced the dash with the letter
        if chr(key) not in word:
            lives -= 1
            fails += 1
        # Here i checked if the letter that the user has inputted is in the word to guess and if it isn't i removed a life
        if chr(key) not in guessed_letters:
            guessed_letters.append(chr(key))
        # Here i just added the letter that the user has inputted to the list of letters that the user has already guessed
        if "-" not in word_to_guess:
            stdscr.clear()
            stdscr.addstr(2, 0, " ".join(word_to_guess))
            stdscr.addstr(25, 0, "You guessed the word!")
            stdscr.addstr(26, 0, "You survived!")
            stdscr.refresh()
            time.sleep(3)
            break
        # Here i checked if the word to guess has been guessed and if it has i printed a message and i exited the loop
        if lives == 0:
            stdscr.clear()
            stdscr.addstr(2, 0, " ".join(word_to_guess))
            stdscr.addstr(25, 0, "You are hanged!")
            stdscr.refresh()
            time.sleep(3)
            break
        # Here i checked if the user has lost all his lives and if he has i printed a message and i exited the loop


wrapper(main)
print(word)
# def main(stdscr):
    
# wrapper(main)
