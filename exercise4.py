#Exercise 4: Remove first n characters from a string

def remove_char( word, length):
    print (f"Original word: {word}")
    x = word[length:]
    return x

print (f"Removing characters from a string")
print (remove_char ("pynative", 4))
print (remove_char ("pynative", 2))
