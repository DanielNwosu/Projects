# Problem Set 2, hangman.py
# Name: Daniel Nwosu
# Collaborators:
# Time spent: 5 days

# Hangman Game

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):

    import random
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
        else:
            return True
    pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    string = ''
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += '_'
    return string


    #print('sorry that letter is not in my word')
    #print(reveal)
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    import string
    string = string.ascii_lowercase
    letters = ''
    for i in string:
        if i not in letters_guessed:
            letters += i
    return letters
    pass
    
    

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

    print('welcome to the game hangman')
    print('I am thinking of a word that is', len(secret_word), ' letters long')
    letters_guessed = ''
    lives = 6
    warnings = 3
    print('_' * 10)
    while True:
        print('you have', lives, ' guesses left, and ', warnings, ' warnings left')
        print('available letters: ', get_available_letters(letters_guessed))
        guess = input('guess any letter: ')
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed += guess
            print('good guess: ', get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print('you already guessed this! ', get_guessed_word(secret_word, letters_guessed))
        elif guess.isalpha() != True:
            print('this is not a letter!')
            warnings -= 1
        else:
            letters_guessed += guess
            print('oops, that letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            lives -= 1
        print('_' * 10)
        if lives <= 0 or warnings <= 0:
            print('sorry you are out of lives. Word was: ', secret_word)
            break
        if is_word_guessed(secret_word, letters_guessed):
            total_score = lives*len(secret_word)
            print('congrats, you are a champion')
            print('total score: ',total_score)
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)l


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

    my_word = my_word.replace(" ","")
    if len(my_word) == len(other_word):
        for i in range (0, len(other_word)):
            if my_word[i] != '_':
                if my_word[i] == other_word[i]:
                    continue
                else:
                    return False
            else:
                continue
        return True
    return False
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    words_list = []
    for i in range (0, len(wordlist)):
        other_word = wordlist[i]
        if match_with_gaps(my_word,other_word) is True:
            words_list.append(other_word)
    print(words_list)
    pass



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

    print('welcome to the game hangman')
    print('I am thinking of a word that is', len(secret_word), ' letters long')
    letters_guessed = ''
    lives = 6
    warnings = 3
    letter = ('_' + ' ') * len(secret_word)
    my_word = letter.replace(' ','')
    print('_' * 10)
    while True:
        print('you have', lives, ' guesses left, and ', warnings, ' warnigs left')
        print('available letters: ', get_available_letters(letters_guessed))
        guess = input('guess any letter: ')
        if guess in secret_word and guess not in letters_guessed:
            letters_guessed += guess
            print('good guess: ', get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print('you already guessed this! ', get_guessed_word(secret_word, letters_guessed))
        elif guess.isalpha() != True and guess != '*':
            print('this is not a letter!')
            warnings -= 1
        else:
            letters_guessed += guess
            print('oops, that letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            lives -= 1
        print('_' * 10)
        if guess == '*':
            my_word = letter
            show_possible_matches(my_word)

        if lives <= 0 or warnings <= 0:
            print('sorry you are out of lives. Word was: ', secret_word)
            break
        if is_word_guessed(secret_word, letters_guessed):
            total_score = lives*len(secret_word)
            print('congrats, you are a champion')
            print('total score: ',total_score)
            break


    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
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

