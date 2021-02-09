# This program takes numbers from the file
# numbers.txt and calculates the average of all
# the numbers stored on the file

# The main function
def main():
   try:
       # Open the file to get the numbers
       file = open('numbers.txt', 'r')

       # Intitialize accumulator 
       total = 0
       lineNumber = 0
       info = file.readline()

       while info != "":

           # Add to the amount of numbers for each pass
           lineNumber += 1

             
           # Read the values from the file
           # and accumulate them
           total += int(info)
           info = file.readline()

       # Calculate average by taking total divided
       # amount of numbers
       average = total/lineNumber
       
    except IOError:
        print('An error occured trying to read the file.')
    except ValueError:
        print('Non-numeric data found in this file.')
        
    else:
        # Print the average
        print('The average is', average)

        # Close the file
        file.close()

# Call the main function        
main()
print('Stephen Oakford')
