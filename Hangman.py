import random, string
"""
Import words from external text file and assign to a list variable:
"""
with open("word_list.txt") as word_file:
    word_list=[line.rstrip() for line in word_file]
"""
Create a player Class to allow OOP of player guesses, when/if a player loses a life and printing of player stats:
"""
class Player:
    def __init__(self):
        self.guesses=[]
        self.guess_count=0
        self.lives=7
        self.alphabet_list=[letter for letter in string.ascii_lowercase]
        
    def guess_letter(self):
        while True:
            print(f"\nThe hidden word is: {masked_word_str}")    
            self.guess=input("Please enter your next guess: ")
            if self.guess.isalpha() == False or len(self.guess) != 1:
                print("\nSorry, you must enter a single string (letter).")
            elif self.guess not in self.alphabet_list:
                print("\nSorry you have already guessed that letter.")
            else:
                self.alphabet_list.remove(self.guess)
                self.guesses.append(self.guess)
                self.guess_count+=1
                break
                
    def lose_life(self,check):
        if check == False:
            self.lives-=1
            print("\nYou have lost a life and moved one step closer to your fate.")

    def __str__(self):
        return "\nPlayer Guesses: " + str(self.guesses) + "\nPlayer Lives Remaining: " + str(self.lives)
"""
Create a function to check if a player guess is correct or not:
"""
def letter_check(word,mask,guess):
    global masked_word_str
    check_count=-1
    correct_count=0
    for letter in word:
        check_count+=1
        if letter == guess:
            mask[check_count]=guess
            masked_word_str="".join(masked_word)
            correct_count+=1
    if correct_count==0:
        return False
    else:
        return True
"""
Create a function to display the hangman relative to the players lives:
"""
def display_hangman(lives):
    if lives == 7:
        print("\n__________ ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 6:
        print("\n__________ ")
        print("|        | ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 5:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 4:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|       /  ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 3:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|       /| ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 2:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|       /|\\")
        print("|          ")
        print("|          ")
        print("|          ")
    elif lives == 1:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|       /|\\")
        print("|       /  ")
        print("|          ")
        print("|          ")
    elif lives == 0:
        print("\n__________ ")
        print("|        | ")
        print("|        O ")
        print("|       /|\\")
        print("|       / \\")
        print("|          ")
        print("|          ")
"""
Create a function to check if a player has won or lost:
"""
def win_check(mask,lives):
    global guessing
    hidden_word="".join(selected_word)
    if lives>0 and "*" not in mask:
        print("Congratulations you WIN!")
        print(f"The hidden word was {hidden_word}!")
        print(f"You guessed the word in {p.guess_count} guesses.")
        guessing = False
    elif lives == 0:
        print("You LOSE!")
        print(f"The hidden word was {hidden_word}!")
        guessing = False
"""
The game itself:
"""
"""
Select a word at random from the word list and assign it to a variable:
"""
selected_word=[letter for letter in random.choice(word_list)]
"""
Create an asterisked representation of the word at random from the word list and assign it to a variable:
"""
masked_word=["*" for letter in selected_word]
masked_word_str="".join(masked_word)
"""
Create a player variable assigned to the player class.
"""
p=Player()
"""
Print a welcome statement and basic instructions on how to play:
"""
print("\nWelcome to Hangman.\nCan you guess the hidden word to save Stick Man from the gallows?")
print("Guess one letter at a time to see if that letter is in the hidden word.\nChoose wisely, if the letter isn't in the word you will lose a life.")
print("You have 7 lives...GOOD LUCK!")
"""
Assign a variable and loop to allow the player to continue to guess until the player has won or lost:
"""
guessing=True
while guessing == True:
    p.guess_letter()
    letter_check(selected_word,masked_word,p.guess)
    p.lose_life(letter_check(selected_word,masked_word,p.guess))
    display_hangman(p.lives)
    print(p)
    win_check(masked_word,p.lives)
print("Thanks for playing!")