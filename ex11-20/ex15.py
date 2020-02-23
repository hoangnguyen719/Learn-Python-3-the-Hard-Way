from sys import argv

# script, filename = argv
#
# # open a text file and name it txt
# txt = open(filename)
#
# # read the file txt
# print(f"Here's your file {filename}:")
# print(txt.read())
# txt.close()

# open another text file
print("Type the filename again:")
file_again = input("> ")

# read the other text file
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
