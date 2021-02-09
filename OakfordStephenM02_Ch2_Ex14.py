#This program calculates compound interest for
#an account after a specified amount of years

#Get the user's amount of intially deposited, annual interest rate,
#number of times per year compounded, and number of years left alone
deposited = float(input('What is the amount initially deposited into the account?'))
interestRate = float(input('What is the interest rate paid by the account?'))
timesCompounded = int(input('How many times a year is the interest compounded?(For example\n'
                            '12 for once a month or 4 for quarterly. '))
years =  float(input('How many years will the account be left alone?'))

#Convert interest rate to a decimal
interestRate = interestRate/100

#Formula for compound interest
totalAmount = deposited*(1+(interestRate/timesCompounded))**(timesCompounded*years)

#Display the data
print('The amount of money in the account after ', format(years, '.0f'), ' years is $', format(totalAmount, ',.2f'), sep='')

                  

print('Stephen Oakford')
