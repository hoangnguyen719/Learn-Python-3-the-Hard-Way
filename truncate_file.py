from sys import argv

script, file_to_truncate = argv

open(file_to_truncate, 'w').truncate()
