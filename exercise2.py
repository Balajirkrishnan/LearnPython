#Exercise 2: Print the sum of the current number and the previous number

PreviousNumber = 0
for num in range(10):
    print (f"Current Number {num} Previous Number {PreviousNumber} Sum: {PreviousNumber + num}")
    PreviousNumber = num

