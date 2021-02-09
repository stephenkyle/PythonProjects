#This program troubleshoots a bad Wi-Fi connection

#Display the first solution to troubleshooting
print('Reboot the computer and try to connect.')

#Get the user's feedback
fix = str(input('Did that fix the problem?'))

#If the solution did not work
if fix in['No', 'no', 'N', 'n', 'NO']:
    print('Reboot the router and try to connect.')
    fix = (input('Did that fix the problem?'))
    if fix in['No', 'no', 'N', 'n', 'NO']:
            print('Make sure the cables between the router\nand'
                  'moden are plugged in firmly')
            fix = (input('Did that fix the problem?'))
            if fix in['No', 'no', 'N', 'n', 'NO']:
                print('Move the router to a new location\n'
                      'and try to connect')
                fix = (input('Did that fix the problem?'))
                if fix in['No', 'no', 'N', 'n', 'NO']:
                        print('Get a new router.')

#the Wi-Fi was troubleshooted and no further action required
else:
    exit()

print('Stephen Oakford')
