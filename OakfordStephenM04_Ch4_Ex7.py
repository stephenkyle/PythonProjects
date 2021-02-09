# This program calculates the amount of money a
# person would earn over a period of time

# Get the amount of days
end = int(input('How many days?'))

# Validaiton loop to get no negative days
while end<0:
    print('ERROR: The days cannot be negative')
    end  = int(input('How many days?'))

# Set the pay for the first day and total amount
pay = 1
total = 0

# Print the table headings
print()
print('Day\tPay')
print('------------')

# Print the day and their pay for the day
for days in range(1, end+1):
      print(days, '\t', pay)
      total+=pay
      pay=pay*2

# Convert the total amount into dollars and not pennies
total = total/100

# Print the total amount
print('The total amount earned in', days, 'days: $', format(total, ',.2f'))

print('Stephen Oakford')
