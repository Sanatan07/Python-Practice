#variables
print("Example for Variables:")
name = "Sanatan Bramhane"
print("Hello ", name)
age = 24

print("----------------------------------------")

#print statment
print("Example for print function:")
print(name + " age is", age, "years old")

#escape sequences
print("Example for Escape Sqeuences:")
print(r'1. \n', "this is used to print a new line also known as new line character")
print(r'2. \t', "this is used to give a extended space in a sentence as a tab")
print(r'3. \\', "this is used to print a single character")
print(r'4. \'', "this is used to print a single quote in the sentence")
print(r'5. \"', "this is used to print a double quote in the sentence")
print("Hi. \nHow are you!")
print("Hi. \tHow are you!")
print("Hi. \\How are you!")
print("Hi. This is sanatan\'s house.")
print("Hi. This is you are calling at Bramhane \"nHow are you!")

print("----------------------------------------")
#Strings
#Index of a character in a string
print("Example for Index Function:")
name = "Sanatan"
print(name.index('n'), "so the first occurance of letter n is at index 2. This gives the first occurance of the character mentioned in the function")

print(name.index('n', 3)," so the first occurance of letter n is at index 6 after 3rd index. Here you can also give a second parameter where you can specify after which index you need to search for the index of that character or element")

print("----------------------------------------")

#Replace a string in a sentence
print("Example for Replace Function:")
sentence = "This is our house"
print(sentence)
print(sentence.replace("our", "my"))



#Convert Lowercase to Uppercase
print("Example for Upper Function:")
print(name.upper())


#convert Uppercase to Lowercase 
print("Example for Lower Function:")
print(name.lower())
