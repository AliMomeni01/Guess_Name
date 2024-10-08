Word Guessing Game

This is a simple word guessing game where the player tries to guess the letters of a randomly selected name. The player has a limited number of attempts to guess the correct letters, and the game provides feedback after each guess. If the player successfully guesses all letters within the available attempts, they win; otherwise, they lose.
How It Works

    The program randomly selects a name from a predefined list (Abas, Namdar, Sievasch, Mahtab).
    The name is hidden, and the player needs to guess one letter at a time.
    After each guess, the game checks if the letter is in the word:
        If the letter is correct, it is revealed in the correct position(s).
        If the letter has already been guessed, the player is notified.
        If the guess is incorrect, the player loses one of their remaining attempts.
    The game ends when the player either correctly guesses all the letters or runs out of attempts.

Features

    Randomly selects a name from the list.
    Tracks the number of remaining attempts.
    Handles repeated guesses by notifying the player if a letter has been guessed before.
    Displays the progress after each guess by showing the correctly guessed letters and blanks for the remaining ones.
    Ends the game with a "win" or "lose" message depending on the outcome.

How to Play

    The program will display the number of letters in the name as underscores (e.g., _ _ _ _ _).
    You will be prompted to guess a letter.
    If your guess is correct, the letter will be revealed in the appropriate position(s).
    If your guess is incorrect, you lose one attempt.
    You win if you guess the entire word before running out of attempts, otherwise, you lose.

Example

less

Your name has _ _ _ _ _ letters
Please guess a letter in the name: a
You are right, the word is _ a _ _ a
Please guess a letter in the name: n
You are right, the word is N a _ _ a
You win!

Requirements

    Python 3.x