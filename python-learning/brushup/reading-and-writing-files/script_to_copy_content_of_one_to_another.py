# Now we are going to write a python script to copy content of one file to another

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying form {from_file} to {to_file}")

# we could do those two in one line
in_file = open(from_file)
in_data = in_file.read()

print(f"The input file data is {len(in_data)} bytes long")

print(f"Does the output file exists ? {exists(to_file)}")
print("Ready, hit RETURN to start copying, CTRL + C to cancel the operation")

input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done")

out_file.close()
in_file.close()
