#Print characters from a string that are present at an even index number

#Get the string
word = input("Please enter a single word:")
print (word)

length = len(word)
print (length)

for i in range(0, length-1, 2):
    print (f"Index[{i}] - {word[i]}")