import random, sys

#randomly return a word from the list
words = ["fly", "free", "fox", "farm"]
random_index = random.randint(0, len(words)-1)
word = words[random_index].strip()
print(word)

#returns an "empty" container
original_word = []
#returns list of characters from "word"
original_word[:0] = word 
#returns size of container
chosen_word =len(word)
#returns random index
index = random.randint(0, len (original_word) -1) 
#returns random letter
letter = original_word[index].strip()
#prints new word to be filled
new_word = ("_" *index + letter+"_"*((chosen_word-1)-index))
print(new_word)


char = input("Guess the letter: ")
#check if input is in list and if not print "Wrong"
if char in original_word:
    print("Wrong")


#check where the character appears in the index
    for num in range(len(word)):
        if char == word[num] and new_word[num] == "_":
            word = list(new_word)
            word[num] = char
    print(word)
    str1 =" "
    print(str1.join(word))

