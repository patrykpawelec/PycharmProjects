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

telemetryConsent
