#Exercise 6: Display numbers divisible by 5 from a list

List = [10, 20, 33, 46, 55]
print (f"Given List: {List}")
print ('Divisible by 5:')
for num in List:
    if num % 5 == 0:
        print (num)
