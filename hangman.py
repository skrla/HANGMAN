import random
import string
print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit')


def menu():
    return input()


def game():
    word = ['python', 'java', 'kotlin', 'javascript']
    lost = random.choice(word)
    shownot = list("-"*(len(lost)))
    show = "".join(shownot)
    counter1 = 8
    guess = []
    while counter1 > 0:
        print()
        show = ''.join(shownot)
        print(show)
        letter = input("Input a letter: ")
        if show == lost:
            print(f"You guessed the word {show}!")
            print("You survived!")
            break
        elif 0 < len(letter) < 2:
            if letter in string.ascii_lowercase:
                if letter in guess:
                    print("You've already guessed this letter")
                elif letter in lost:
                    for i in range(len(lost)):
                        if letter == lost[i]:
                            shownot[i] = letter
                            guess.append(letter)
                else:
                    print("That letter doesn't appear in the word")
                    counter1 -= 1
                    guess.append(letter)
            else:
                print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")
    else:
        print("You lost!")

        
while menu() == 'play':
    game()
