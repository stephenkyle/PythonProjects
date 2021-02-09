# This program generates random numbers
# between 1-500 and then outputs the amount
# of numbers and the amount of the numbers
# added together


import random

# The randomNumber function
def randomNumber():
    number = random.randint(1,500)

    # Return the random number to be entered into the file
    return number

# The outputNumbers function
def outputNumbers ():
    fileNumber = open('randoms.txt', 'r')

    #Set the accumulators 
    total = 0
    amountOfNum = 0

    # Read the line from the file
    number = fileNumber.readline()

    
    while number !=" ":

        # Add to accumulator
        amountOfNum += 1

        # Convert into integer
        # Could not read from randoms.txt, tried to put path directly into file still would not read
        # Get ValueError
        randomNum = int(number)                             # This is where it wouldn't work

        # Add to accumulator for total
        total += randomNum
        
        # Let the user know the first random number on file
        print(randomNum)
        number = numberFile.readline()

    # Print the total amount of numbers and total added together
    print('The total of the all the numbers is: ' + str(total))
    print('The number of random numbers is: ' + str(amountOfNum))

# The main function 
def main():
    try:
        file = open('randoms.txt', 'w')
        amountOfNum =  int(input('How many numbers should the random file hold?: '))
    except Exception as error:
        print(error)
    else:
        for amount in range(1, amountOfNum+1):
            number = randomNumber()
            file.write(str(number)+ '\n')
    outputNumbers()

            


        

# Call the main function
main()

print('Stephen Oakford')
