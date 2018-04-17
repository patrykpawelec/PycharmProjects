hello = "Hello"
world = 'World'
hello_world = hello+' '+world
print(hello_world)      # Note: you should print "Hello World"

hello = "hello"
ten_of_hellos = hello * 10
print(ten_of_hellos)

python = "Python"
print("h " + python[3])     # Note: string indexing starts with 0
p_letter = python[0]
print(p_letter)

long_string = "This is a very long string!"
exclamation = long_string[-1]
print(exclamation)

monty_python = "Monty Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:]
print(python)

ice_cream = "ice cream"
print("cream" in ice_cream)    # print boolean result directly
contains = 'ice' in ice_cream
print(contains)

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
print(first_half)

dont_worry = "Don't worry about apostrophes"
print(dont_worry)
print("\"Sweet\" is an ice-cream")
print('The name of this ice-cream is "Sweet\'n\'Tasty"')

monty_python = "Monty Python"
print(monty_python)
print(monty_python.lower())    # print lower-cased version of the string
print(monty_python.upper())
print(monty_python[int(len(monty_python)/2)].lower())

name = "Patriko"
print("Hello, PyCharm! My name is %s!" % name)     # Note: %s is inside the string, % is after the string
print("I'm %d years old" % 30)
