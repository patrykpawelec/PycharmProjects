for i in range(5):    # for each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # this line is executed 5 times. First time i equals 0, then 1, ...
primes = [2, 3, 5, 7]   # create new list
for prime in primes:
    print(prime)

hello_world = "Hello, World!"
for i in hello_world:    # print each character from hello_world
    print(i)
length = 0      # initialize length variable
for i in hello_world:
    length += 1     # add 1 to the length on each iteration
print(len(hello_world) == length)

square = 1
while square <= 10:
    print(square)    # This code is executed 10 times
    square += 1      # This code is executed 10 times
print("Finished")  # This code is executed once
square = 0
number = 1
while square<81:
    square = number ** 2
    print(square)
    number += 1

count = 0
while True:  # this condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # exit loop if count >= 5
zoo = ["lion", 'tiger', 'elephant']
while True:                         # this condition cannot possibly be false
    animal = zoo.pop()       # extract one element from the list end
    print(animal)
    if animal == 'elephant':
        break           # exit loop

for i in range(5):
    if i == 3:
        continue   # skip the rest of the code inside loop for current i value
    print(i)
for x in range(10):
    if x%2 == 0:
        continue   # skip print(x) for this loop
    print(x)
