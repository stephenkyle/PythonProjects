#This program calculates the discount and
#total amount of the purchase after discount

#Inform the user of the discount
print('Discounts are given for buying in quantity, 10-19 is 10% off,'
      ' 20-49 is 20%, 50-99 is 30%, 100 or more gets 40% off.' )

#Get the user's amount of packages
quantity = int(input('How many packages did you buy?'))

#If the quantity is between 10-19 then use these calculations
if quantity >=10 and quantity <=19:
    
    #calulate the discount
    discount =99*quantity*.1
    
    #calculate the total amount after discount
    total=99*quantity*.9

    #display the discount amount and total amount
    print('Your 10% discount: $', format(discount, '.2f'),sep='')
    print('Your total amount after discount: $', format(total, '.2f'),sep='')

#If the quantity is between 20-49 then use these calculations    
elif quantity >=20 and quantity <=49:
     discount =99*quantity*.2
     total=99*quantity*.8
     print('Your 20% discount: $', format(discount, '.2f'),sep='')
     print('Your total amount after discount: $', format(total, '.2f'),sep='')

#If the quantity is between 50-99 then use these calculations     
elif quantity >=50 and quantity <=99:
     discount =99*quantity*.3
     total=99*quantity*.7
     print('Your 30% discount: $', format(discount, '.2f'),sep='')
     print('Your total amount after discount: $', format(total, '.2f'),sep='')

#If the quantity is more than 100 then use these calculations     
elif quantity >100:
     discount =99*quantity*.4
     total=99*quantity*.6
     print('Your 40% discount: $', format(discount, '.2f'),sep='')
     print('Your total amount after discount: $', format(total, '.2f'),sep='')
     
else:
    #calculate the total amount without any discounts
    total =quantity*99
    print('No discount applied.')
    print('Your total amount: $', format(total, '.2f'),sep='')

print('Stephen Oakford')
    
    
