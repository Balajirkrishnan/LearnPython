#Exercise 7: Return the count of a given substring from a string

def checkString(string, substring):
    count = string.count(substring)
    return count

string = "Emma is good developer. Emma is a writer... Emma"
substring = "Emma"

print (f"Count: {checkString(string,substring)}")