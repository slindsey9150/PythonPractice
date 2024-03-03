def doComplexMath():
    print("we're doing more complex math now")
    whatComplexMath = input('What type of complex math would you like to do?')
    if whatComplexMath.lower() == "exponent":
        print('Exponent')
    
def addition ():
    firstNumber = int(input('we\'re going to do some addition. type a number: '))
    secondNumber = int(input('type another number: '))
    print (firstNumber + secondNumber)
    doMath()
  
def subtraction ():
    firstNumber = int(input('we\'re going to do some subtraction. type a number: '))
    secondNumber = int(input('type another number: '))
    print (firstNumber - secondNumber) 
    doMath()
  
def multiplication () :
    firstNumber = int(input('we\'re going to do some multiplication. type a number: '))
    secondNumber = int(input('type another number: '))
    print (firstNumber * secondNumber) 
    doMath()
  
def division () :
    firstNumber = int(input('we\'re going to do some division. type a number: '))
    secondNumber = int(input('type another number: '))
    print (firstNumber / secondNumber)
    doMath() 

def doMath  () :
    startMath = input('Would you like to do some basic math? ')
    if startMath.lower() == 'yes':  
        print('alright let\'s do some math!')
        whatMath = input("""
What type of math would you like to do? 
(addition, subtraction, multiplication, or division): """)
        if whatMath.lower() == 'subtraction':
            subtraction()
        if whatMath.lower() == 'addition':
            addition()
        if whatMath.lower() == 'division':
            division()
        if whatMath.lower() == 'multiplication':
            multiplication()
        
    if startMath.lower() == 'no':
        print('Well would you like to do some more complex math? ')
        complexMath = input('Yes or No: ')
        if complexMath.lower() == 'yes':
            doComplexMath()
        if complexMath.lower() == 'no':
            print("alright. no math for right now")
    
doMath()


   

