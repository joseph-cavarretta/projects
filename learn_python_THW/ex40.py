class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy bithday to you.",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song (["They rally round the family",
                        "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

ice_ice_baby = Song(["Alright stop collaborate and listen",
                    "Ice is back with a brand new invention"])

ice_ice_baby.sing_me_a_song()

kashmir = "Oh let the sun beat down upon my face"
LedZep = Song([kashmir])
LedZep.sing_me_a_song()
