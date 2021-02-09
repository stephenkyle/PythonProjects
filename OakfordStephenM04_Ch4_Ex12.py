# This program calculates the factorial
# of a nonnegative number
print('This program calculates the factorial of any number.')
      
# Get the number
number = int(input('What is the number?'))

#Set the total to start the factorial multiplying
total = 1

# Validaiton loop to get no negative days
while number<0:
    print('ERROR: The days cannot be negative')
    end  = int(input('How many days?'))

# Get the factorial of the number
for factorial in range(1, number+1):
    total*=factorial

# Print the total amount
print('The factorial of', number, 'is', format(total, ','))

print('Stephen Oakford')
