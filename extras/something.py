'''
# Example of using higher-order functions in Python  
# Function that adds 1 to the passed value (x)  
def add(x=0):
    return x+1
# Function that multiplies the passed value (x) by 2  
def mul(x=0):
    return x**2
# Function that subtraction the passed value (x) by 3  
def sub(x=0):
    return x-3
x = 20
z = sub(x)
p = add(x)
q = mul(x)
print(f"the value of the function'add' is {p}")
print(f"The value of the function 'mul' is {q}")
print(f"The value of the function 'sub' is {z}")
'''
'''
#LAMBDA
# Example of using lambda functions in Python  
# Lambda function that adds 1 to x  
# An anonymous function refers to a function declared with no name.
add = lambda x:x+1
mul = lambda x:x*2
sub = lambda x:x-3
r1 = add(5)
r2 = mul(5)
r3 = sub(5)
print(f"The value of the add is {r1}")
print(f"The value od mul is {r2}")
print(f"The value of the sub is {r3}")
'''
'''
d2 =list(range(100))
print(d2)
#d1 = [1, 2, 3, 4, 5]
def mul(x):
    for n in x:
        print((n**2))
mul(d2)
'''

# Using the map to apply a function to each element  
# Lambda function returns the square of x
'''
data = list(range(10))
result1 = map(lambda x:x**2,data)
print(list(result1))
print(type(result1))

#data = list(range(10))
result2 = map(lambda x:x**3,data)
print(list(result2))
print(type(result2))
'''
'''
def add(n):
    return n + n
def mul (n):
    return n**n

data =(1,2,3,4,5)

result1 = map(add,data)
print(list(result1))

result2 = map(mul,data)
print(list(result2))
'''
l = ['star','space','neuton']
r2 = list(map(list,l))
print(r2)


