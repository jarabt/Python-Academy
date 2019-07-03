sentence = input("Please enter a sentence: ")
word = input("Please enter a word you want to search for: ")

i = sentence.find(word)

if i != -1:
    print("I have found the word at index " + str(i) +  ".")
else:
    print("The word not found.")
