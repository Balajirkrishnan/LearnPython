#Exercise 12: Calculate income tax for the given income by adhering to the below rules


income = int(input("Enter the income: "))
tax_payable = 0

print (f"Given Income: {income}")

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    taxable_income = income - 10000

    tax_payable = taxable_income * 10 / 100
else:
    tax_payable = 0

    tax_payable = 10000 * 10 /100

    tax_payable += (income -20000) * 20 / 100

print (f"total tax: {tax_payable}")