# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


# def main():
#    hangman('apple')


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += letter + ' '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwyxz'
    for letter in letters_guessed:
        alphabet = alphabet.replace(letter, '')
    return alphabet


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    # intialize the guess and warning variables plus a whole bunch of other stuff now wooooooo
    warnings = 3
    guesses = 6
    new_line = '----------------'
    letters_guessed = ''
    valid_letters = 'abcdefghijklmnopqrstuvwyxz'
    score = 0
    vowels = 'aeiou'

    # start of the game messages
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings, 'left.')
    print(new_line)

    # now we loop through and we will get a result. If score still = 0 then the game has failed
    while guesses != 0:
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # ask for an input
        guess = input('Please guess a letter:').lower()
        # this test is if it's not a valid letter
        if guess not in valid_letters:
            if warnings < 1:
                guesses -= 1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
        # then we test if it's already been guessed
        elif guess in letters_guessed:
            if warnings < 1:
                guesses -= 1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print('Oops! You\'ve already guessed that letter. You have', warnings, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
        # now we have to actually work out a correct answer
        else:
            if guess in secret_word:
                letters_guessed += guess
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed):
                    # like the most important, updates the score variable, this is used to know if the user has won
                    score = guesses * len(secret_word)
                    guesses = 0
            elif guess in vowels:
                guesses -= 2
                print('Oops! That letter is not in my word.')
            else:
                guesses -= 1
                print('Oops! That letter is not in my word.')

    if score != 0:
        print(new_line)
        print('Congratulations, you won! \nYour total score for this game is:', score)
    else:
        print('Sorry, you ran out of guesses. The word was:', secret_word, '.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word.strip()
    index = 0
    if len(my_word) != len(other_word):
        return False
    for letters in my_word:
        if letters != '_':
            if letters != other_word[index]:
                return False
        index += 1
    return True




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace(' ', '')
    matching_words = ''
    global wordlist
    for words in wordlist:
        if match_with_gaps(my_word, words):
            matching_words += words + ' '
    if matching_words == '':
        print('No matches found')
    else:
        print(matching_words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    #Things still to implement:
    #remove the trailing none when using the * special character
    #when guessing a letter that isn't in the word update the available letters string
    #word wrap the hint words
    #check the style guide document and update as neccesary



    warnings = 3
    guesses = 6
    new_line = '----------------'
    letters_guessed = ''
    valid_letters = 'abcdefghijklmnopqrstuvwyxz*'
    score = 0
    vowels = 'aeiou'

    # start of the game messages
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings, 'left.')
    print(new_line)

    # now we loop through and we will get a result. If score still = 0 then the game has failed
    while guesses != 0:
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # ask for an input
        guess = input('Please guess a letter:').lower()

        if guess == '*':
            print('Possible word matches are:')
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        # this test is if it's not a valid letter
        elif guess not in valid_letters:
            if warnings < 1:
                guesses -= 1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
        # then we test if it's already been guessed
        elif guess in letters_guessed:
            if warnings < 1:
                guesses -= 1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                warnings -= 1
                print('Oops! You\'ve already guessed that letter. You have', warnings, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
        # now we have to actually work out a correct answer
        else:
            if guess in secret_word:
                letters_guessed += guess
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed):
                    # like the most important, updates the score variable, this is used to know if the user has won
                    score = guesses * len(secret_word)
                    guesses = 0
            elif guess in vowels:
                guesses -= 2
                print('Oops! That letter is not in my word.')
            else:
                guesses -= 1
                print('Oops! That letter is not in my word.')

    if score != 0:
        print(new_line)
        print('Congratulations, you won! \nYour total score for this game is:', score)
    else:
        print('Sorry, you ran out of guesses. The word was:', secret_word, '.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
# pass

# To test part 2, comment out the pass line above and
# uncomment the following two lines.

#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)

#print(show_possible_matches('_ee_______'))