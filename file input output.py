f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument
for line in f.readlines():   # read lines
    print(line)
f.close()                   # It's important to close the file to free up any system resources.
f1 = open("input1.txt", "r")
print(f1.readline())
f1.close()

zoo = ['lion', "elephant", 'monkey']
if __name__ == "__main__":
    f = open("output.txt", 'a')
    for i in zoo:
        f.write(i)
        f.write(',')
    f.close()

zoo = ['lion', "elephant", 'monkey']
f = open("output.txt", 'w')
for i in zoo:
    f.write(i)
    f.write(',')
f.close()