# Program make a simple calculator that can add, subtract, multiply and divide using functions

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  return(x / y)
}

exponent <- function(x,y){
  return(x**y)
}
#print (exponent(3,3))
#6
cube <- function(x){
  return(x**3.0)
}
#print (cube(4))
#7
square <- function(x){
  return(x*x)
}
print (square(3*x))
#8
squareroot <- function(x){
  return(sqrt(x))  
}
#9    
rad <- function(x){
  return(x * 3.1415926536/180)
}
#10
degree <- function(x){
  return(x* 180/3.1415926536)      
}


# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Cube")
print("7.Square")
print("8.Squareroot")
print("9.Radian")
print("10.Degree")

selection = as.integer(readline(prompt="Enter choice 1 ,2, 3, 4, 5, 6, 7, 8, 9, 10         :   "  ))
num1 = as.numeric(readline(prompt="Enter first number: "))
if (selection <= 5) {
  num2 = as.numeric(readline(prompt="Enter second number: "))
}  
operator <- switch(selection,"+","-","*","/","Exp","Cube","Square","Squareroot","Radian","Degree")
result <- switch(selection, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), 
                 exponent(num1, num2), cube(num1), square(num1), squareroot(num1), rad(num1), degree(num1))
if (selection <= 5) {
  print(paste(num1, operator, num2, "=", result))
} else
  print(paste(num1, operator, "=", result))

