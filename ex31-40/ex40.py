class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print("\n")

    def add_more_lyrics(self, add):
        self.lyrics.append(add)

    def print_random(self): #if there is no self then it does not work
        print(9)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print(happy_bday.lyrics)
print("\n")

happy_bday.add_more_lyrics("This is an added line")

happy_bday.sing_me_a_song()

happy_bday.print_random()

bulls_on_parade.sing_me_a_song()
