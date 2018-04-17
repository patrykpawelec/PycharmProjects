squares = [1, 4, 9, 16, 25]   # create new list
print(squares)a
print(squares[1:4])

animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)
animals += ["monkey", 'dog']    # add two items to the list
print(animals)
animals.append("dino")   # add one more item to the list using append() method
print(animals)
animals[6] = 'dinosaur'
print(animals)

animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # create new list
print(animals)
animals[1:3] = ['cat']    # replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
print(animals)
animals[1:3] = []     # remove 2 items -- 'cat' and 'giraffe' from the list
print(animals)
animals = []
print(animals)

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print(len(alphabet))

# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)
# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)
# Remove key-value pair from phone_book
del phone_book['John']
print(phone_book['Jane'])

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}  # create new dictionary
print(phone_book)
# Add new item to the dictionary
phone_book["Jill"] = 456
print(phone_book)
print(phone_book.keys())
print(phone_book.values())

grocery_list = ["fish", "tomato", 'apples']   # create new list
print("tomato" in grocery_list)    # check that grocery_list contains "tomato" item
grocery_dict = {"fish": 1, "tomato": 6, 'apples': 3}   # create new dictionary
print('fish' in grocery_dict.keys()) #Check if grocery_dict keys contain "fish".
