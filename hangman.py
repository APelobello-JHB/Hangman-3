import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()                                                                                                                                  
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_letter = random.randint(0, len(word)-1)
    word = list(word)
    for i in range(len(word)):
        if word[i] != word[random_letter]:
            word[i] = "_"
        else:
            word[i] = word[random_letter]

    new_word = "".join(word)
    return(new_word)     


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    """
    original_word = word with underscores
    answer_word = the completed word based on the word list
    char = users input
    """
    if char in original_word and char not in answer_word:
        return True
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    answer_word = list(answer_word)
    list_word = list(answer_word) #broke word into a list
    index_char = original_word.find(char)#found index of char given by user
    if  char in original_word:
        list_word[index_char] = char #assigning the value of the char to the underscore of it's index (the char is from the user)
    more_complete_word = "".join(list_word)
    return more_complete_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer #answer is print out of word with users input


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("""/----
|
|
|
|
_______""")

    elif number_guesses == 3:
        print("""/----
|   0
|
|
|
_______""")

    elif number_guesses == 2:
        print("""/----
|   0
|  /|\\
|
|
_______""")

    elif number_guesses == 1:
       print("""/----
|   0
|  /|\\
|   |
|
_______""")

    elif number_guesses == 0:
          print("""/----
|   0
|  /|\\
|   |
|  / \\
_______""")
         

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses

def run_game_loop(word, answer):
    print("Guess the word: " + answer)
    guesses = 5
    while guesses > 0 :
        guess = get_user_input().lower()
        if guess == "exit" or guess == "quit":
            print("Bye!")
            break
        if is_missing_char(word, answer, guess) == True:
            answer = fill_in_char(word, answer, guess)
            print(answer)
            if "_" not in answer:
                break
        elif guesses >= 0:
            guesses = guesses-1
            if guesses >= 0:
                do_wrong_answer(answer,guesses)
            if guesses == 0:
                print("Sorry, you are out of guesses. The word was: "  + word)
              


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)
