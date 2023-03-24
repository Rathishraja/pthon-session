# my_notes = open("file.txt","r")

# print(my_notes.read())

# my_notes.close()

my_notes = open("file.txt","r")

for i in my_notes.readlines():
    print(i)

my_notes.close()
