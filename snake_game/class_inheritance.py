class Animal:
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("we are doing this under the water")

    def swim(self):
        print("moving in the water")


nemo = Fish()
nemo.breath()
