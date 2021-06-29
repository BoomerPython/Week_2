## Program: taxform.py
## Author: Ken Lambert

## Initialize the constants
taxRate = 0.20
standardDeduction = 10000.0
dependentDeduction = 3000.0

## Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

## Compute the income tax
taxableIncome = grossIncome - standardDeduction - dependentDeduction * numDependents
incomeTax = taxableIncome * taxRate

## Display the income tax
print("The income tax is $" + str(incomeTax))

