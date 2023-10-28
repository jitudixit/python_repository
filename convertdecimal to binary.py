#Convert decimal number in binary numbers
def decimalToBinary(number):
    ''' this is function convert decimal number to binary and prints it '''
    if number>1:
        decimalToBinary(number//2)
    print(number%2,end = '')

number = int(input('Enter the any decimal number :'))

decimalToBinary(number)
