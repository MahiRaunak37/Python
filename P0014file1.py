
with open('example1.txt','r') as File1:
    file_stuff = File1.readlines(16)
    print(file_stuff)
    file_stuff = File1.readlines(5)
    print(file_stuff)
    file_stuff = File1.readlines(9)
    print(file_stuff)
