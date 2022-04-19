#Exercise 9: Check Palindrome Number

num = int(input("Enter a number:"))
rev_num = int(str(num)[::-1])
print (rev_num)

if num == rev_num:
    print (f"{num} is a Palindrome number")
else:
    print (f"{num} is NOT a Palindrome")