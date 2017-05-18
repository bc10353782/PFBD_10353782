###  Brian Cleary 10353782


add = lambda x,y :x+y
print add(1, 1)

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F
C = map(celsius, F)
print C

##########################
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]

print map(lambda x,y:x+y, a,b)
print map(lambda x,y,z:x+y+z, a,b,c)
print map(lambda x,y,z:x+y-z, a,b,c)
##############################
       
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

is_even = lambda x: x % 2 ==0
result = filter(is_even, fib)
print result


result = filter(lambda x: x % 2 == 1, fib)
print result

#ret = []
#for x in fib:
#    if x % 2:
#        ret.append(x)

print reduce(lambda x, y: x+y, [47, 11, 42, 13])

max = lambda a,b: a if (a>b) else b
print reduce(max, [47, 11, 42, 13]) 

#   Functions
def max(values):
    return reduce(lambda a,b: a if (a>b) else b, values)
print max([47, 11, 42, 13])

def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values)
print min([47, 11, 42, 13])

def add(values):
    return reduce(lambda a,b: a + b, values)
print add([47, 11, 42, 13])

def sub(values):
    return reduce(lambda a,b: a - b, values)
print  sub([47, 11, 42, 13]) 

def is_even(values):
    return filter(lambda x: x % 2 ==0, values)
print  is_even([47, 11, 42, 13]) 

def is_odd(values):
    return filter(lambda x: x % 2 , values)
print  is_odd([47, 11, 42, 13]) 

def divide(values):
    return reduce(lambda a,b :a/float(b) if (b != 0 and a != 'Nan') else 'Nan' , values)
print  divide([47, 11, 0 ,42, 13, 0])
print  divide([47, 11, 42, 13, 0])
print  divide([47, 11, 42, 13]) 

def multiply(values):
    return reduce(lambda a,b : a*b  , values)
print  divide([47, 11, 42, 13]) 

def to_fahrenheit(values):
    return map(fahrenheit, values)
print to_fahrenheit([0, 37, 40, 100])
    
def to_celsius(values):
    return map(celsius, values)
print to_celsius([0, 32, 100, 212])

def sum(to):
    return reduce(lambda x, y: x+y, range (1, to+1))
print sum(100)
 
 #####################
Celcius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x +32) for x in Celcius ]
print Fahrenheit
#####################################
my_list =[]
for x in Celcius:
    my_list.append ( ((float(9)/5)*x +32) )
# or
my_list = [ fahrenheit(x) for x in Celcius ]
print my_list

print [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) 
        if x**2 + y**2 == z**2]
#Add n as a variable to change to code quickly
n = 30
pyt_tryples =[]
for x in range (1,n):
    for y in range (x,n):
        for z in range(y,n):
            if x**2 + y**2 == z**2:
                pyt_tryples.append((x,y,z))
                
print pyt_tryples                


######
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things        


########################
#       using yields

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
x = city_generator()
print x.next()

print x.next()

print x.next()

print x.next()
#if this lis is uncommented it will cause an error as there are only 4 cities in the list
# #print x.next()


cities = city_generator()
for city in cities:
    print city

###############
def get_triples(n):
    for x in range (1,n):
        for y in range (x,n):
            for z in range(y,n):
                if x**2 + y**2 == z**2:
                    yield (x,y,z)

triplets = get_triples(30)
for triplet in triplets:
    print triplet,
          

##########
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(500)
for x in f:
    print x,
print
print
print


def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print x,
    counter += 1
    if (counter > 10): break 
print
print
print