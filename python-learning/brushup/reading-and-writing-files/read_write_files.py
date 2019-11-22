# Here in this example we are going to read from a file and then the read string will be written back to another file

from sys import argv

script, filename = argv

print(f"we are going to erase {filename}")
print("If you don't want that then press CTRL + C")
print("If you do not want that then hit RETURN")

input("? ")

print("Opening the file")
target = open(filename, 'w')  # w stands for writing permission for the opened file

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you three lines, those three lines will be written in the file ")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("Writing to the file is done, now finally we are going to close the file.")
target.close()
