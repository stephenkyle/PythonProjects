def main():
    for newNumber in range(1, 101):
        if is_prime(newNumber):
            print(newNumber)

def is_prime(number):
    remainders = 0
    if number==1:
        return False
    for newNumber in range(1, number+1):
        if number % newNumber == 0:
            remainders = remainders + 1
            if remainders > 2:
                return False
    return True 

main()

print('Stephen Oakford')
