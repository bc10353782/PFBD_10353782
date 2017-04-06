#   Brian Cleary 10353782

##  Calculator Functions 
#   1
# Addition funtion, takes inputs and adds together
def add(num1, num2):
    return num1 + num2
#   2
#   Subtraction function, takes inputs and subtracts
def subtract(num1, num2):
    return num1 - num2
#   3
#   Multiplication function, takes inputs and multiplies
def multiply(num1,num2):
    return num1 * num2
#   4
#   Division function, takes inputs and divideds. Will raise an error in num2 is zero
def divide(num1,num2):
    if num2 == 0:
        return 'error'
    return num1 /float(num2)
#   5
#   Exponetial function, takes inputs and raises num1 by power of num2
def exponent(num1,num2):
    return num1 ** num2
#   6
#   Cube function, takes input and cubes num1
def cube(num1):
    return num1 ** 3.0
#   7
#   Square function, takes input and squares num1
def square(num1):
    return num1 ** float(num1)
#   8
#   Square Root function, takes input and gives square root of num1
def sqrt(num1):
    return round((num1 ** .5),2)
#   9
#   Radian function, takes num1 and converts to radians
def rad(num1):
    return round((num1 * 3.1415926536/180),2)
#   10
#   Degree function, takes num1 and converts to degrees
def deg(num1):
    return round((num1 * 180/3.1415926536),2)
   
if __name__ == '__main__': # will only run this section if the file is called from cmd with python in front
    unittest.main()
# Menu for the calculator 
print '''
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exponent
6.Cube
7.Square
8.SquareRoot
9.Radians
10.Degrees

Enter q to quit'''

while True:   
    num1 = raw_input('Please enter first number \n')
    if num1=='q':
            print 'Bye'
            break
    func = raw_input('Please enter function 1,2,3,4,5,6,7,8,9,10 \n')
    if func=='q':
        print 'Bye'
        break
    if func in ['1','2','3','4','5']:   # Splits the functions in to those which require 2 inputs vs those which require 1
        num2 = raw_input('Please enter second number \n')
        if num2=='q':
            print 'Bye'
            break
        if num2 == '0' and func == '4' :
            print 'You cannot divide by zero'  # Error message if trying to divid by Zero
            continue
    try:
        num1 = float(num1)
        if func in ['1','2','3','4','5']:
            num2 = float(num2)
        if func == '1':
            result = add(num1,num2)
        elif func == '2':
            result = subtract(num1,num2)
        elif func == '3':
            result = multiply(num1,num2)
        elif func == '4':
            result = divide(num1,num2)
        elif func == '5':
            result = exponent(num1,num2)
        elif func == '6':
            result = cube(num1)
        elif func == '7':
            result = square(num1)
        elif func == '8':
            result = sqrt(num1)
        elif func == '9':
            result = rad(num1)    
        elif func == '10':
            result = deg(num1)
        else:
            print 'Invalid function'
            continue
    except:
        print 'Please use numbers'
        continue
    print "the answer is {}".format(result)
    if 'y' == raw_input('Do you wish to do another calculation? (y/n)  :\n'):  # Loops to enable user to continue with calculations or quit
        continue
    else:
        break
    