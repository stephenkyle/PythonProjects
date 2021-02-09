# This program reads the contents of two file and
# displays whether the names were among the most popular
# for the years 2000-2009

# The checkBoy function
def checkBoy(nameGiven):
    status = 0
    # Open file named BoyNames
    infile = open('BoyNames.txt', 'r')
    boyNames = infile.readlines()
    infile.close()
    index = 0
    # Strip the \n from each element
    while index < len(boyNames):
        boyNames[index] = boyNames[index].rstrip('\n')
        index+=1
    # Check to see if name is in list
    if nameGiven in boyNames:
        status = 1
    else:
        status = 0
    # Return the status
    return status

# The checkGirl function        
def checkGirl(nameGiven):
    status = 0
    # Open file named GirlNames
    infile = open('GirlNames.txt', 'r')
    girlNames = infile.readlines()
    infile.close()
    index = 0
    # Strip the \n from each element
    while index < len(girlNames):
        girlNames[index] = girlNames[index].rstrip('\n')
        index+=1
    # Check to see if name is in list
    if nameGiven in girlNames:
        status = 1
    else:
        status = 0
    # Return the status
    return status

# The main function
def main():
    # Get user's name input
    nameGiven = str(input('Please enter a name to check: '))
    # Call the checkBoy function
    status = checkBoy(nameGiven)
    if status == 1:
        print(nameGiven, "is a popular boy's name!")
    else:
        print(nameGiven, "is not a popular boy's name.")
    # Call the checkGirl function    
    status = checkGirl(nameGiven)
    # Check to see if popular girl name
    if status == 1:
        print(nameGiven, "is a popular girl's name!")
    else:
        print(nameGiven, "is not a popular girl's name.")
        
# Call the main function
main()

print('')
print('Stephen Oakford')
