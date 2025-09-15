from functools import reduce
import asyncio

 # def function_name(parameters):
    # function body

def greet_all():
    print("Hej allihopa!")

def greet_matilda():
    print("Hej Matilda!")

greet_all()
greet_matilda()

# define a function
def greeting():
    print('Hello, world')

# call a function
greeting()

# function arguments - you can add data_type for arguments and return_type
def even_odd(x: int) -> str:
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(even_odd(4))
print(even_odd(3))

def check_tal(x: int) -> str:
    if x > 0:
        return 'Positive'
    elif x < 0:
        return 'Negative'
    else:
        return 'Number is zero'

for i in range(2):
    tal = int(input('Skriv ett tal: '))
    resultat = check_tal(tal)
    print('Resultat: ', resultat)


# types of function arguments
# default argument
def default_args(x, y=10):
    print('x:', x)
    print('y:', y)

default_args(20)

# Använda moms som ett defeault argument. Skapa funktion som räknar ut pris inkl moms

def add_moms(pris, moms=0.25):
    return pris * (1 + moms)

print(add_moms(100))      # använder standard 25% moms
print(add_moms(100, 0.12))  # använder 12% moms istället

# keyword arguments
def student(fname, lname):
    print(fname, lname)

student(fname='John', lname='Doe')

# arbitrary keyword arguments - *args and **kwargs

def order_pizza(size, *toppings):
    if size == 'small':
        price = 80
    elif size == 'medium':
        price = 100
    elif size == 'large':
        price = 120
    else:
        price = 90  # standardpris om storleken inte känns igen
    
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
    print(f"Total price: {price} kr")

size_input = input('Vilken storlek på pizza vill du beställa? (small, medium, large)')
order_pizza(size_input, 'salami', 'olives')


def my_fun(*args):
    print(args)

my_fun(1, 2, 3)
my_fun('a', 'b')

def my_fun2(**kwargs):
    print(kwargs)

my_fun2(name='Jane', age=60)
my_fun2(city='Stockholm', country='Sweden')


# docstring
def print_doc():
    """This text should describe the function
    """
    print(print_doc.__doc__)

print_doc()

# inner function / nested function
def outer_fun():
    s = 'Snakes'
    def inner_fun():
        print(s)
    inner_fun()

outer_fun()

# return - ends function and (opt) returns value 
# anonymous function
def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(7))

# reference value
# if you update a value, it will change outside the function
def ref_fun(x):
    x[0] = 20

li = [10, 11, 12, 13, 14, 15]
ref_fun(li)
print(li)

# if you assign a new value the link to the old object is broken
def ref_fun2(x):
    x = [20, 30, 40]

li = [10, 11, 12, 13, 14, 15]
ref_fun2(li)
print(li)

# recursive functions - a function that calls itself
def countdown(n):
    if n == 0:
        print('Done')
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# calling function from function
def multiply(a, b):
    return a * b

def rectangle_area(width, heigth):
    return multiply(width, heigth)

print(rectangle_area(5, 5))

# map - filter - reduce
# map - adds 10 on every element
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x + 10, numbers))
print(result)

# filter - filters elements that meets condition
result = list(filter(lambda x: x > 3, numbers))
print(result)

# reduce - adds all the numbers togheter
result = reduce(lambda a, b: a + b, numbers)
print(result)

# assigning function to variable
def a():
    print('Python')

snake = a
snake()

# local and global variable
x = 123

def display():
    x = 42
    print(x)
    print(globals()['x'])

print(x)
display()

# async functions
async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"

async def task_main():
    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )
    print("Results:", results)

asyncio.run(task_main())









