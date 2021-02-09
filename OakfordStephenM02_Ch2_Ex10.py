#This program calculates the amount of  
#ingredients needed to use to make the
#amount of cookies specified

#Get the user's amount of cookies
amount = int(input('What is the amount of cookies you would like to make? '))

#Named Constants
sugarCups = 1.5
butterCups = 1
flourCups = 2.75

#Calculate the multiplier by dividing the amount of cookies he or she is 
#making by 48
multiplier = amount/48

#Adjust the amount needed of each ingredient for the new recipe
totalSugar = multiplier*1.5
totalButter = multiplier*1
totalFlour = multiplier*2.75

#Display the data with 2 decimals
print('You need ', format(totalSugar, '.2f') , 'cups of sugar to make', amount , 'of cookies.')
print('You need ', format(totalButter, '.2f') ,  'cups of butter to make', amount , 'of cookies.')
print('You need ', format(totalFlour, '.2f') ,  'cups of flour to make', amount , 'of cookies.')     
      

print('Stephen Oakford')
