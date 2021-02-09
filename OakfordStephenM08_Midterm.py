# This program inputs a sentence word by 
# word into a list

# The main function
def main():
    # Create an empty list
    sentence=[]
    # Get the user's input of the first element in the list
    inputString = input('What is the first word you would like to input?')
    # Capitalize the first word of the sentence
    inputString = inputString.capitalize()
    # Add the first word to the list
    sentence.append(inputString)
    # Access the loop conditions
    nextWord = input('Would you like to add another word to the sentence?'
                   '\nPlease enter "y" for yes or anthing else for no.')
    while nextWord == 'y':
        # Get the user's next element in the list
        insertWord = input('\nWhat is the next word you would like to input?')
        # Add the next word to the list
        sentence.append(insertWord)
        # Loop controller
        nextWord = input('Would you like to add another word to the sentence?'
                   '\nPlease enter "y" for yes or anthing else for no.')
    # Check the size of the list     
    size = len(sentence)
    # Output the list but without the brackets and commas
    print(*sentence, '.')
    # Output the size of the list
    print('There are', size, 'words in the sentence.')





# Call the main function
main()


