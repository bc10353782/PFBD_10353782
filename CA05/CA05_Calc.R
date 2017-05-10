# Program make a simple calculator
# that can add, subtract, multiply
# and divide using functions

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
def exponent(num1,num2):
  return num1 ** num2
# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
selection = as.integer(readline(prompt="Enter choice[1/2/3/4/5]: "))
if selection <= 5 {
  num1 = as.numeric(readline(prompt="Enter first number: "))
  num2 = as.numeric(readline(prompt="Enter second number: "))

  operator <- switch(selection,"+","-","*","/")
  result <- switch(selection, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1, num2))

  print(paste(num1, operator, num2, "=", result))
}
