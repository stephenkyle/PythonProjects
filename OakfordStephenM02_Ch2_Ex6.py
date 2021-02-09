
amount = float(input('What is the amount of the purchase? '))

stateSalesTaxAmount = 0.05
countySalesTaxAmount = 0.025

stateTax = amount*stateSalesTaxAmount
countyTax = amount*countySalesTaxAmount

totalTax = stateTax+countyTax

total = amount+totalTax

print('Amount of purchase\t $',format(amount, '.2f'), sep='') 
print('State Sales Tax\t\t $',format(stateTax, '.2f'), sep='')
print('County Sales Tax\t $',format(countyTax, '.2f'), sep='')
print('Total Sales Tax\t\t $',format(totalTax, '.2f'), sep='')
print('Total Amount\t\t $',format(total, '.2f'), sep='')


