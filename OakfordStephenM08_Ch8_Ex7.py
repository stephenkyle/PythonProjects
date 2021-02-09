# This program analyzes characters from
# the file text.txt

# The main function
def main():
    # Open the file named text.txt
    file=open('text.txt', 'r')
    # Read the files contents
    readFile=file.read()
    # Set accumulators to 0
    upper, lower, digit, whitespace = 0,0,0,0
    # Count the characters and add them to the correct accumulator
    for ch in readFile:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            whitespace += 1
    # Output the number of each character
    print('Number of uppercase letters: \t', upper)
    print('Number of lowercase letters: \t', lower)
    print('Number of digits: \t\t', digit)
    print('Number of whitespaces: \t\t', whitespace)

# Call the main function
main()

print('\nStephen Oakford')
