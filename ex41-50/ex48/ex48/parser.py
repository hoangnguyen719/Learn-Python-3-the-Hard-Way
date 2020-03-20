from .lexicon import scan

class ParserException(Exception):
    pass

class Sentence(object):
    def __init__(self, string):
        broken_string = string.lower().replace(',', ';').replace('.', ';').replace('and', ';').split(';')
        self.scanned_string = scan(string)
