import string
from words import choose_word
from images import IMAGES
def ifValid(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    return True
def is_word_guessed(secret_word,letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False
def get_guessed_word(secret_word, letters_guessed):  
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1    
    return guessed_word
def get_hint(secret_word,letters_guessed):
    import random 
    letters_not_gussed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_gussed:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                letters_not_gussed.append(i)
            return random.choice(letters_not_gussed)
def get_available_letters(letters_guessed):   
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left
def hangman(secret_word):    
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    letters_guessed = []
    total_lives=remaining_lives = 8
    image_selection_list_indices=[0,1,2,3,4,5,6,7]
    user_difficulty_choice=input("app kitni difficulty par ye game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a,b ya c ki mei btaiyein\n")
    if user_difficulty_choice=="b":
        total_lives=remaining_lives=6
        image_selection_list_indices=[1,2,3,4,6,7]
        while remaining_lives>0:
            available_letters=get_available_letters(letters_guessed)
            print("availble letters: "+available_letters)
            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if guess == "hint":
                print("your hint for secret word is "+get_hint(secret_word,letters_guessed))
            else:
                if (not ifValid(letter)) and letter!="hint":
                    print("invalid input")
                    continue
                if letter in secret_word:
                    letters_guessed.append(letter) 
                    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print (" * * Congratulations, you won! * * ")
                        print ("")
                        break
                else:
                    print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    print (IMAGES[image_selection_list_indices[total_lives-remaining_lives]])
                    remaining_lives-=1
                    print ("Remaining Lives : "+str(remaining_lives))
                    print ("")
    elif user_difficulty_choice=="c":
        total_lives=remaining_lives=4
        image_selection_list_indices=[1,3,5,7]
        while remaining_lives>0:
            available_letters=get_available_letters(letters_guessed)
            print("availble letters: "+available_letters)
            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if guess == "hint":
                print("your hint for secret word is "+get_hint(secret_word,letters_guessed))
            else:
                if (not ifValid(letter)) and letter!="hint":
                    print("invalid input")
                    continue
                if letter in secret_word:
                    letters_guessed.append(letter) 
                    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print (" * * Congratulations, you won! * * ")
                        print ("")
                        break
                else:
                    print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    print (IMAGES[image_selection_list_indices[total_lives-remaining_lives]])
                    print ("Remaining Lives : "+str(remaining_lives))
                    print ("")
                    letters_guessed.append(letter)
                    remaining_lives -= 1
    else:
        if user_difficulty_choice!="a":
            print("your choice is invalid")
    while remaining_lives>0:
            available_letters=get_available_letters(letters_guessed)
            print("availble letters: "+available_letters)
            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if guess == "hint":
                print("your hint for secret word is "+get_hint(secret_word,letters_guessed))
            else:
                if (not ifValid(letter)) and letter!="hint":
                    print("invalid input")
                    continue
                if letter in secret_word:
                    letters_guessed.append(letter) 
                    print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                    print ("")
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print (" * * Congratulations, you won! * * ")
                        print ("")
                        break
                else:
                    print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                    print (IMAGES[image_selection_list_indices[total_lives-remaining_lives]])
                    print ("Remaining Lives : "+str(remaining_lives))
                    print ("")
                    letters_guessed.append(letter)
                    remaining_lives -= 1
    
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
secret_word = choose_word()
hangman(secret_word)