class Bird:
    def __init__(self):
        self.hungry=True


    def eat(self):
        if self.hungry:
            print("AHAHAHAH")
        else:
            print("NO thanks")



class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound="squawk"

    def sing(self):
        print(self.sound)
