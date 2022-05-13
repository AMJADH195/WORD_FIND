# Name:
# Student Number:

# This file is provided to you as a starting point for the "word_find.py" program of Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary modules.
import enchant  # Used to import pyenchant package.
# Used to convert between JSON-formatted text and Python variables.
import json
# Used to provide convenient access to a string variable containing all uppercase letters.
import string
import random  # Used to randomly select letters.


wordlist = []
SCORE = 0
dict_list = []
SHUFFLE = True
# This function generates and returns a list of 9 letters.  It has been completed for you.
# See Point 1 of the "Functions in word_find.py" section of the assignment brief.


def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2,
                      6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(
        string.ascii_uppercase, weights=letter_weights, k=9)

    # We've selected a list of 9 random letters using the specified letter frequencies, and now return it.
    return chosen_letters


# This function displays the 9 letters in a 3x3 grid.
# See Point 2 of the "Functions in word_find.py" section of the assignment brief.
def display_letters(letters):
    '''
     Function for displaying letters in a grid.
    '''
    global SHUFFLE
    if(SHUFFLE==True):
        random.shuffle(letters)
        SHUFFLE=False
    split_lists = [letters[x:x+3] for x in range(0, len(letters), 3)]
    for i in range(3):
        print(*split_lists[i], sep=' | ')
        if(i < 2):
            print('----------')
def checkmultipleocc(list, wrd):
    '''
     Function for checking multiple occurances of letters from the list
    '''
    listcout = {}
    wordcnt = {}
    for l in wrd:
        listcout[l] = list.count(l)
        wordcnt[l] = wrd.count(l)
    for k in wordcnt:
        if(wordcnt[k] > listcout[k]):
            return(False)
    return(True)
def checklength(word):
    '''
      Function for checking word length
    '''
    if(len(word) < 3):
        return(False)
    else:
        return(True)
def checkvalidenglish(word):
    '''
      Function for checking weather a word is valid english word
    '''
    d = enchant.Dict("en_US")  # US dictionary. Other option is en_GB
    return(d.check(word))
def getscore(word):
    '''
     Function for calculating scrabble score for the word
    '''
    SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    total = 0
    for letter in word:
        total += SCORES[letter.lower()]
    return total
def checkduplicates(word):
    '''
     Function for checking if the word is previously used or not
    '''
    if str(word).upper() in wordlist:
        return(False)
    else:
        return(True)
def printsore():
    '''
     Function for printing final score
    '''
    print(f'Your final score was '+str(SCORE)+'.\nThank you for playing!')
def logscore(letterlist, wordlist,score):
    '''
     Function for logging details into text file
    '''
    if score>=50:
        with open('log.txt') as f:
            json_data = json.load(f)
        wordlist.sort()
        json_data.append(
            {
                "letters": letterlist,
                "words": wordlist,
                "score": SCORE})
        f.close()
        with open('log.txt', "w") as file:
            json.dump(json_data, file,indent = 3)
        file.close()
        print("Congratulations ! Your score is "+str(score)+".")
    else:
        print(f'Your final score was '+str(score)+'\nThank you for playing')
# This function checks whether a word entered by the user contains appropriate letters.
# See Point 3 of the "Functions in word_find.py" section of the assignment brief.
def validate_word(word, letters):
    '''
     Function for checking if the word entered by the user contains appropriate letters
    '''
    llist = letters
    for e in word:
        if e not in llist:
            return(False)
    return(True)

ISHARD_MODE = False
print('Welcome to Word Find')
print('Come up with as many words as possible from the letters below!')
while True:
    data = input("Do you wish to play [e]asy mode or [h]ard mode?: ")
    if data.upper() == 'E':
        ISHARD_MODE = False
        print('Easy mode')
        break
    elif data.upper() == 'H':
        ISHARD_MODE = True
        print('Hard mode selected,Entering an invalid word will end the game!')
        break
    else:
        print('Invalid input, please select a mode.')
        continue
letters_list = select_letters()
while True:
    print('Score:'+str(SCORE)+'. Your letters are:')
    display_letters(letters_list)
    userinput = input(
        "Enter a word, [s]huffle letters, [l]ist words, or [e]nd game :")
    if userinput.upper() == 'S':
        print('Shuffling letters...')
        SHUFFLE=True
        continue
    elif userinput.upper() == 'L':
        if wordlist:
            wordlist.sort()
            print('Previously entered words:')
            for i in wordlist:
                print(' - '+str(i).upper())
        else:
            print('You have not yet entered any words')
        continue
    elif userinput.upper() == 'E':
        logscore(letters_list, wordlist,SCORE)
        break
    else:
        if(checklength(userinput.upper())):
            if(validate_word(userinput.upper(), letters_list)):
                if(checkmultipleocc(letters_list, userinput.upper())):
                    if(checkvalidenglish(userinput.upper())):
                        if(checkduplicates(userinput.upper())):
                            wordlist.append(userinput.upper())
                            SCORE += getscore(userinput.upper())
                            print(userinput.upper()+' accepted - '+str(getscore(userinput.upper())
                                                                       )+' awarded. Your score is now '+str(SCORE)+'.')
                        else:
                            if(ISHARD_MODE == True):
                                print('Word alredy exist! Game over!')
                                printsore()
                                logscore(letters_list, wordlist,SCORE)
                                break
                            else:
                                print('Word alredy exist')
                    else:
                        if(ISHARD_MODE == True):
                            print('Not a valid english word! Game over!')
                            printsore()
                            logscore(letters_list, wordlist,SCORE)
                            break
                        else:
                            print('Not a valid english word!')
                else:
                    if(ISHARD_MODE == True):
                        print('Multiple occurance of letters! Game over!')
                        printsore()
                        logscore(letters_list, wordlist,SCORE)
                        break
                    else:
                        print('Multiple occurance of letters')
            else:
                if(ISHARD_MODE == True):
                    print('Word created with outside letters! Game over!')
                    printsore()
                    logscore(letters_list, wordlist,SCORE)
                    break
                else:
                    print('Word created with outside letters')
        else:
            if(ISHARD_MODE == True):
                print('Word length less than three! Game over!')
                printsore()
                logscore(letters_list, wordlist,SCORE)
                break
            else:
                print('Word length less than three')


# Welcome the user and create necessary variables (Requirement 1).

# Ask the user to select easy mode or hard mode (Requirement 2).

# Enter gameplay loop (Requirement 3).

    # Display score, letter grid and prompt user for input (Requirement 3.1).

    # If input is "E",
        # End the game/loop (Requirement 3.2).

    # Otherwise, if input is "S",
        # Shuffle the letters (Requirement 3.3).

    # Otherwise, if input is "L",
        # List previously used words (Requirement 3.4).

    # Otherwise, if input is less than 3 characters long,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.5).

    # Otherwise, if input is in the used words list,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.6).

    # Otherwise, if input is not valid,
        # Show appropriate message and end game if playing on hard mode (Requirement 3.7).

    # Otherwise,
        # Request Scrabble score of input, etc.
        # End game if playing on hard mode (Requirement 3.8).


# Print final score and record log of game if it is above 50 (Requirement 4).

