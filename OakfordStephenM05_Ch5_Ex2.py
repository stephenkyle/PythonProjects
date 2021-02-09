# This program calculates total cost of item with 
# state and county taxes.


# Named constants fot taxes
stateSalesTaxAmount = 0.05
countySalesTaxAmount = 0.025

# The main function
def main():
    # Get the user's amount of purchase
    amount = float(input('What is the amount of the purchase? '))

    # Call calculate state tax function
    stateTax = calculate_stateTax(amount)

    #Call calculate county tax function
    countyTax = calculate_countyTax(amount)

    #Call calculate total tax function
    totalTax = calculate_totalTax(stateTax, countyTax)

    #Call calulate total function
    total = calculate_total(amount, totalTax)
    
    # Call output_total function
    output_total(amount, stateTax, countyTax, totalTax, total)



def calculate_stateTax(amount):
    # Calculate state taxes
    return amount*stateSalesTaxAmount

    # Calculate county taxes
def calculate_countyTax(amount):    
    return amount*countySalesTaxAmount

    # Calculate total amount of taxes
def calculate_totalTax(stateTax, countyTax):
    return stateTax+countyTax
 
    # Calculate total cost with taxes added
def calculate_total(amount,totalTax):
    return amount+totalTax
    

# The output_total function displays the total with taxes
def output_total(amount, stateTax, countyTax, totalTax, total):
    print('Amount of purchase\t $',format(amount, '.2f'), sep='') 
    print('State Sales Tax\t\t $',format(stateTax, '.2f'), sep='')
    print('County Sales Tax\t $',format(countyTax, '.2f'), sep='')
    print('Total Sales Tax\t\t $',format(totalTax, '.2f'), sep='')
    print('Total Amount\t\t $',format(total, '.2f'), sep='')


# Call the main function
main()

print('Stephen Oakford')
