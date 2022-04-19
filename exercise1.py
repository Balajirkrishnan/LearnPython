#Calculate the multiplication and sum of 2 numbers

def multiplication_or_sum(num1, num2):
    #Calculate the product
    product = num1 * num2

    #Check if product is greater than 1000
    if product <= 1000:
        return product
    else:
        return num1 + num2

num1 = int(input("Enter the fist number: "))
num2 = int(input("Enter the second number: "))

result = multiplication_or_sum(num1, num2)
print (f"The result is {result}")

