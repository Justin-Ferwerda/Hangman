import bs4
import requests
from time import gmtime, strftime
import re
import time

# Webscrapes for the dictionary.com word of the day

url = requests.get('https://www.dictionary.com/e/word-of-the-day/')
soup = bs4.BeautifulSoup(url.text, 'lxml')
word_of_the_day = soup.select_one('.otd-item-headword__word')
date = soup.select_one('.otd-item-headword__date')
current_date = re.search(strftime('%A, %B %d, %Y'), date.text)

# Variables

word = word_of_the_day.text.translate({ord(i): None for i in '\n'})
word_list = list(word)
display_word = '_' * len(word)
guess = ''
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
wrong_choice = []
choices_left = 6
spot_in_word = 0
letters_guessed = []
playing = True
display_word_list = list(display_word)
index_list = []

# Functions

def hangman():
    print('----')
    print('|   |')
    print('    |')
    print('    |')
    print('    |')
    print('    |')
    print('  -----')
    print('\n')
    print('\n')

def hangman_5():    
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print('     |')
    print('     |')
    print('     |')
    print('   -----')
    print('\n')
    print('\n')

def hangman_4():
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print(' |\  |')
    print('     |')
    print('     |')
    print('   -----')
    print('\n')
    print('\n')

def hangman_3():
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print('/|\  |')
    print('     |')
    print('     |')
    print('   -----')
    print('\n')
    print('\n')

def hangman_2():
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print('/|\  |')
    print(' |   |')
    print('     |')
    print('   -----')
    print('\n')
    print('\n')

def hangman_1():
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print('/|\  |')
    print(' |   |')
    print('/    |')
    print('   -----')
    print('\n')
    print('\n')

def hangman_0():
    print(' ----')
    print(' |   |')
    print(' 0   |')
    print('/|\  |')
    print(' |   |')
    print('/ \  |')
    print('   -----')
    print('\n')
    print('\n')

def print_hangman():
    if choices_left == 6:
        hangman()
    if choices_left == 5:
        hangman_5()
    elif choices_left == 4:
        hangman_4()
    elif choices_left == 3:
        hangman_3()
    elif choices_left == 2:
        hangman_2()
    elif choices_left == 1:
        hangman_1()
    elif choices_left == 0:
        hangman_0()

def letter_to_guess():
    global guess
    global letters_guessed
    if guess not in alpha:
        guess = input('Please guess a letter!')
    
def already_guessed():
    global guess
    if guess in letters_guessed:
        guess = input('Letter already guessed, please choose another!')

def change_display_word():
    global guess
    global display_word
    global index_list
    global display_word_list
    for index in index_list:
        display_word_list[index] = guess
    display_word = ''.join(map(str, display_word_list))
    index_list = []

def check_guess():
    global choices_left
    global guess
    global word
    global index_list
    global playing
    if guess not in word:
        print(f"I'm sorry {guess} is not in the word!")
        wrong_choice.append(guess)
        letters_guessed.append(guess)
        choices_left -= 1
        print(f"You have {choices_left} guesses left!")
        guess = ''
    elif guess in word:
        for i, char in enumerate(word):
            if guess == char:    
                index_list.append(i)
        print(f"Yes! {guess} is in the word!")
        letters_guessed.append(guess)
        change_display_word()
        guess = ''

def is_game_over():
    global playing
    global display_word
    if '_' not in display_word:
        print('You have guessed the word! Congratulations!')
        print(display_word)
        playing = False
    elif choices_left == 0:
        print("I'm sorry you've been hanged!")
        playing = False
    else:
        pass 

def guessed_letters():
    global letters_guessed
    _ = ' '.join(map(str, letters_guessed))
    print("You've guessed these letters: " + _)

# logic

print("Welcome to Hangman!")
print(f"This word is Dictionary.com's word of the day for {current_date.group()}")
print("Let's get to work!")
time.sleep(.5)
print('\n')
print('\n')

while playing:

    print_hangman()
    print(display_word)
    guessed_letters()
    letter_to_guess()
    already_guessed()
    check_guess()
    is_game_over()

























