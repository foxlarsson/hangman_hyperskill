import random
from string import ascii_lowercase

word_base = ['python', 'java', 'kotlin', 'javascript']
random.seed()
random_word = random.choice(word_base)
word_map = tuple(random_word)
guessing_board = list("-" * len(random_word))
letters = set(letter for letter in random_word)
input_letter = ""
guessed_letters = set()
guessed_wrong_letters = set()
ascii_list = set(ascii_lowercase)
loss_counter = 0
attempts = 8
action = "play"

print("H A N G M A N")

while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action != "play" and action != "exit":
        print('Please type either "exit" or "play"')
        print("")
        continue
    elif action == "exit":
        break

    while loss_counter < attempts:
        print("")
        print("".join(guessing_board))
        input_letter = input("Input a letter: ")
        if len(input_letter) != 1:
            print("You should print a single letter")
        elif input_letter not in ascii_list:
            print("It is not an ASCII lowercase letter")
        elif input_letter in letters:
            if input_letter in guessing_board:
                print("You already typed this letter")
                if loss_counter == attempts:
                    break
            else:
                for i in range(len(guessing_board)):
                    if word_map[i] == input_letter:
                        guessing_board[i] = input_letter
                        guessed_letters.add(input_letter)
                if "-" not in guessing_board:
                    break
        else:
            if input_letter in guessed_wrong_letters:
                print("You already typed this letter")
            else:
                loss_counter += 1
                guessed_wrong_letters.add(input_letter)
                if loss_counter != attempts:
                    print("No such letter in the word")

    if "-" not in guessing_board:
        print("You guessed the word", "".join(guessing_board) + "!")
        print("You survived!")
    else:
        print("You are hanged!")
    print("")
