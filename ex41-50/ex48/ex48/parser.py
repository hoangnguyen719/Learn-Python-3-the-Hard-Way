from .lexicon import scan
import re

class ParserException(Exception):
    pass

class Sentence(object):
    """
    <class Sentence> object needs to have keywords in format:
        [Subject] Verb [Number] Object
    with Subject and Number being optional.
    """
    def __init__(self, string):
        # default error messages
        length_message = "Incorrect number of keywords: {} was given (2 to 4 required)"
        error_message = "Error keyword: {}"
        format_message = "Incorrect keyword format:\n\t(given): {}\n\t(required): {}"
        format_default = "[Noun], Verb, [Number,] Noun"

        player='player'
        self.string = string
        self.word_list = [word for word in scan(string) if word[0] != 'stop']
        self.word_list_key = [word[0] for word in self.word_list]
        self.word_list_value = [word[1] for word in self.word_list]

        if (len(self.word_list) < 2) or (len(self.word_list) > 4):
            raise ParserException(length_message.format(len(self.word_list)))
        else:
            if any([key=='error' for key in self.word_list_key]):
                error_index = self.word_list_key.index('error')
                raise ParserException(error_message.format(self.word_list_value[error_index]))
            else:
                self.obj = ""
                if self.word_list_key == ['verb', 'noun']:
                    self.subj = player
                elif self.word_list_key == ['noun', 'verb', 'noun']:
                    self.subj = self.word_list_value[0]
                elif self.word_list_key == ['verb', 'number', 'noun']:
                    self.subj = player
                    self.obj = str(self.word_list_value[1]) + " "
                elif self.word_list_key == ['noun', 'verb', 'number', 'noun']:
                    self.subj = self.word_list_value[0]
                    self.obj = str(self.word_list_value[2]) + " "
                else:
                    raise ParserException(format_message.format(", ".join(self.word_list_key), format_default))
                self.verb = [word[1] for word in self.word_list if word[0] == 'verb'][0]
                self.obj += self.word_list_value[-1]
                self.sentence = " ".join([self.subj, self.verb, self.obj])

    def print(self):
        print(self.sentence)