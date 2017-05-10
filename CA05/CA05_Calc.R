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
print (exponent(3,3))

cube <- function(x){
  return(x**3.0)
}
print (cube(4))

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Cube")

selection = as.integer(readline(prompt="Enter choice 1 ,2, 3, 4, 5, 6        :   "  ))
if (selection <= 5) {
  num1 = as.numeric(readline(prompt="Enter first number: "))
  num2 = as.numeric(readline(prompt="Enter second number: "))

  operator <- switch(selection,"+","-","*","/","Exp","Cube")
  result <- switch(selection, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1, num2), cube(num))

  print(paste(num1, operator, num2, "=", result))
} else if (selection > 5) {
  num = as.numeric(readline(prompt="Enter number: "))
  
  operator <- switch(selection,"+","-","*","/","Exp","Cube")
  result <- switch(selection, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1, num2), cube(num))
  
  print(paste(num, operator, "=", result))
}  
#  def cube(num1):
#    return num1 ** 3.0
    #   Square function, takes input and squares num1
#  def square(num1):
#    return num1 ** float(num1)
    #   Square Root function, takes input and gives square root of num1
#  def sqrt(num1):
#    return round((num1 ** .5),2)
    #   Radian function, takes num1 and converts to radians
#  def rad(num1):
#    return round((num1 * 3.1415926536/180),2)
    #   Degree function, takes num1 and converts to degrees
#  def deg(num1):
#    return round((num1 * 180/3.1415926536),2)
  
  