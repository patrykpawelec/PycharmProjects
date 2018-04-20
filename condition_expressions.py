name = "John"
age = 17
print(name == "John" or age == 17)    # checks that either name equals to "John" OR age equals to 17
print(name == "John" and age != 23)
print(name == "John" and not age == 23)

name = "John"
age = 17
print(name == "John" or not age > 17)
print(name == "John" or not age > 17)
print(name == "Ellis" or not (name == "John" and age == 17 ))

name = "John"
age = 17
if name == "John" or age == 17:   # check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")
tasks = ['task1', 'task2']    # create new list
if len(tasks) == 0:
    print("empty")

x = 28
if x < 0:
    print('x < 0')                      # executes only if x < 0
elif x == 0:
    print('x is zero')                 # if it's not true that x < 0, check if x == 0
elif x == 1:
    print('x == 1')                    # if it's not true that x < 0 and x != 0, check if x == 1
else:
    print('non of the above is true')
name = "John"
if name == "John":
    print(True)
else:
    print(False)

