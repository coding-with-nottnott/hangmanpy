import random
import sys
HANGMAN_ART = ['''
+---+
|
|
|
===''', '''
+---+
O |
|
|
===''', '''
+---+
O |
| |
|
===''', '''
+---+
O |
/| |
|
===''', '''
+---+
O |
/|\ |
|
===''', '''
+---+
O |
/|\ |
/ |
===''', '''
+---+
O |
/|\ |
/ \ |
===''', '''
+---+
[O |
/|\ |
/ \ |
===''', '''
+---+
[O] |
/|\ |
/ \ |
===''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
  'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
  'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
 'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}
POSSIBLE_WORDS = "apple pear grapes pineapples".split()

class Hangman:
    def __init__(self):
        self.reset()
    #game variables
    def reset(self, debug=False):
        self.error_count = 0
        self.wrong_guessed_letters = []
        self.right_guessed_letters = []
        self.mystery_word_set = random.choice(list(words.keys()))
        self.mystery_word = random.choice(list(words[self.mystery_word_set]))
        #self.mystery_word = POSSIBLE_WORDS[random.randint(0, len(POSSIBLE_WORDS) - 1)]
        self.blanks = '_ ' * len(self.mystery_word)
        self.rendered_word = ''
        self.game_won = False
        self.game_lost = False
        self.debug = debug

    def draw_hangman_art(self):
        self.rendered_word = ''
        print(HANGMAN_ART[self.error_count])
        for letter in self.mystery_word:
            if letter in self.right_guessed_letters:
                self.rendered_word += letter + ' '
            else:
                self.rendered_word += '_ '
        print("Word: " + self.rendered_word)
        print("Your word has something to do with: " + self.mystery_word_set)
        print()

    def win(self):
        print("You WON!")
        self.ask_for_replay()

    def lose(self):
        self.draw_hangman_art()
        print("You lost, sorry.")
        print("Your word was: " + self.mystery_word)
        self.ask_for_replay()

    def ask_for_replay(self):
        print("Would you like to play again? Y/N")
        answer = input().lower()
        if len(answer) > 1 or answer not in 'yn':
            print("Invalid input")
            self.ask_for_replay()
        elif answer == 'y':
            self.reset()
        else:
            sys.exit()

    def ask_for_difficulty(self, debug=False):
        print("(X_X)   H A N G M A N   (X_X)")
        print("What difficulty would you like? [E]asy, [M]edium or [H]ard?")
        answer = input().lower()
        if len(answer) > 1 or answer not in 'emhd':
            print("Invalid input")
            self.ask_for_difficulty()
        elif answer == 'e':
            self.reset(debug)
        elif answer == 'm':
            del HANGMAN_ART[8]
            del HANGMAN_ART[7]
            self.reset(debug)
        elif answer == 'h':
            del HANGMAN_ART[8]
            del HANGMAN_ART[7]
            del HANGMAN_ART[5]
            del HANGMAN_ART[3]
            self.reset(debug)
        elif answer == 'd':
            print("Debug on ya crazy person")
            debug = True
            self.ask_for_difficulty(True)

hangman = Hangman()
hangman.ask_for_difficulty()
#main game loop
while True:
    hangman.draw_hangman_art()
    if '_' not in hangman.rendered_word:
        hangman.win()
        continue
    if hangman.debug:
        print("Debug: " + hangman.mystery_word)
    guess = str(input("Enter a letter: ")).lower()
    print()
    if len(guess) > 1:
        print("Guess too long! Enter one character.")
        continue
    elif guess in hangman.right_guessed_letters or guess in hangman.wrong_guessed_letters:
        print("Already guessed! Try a letter you haven't guessed.")
        continue
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("Try entering a letter, not a number or some weird symbol")
        continue
    else:
        if guess in hangman.mystery_word:
            hangman.right_guessed_letters.append(guess)
        else:
            hangman.wrong_guessed_letters.append(guess)
            hangman.error_count += 1
            if hangman.error_count == len(HANGMAN_ART) - 1:
                hangman.lose()
                continue