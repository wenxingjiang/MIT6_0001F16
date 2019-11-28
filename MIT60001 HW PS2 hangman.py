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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in list(secret_word):
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    comprised = []
    for i in secret_word:
        if i in letters_guessed:
            comprised.append(i)
        else:
            comprised.append('_ ')
    return ''.join(comprised)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    fulllist = list(string.ascii_lowercase)
    finallist = fulllist[:]
    for i in list(letters_guessed):
        if i in fulllist:
            finallist.remove(i)
    return ''.join(finallist)


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
    guesses = 6
    warnings = 3
    letters_guessed = []
    while guesses >0 and is_word_guessed(secret_word, letters_guessed) is False: #Decide by guesses left and if guessed
        print(f'You have {guesses} guesses left,\nyou have {warnings} warnings left,')
        print('Available letters: ', get_available_letters(letters_guessed))

        #get correct input from user,
        #1, needs to be alphabetical,
        #2, Length needs to be 1,
        #3, Not guessed before,
        yourguess = str.lower(input('Please guess a letter: ')) #get in put guess and convert to lower case
        while str.isalpha(yourguess) is False or len(yourguess)!= 1 or yourguess in letters_guessed:
            warnings -= 1
            print(f'you have {warnings} warnings left')
            if str.isalpha(yourguess) is False:
                if yourguess == '*':
                    show_possible_matches(secret_word)
                else:
                    print('only alphabet letter is allowed! ')
            if len(yourguess) != 1:
                print('only one letter is allowed! ')
            if yourguess in letters_guessed:
                print('You have already guessed the word!')

            yourguess = input('Please guess a letter: ')
            if warnings == 0:
                guesses -= 1
                print(f'you lost one guess, now you have {guesses} guesses left')
                print('---------------------')
                warnings =3
        letters_guessed.append(yourguess)

        #test the guesses:
        if yourguess in list(secret_word):
            print('good guess', get_guessed_word(secret_word, letters_guessed))
        else:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            guesses -= 1
        print('---------------------')
    score = guesses+len(set(secret_word))
    if guesses == 0:
        print(f'You used all guesses,and you failed\n the word was {secret_word}')
    else:
        print(f'Congratulations, you won!\nYour total score for this game is {score}')




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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
    if len(my_word) == 0 and len(other_word) == 0:
        return True
    elif (len(my_word) == 0 and len(other_word) != 0) or (len(my_word) != 0 and len(other_word) == 0):
        return False
    else:
        if my_word.strip()[0] == '_':
            return match_with_gaps(my_word.strip()[1:],other_word[1:])
        else:
            return my_word.strip()[0] == other_word[0] and match_with_gaps(my_word.strip()[1:],other_word[1:])


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match_list = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            match_list.append(other_word)
    if len(match_list) != 0:
        print(match_list)
    else:
        print('No matches found')




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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
