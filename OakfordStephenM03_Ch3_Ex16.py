#This program determines if the selected
#year is a leap year

#Get the user's selected year
year = int(input('Please enter a year:'))

#Determine if year selected divided by 100 and 400 
#both get a remaineder of 0 
if year%100 == 0 and year%400 == 0:
    print('In', year, 'February has 29 days.')

#Determine if year selcted is divisible by 4
elif year%4 == 0:
    print('In', year, 'February has 29 days.')


else:
    print('In', year, 'February has 28 days.')

print('Stephen Oakford')
print('Why not just use only the second "if" statement to determine')
