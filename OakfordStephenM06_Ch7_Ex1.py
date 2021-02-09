# This program gets the store's sales for each day of the
# week and calculates the total sales for the week

# The enterDailySales function
def enterDailySales(weekDay):
    # Create an empty list
    salesOfTheDay = []
    # Add the amount of sales for the for the day into the list
    for dayOfWeek in weekDay:
            print('Enter the sales for', dayOfWeek + ": ", end ='')
            soldDay = float(input())
            salesOfTheDay.append(soldDay)
    # Return the sales of the day 
    return salesOfTheDay

# The calculateWeekly function
def calculateWeekly(salesOfTheDay):
    #Set accumulator
    total = 0
    # Calculate total amount of sales for week
    for saleDay in range(len(salesOfTheDay)):
        total += salesOfTheDay[saleDay]
    # Return total amount of sales
    return total    

# The printReport function
def printReport(weekDay, salesOfTheDay, totalSales):
    for currentDay in range (len(weekDay)):
        # Print the day and the amount of sales for that day
        print( weekDay[currentDay] + ' sales: ',
               salesOfTheDay[currentDay])
    # Print the total amount of sales for the week    
    print('Weekly Sales: ', totalSales)
        
# The main function
def main():
    # Create a list of the days of the week
    weekDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday',
               'Saturday', 'Sunday']
    # Set the result of enterDailySales to variable salesOfTheDay
    salesOfTheDay = enterDailySales(weekDay)
    # Set the result of calculateWeekly to variable totalSales
    totalSales = calculateWeekly(salesOfTheDay)
    # Call the printReport function
    printReport(weekDay, salesOfTheDay, totalSales)
    
# Call the main function
main()


print('Stephen Oakford')
