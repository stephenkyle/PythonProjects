# This program accepts two integers and
# outputs whichever number is larger


# The main function
def main():
    #Get user's input information
    first_num = int(input('What is the first number?'))
    sec_num = int(input('What is the second number?'))

    #Get the answer 
    answer = max(first_num, sec_num)

    #Determine if answer is equal to one or two
    if answer == 1:

        #Output the greater number
        print(first_num, 'is the greater number')
    else:
        print(sec_num, ' is the greater number')

        
def max(num1, num2):
    # determine if the first number is greater or not
    if num1>num2:
        return 1
    else:
        return 2

# Call the main function    
main()

print('Stephen Oakford')
