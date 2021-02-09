# This program takes the recorded data
# from steps.txt and calculates how m

def main():
    file = open('steps.txt')
    totalJan = 0
    totalFeb = 0
    totalMar = 0
    totalApr = 0
    totalMay = 0
    totalJun = 0
    totalJul = 0
    totalAug = 0
    totalSep = 0
    totalOct = 0
    totalNov = 0
    totalDec = 0
    steps = file.readline()
    days = 0
    while steps != '':
        days += 1
        if days <= 31:
            totalJan += int(steps) 
            steps = file.readline()

        
        elif days <= 59:
            totalFeb += int(steps)
            steps = file.readline()
     
        elif days <= 90:
            totalMar += int(steps)
            steps = file.readline()
        
        elif days <= 120:
            totalApr += int(steps)
            steps = file.readline()
      
        elif days <= 151:
            totalMay += int(steps)
            steps = file.readline()
        
        elif days <= 181:
            totalJun += int(steps)
            steps = file.readline()
        
        elif days <= 212:
            totalJul += int(steps)
            steps = file.readline()
        
        elif days <= 243:
            totalAug += int(steps)
            steps = file.readline()
        
        elif days <= 273:
            totalSep += int(steps)
            steps = file.readline()
      
        elif days <= 304:
            totalOct += int(steps)
            steps = file.readline()
        
        elif days <= 334:
            totalNov += int(steps)
            steps = file.readline()
       
        else:
            totalDec += int(steps)
            steps = file.readline()
            

    print('The average amount of steps taken for')        
    print('January:\t', format(totalJan, ','))
    print('February:\t', format(totalFeb, ','))
    print('March:\t\t', format(totalMar, ','))
    print('April:\t\t', format(totalApr, ','))
    print('May:\t\t', format(totalMay, ','))
    print('June:\t\t', format(totalJun, ','))
    print('July:\t\t', format(totalJul, ','))
    print('August:\t\t', format(totalAug, ','))
    print('September:\t', format(totalSep, ','))
    print('October:\t', format(totalOct, ','))
    print('November:\t', format(totalNov, ','))
    print('December:\t', format(totalDec, ','))

main()
