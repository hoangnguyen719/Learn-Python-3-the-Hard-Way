from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?\n") # take in any input

print("Opening the file...")
target = open(filename, 'w') # open filename to target object

print("Truncating the file. Goodbye!")
target.truncate() # truncate (empty) the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3)) # write line1, line2 and line3 in 3 lines
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()
