#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

number = int(input("Enter a number:"))

print (f"Given number: {number}")

while number > 0:
    digit = number % 10

    number = number // 10
    print(digit, end=" ")