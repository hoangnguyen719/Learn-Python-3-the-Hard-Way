from sys import argv

script, filename = argv

txt = open(filename)
print(f"The content of the {filename} file is:")
print(txt.read())
txt.close()
