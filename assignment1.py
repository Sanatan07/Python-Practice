#In this assignment we are going to create a simple program where we take a sentence as input and then replace a word from that sentence with a new word.


print("Assignment 1 - Replace a word in the sentence.")
sentence = input('Input a sentence: ')
word1 = input('Input the word that you want to replace from the sentence: ')
word2 = input('Input the new word that will be replaced with word one: ')

new_sentence = sentence.replace(word1,word2)
print("The new sentence is: ", new_sentence)