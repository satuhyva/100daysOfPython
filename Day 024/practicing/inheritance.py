class Animal:
    def __init__(self):
        self.num_eyes = 2

    @staticmethod
    def breathe():
        print("Inhale, exhale!")


# Inheriting class Animal


class Fish(Animal):

    def __init__(self):
        super().__init__()

    @staticmethod
    def swim():
        print("Moving in water.")

    def breathe(self):
        super().breathe()
        print("Doing this under water.")


nemo = Fish()
nemo.breathe()
nemo.swim()
