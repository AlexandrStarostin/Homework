import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        self._DEGREE_OF_DANGER = Animal._DEGREE_OF_DANGER
        self._cords = [0, 0, 0]
        self.speed = speed

    def get_cords(self):
        return self._cords


    def move(self, dx, dy, dz):
        d = self.speed
        self.dx = dx
        self.dy = dy
        self.dz = dz
        if self.dz * d < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = self.dx * d
            self._cords[1] = self.dy * d
            self._cords[2] = self.dz * d


    def get_cords(self):
        print(f'X: {self._cords[0]} '
              f'\nY: {self._cords[1]} '
              f'\nZ: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self, speed):
        super().__init__(speed)
        # Animal.move.__init__(dz)

    def dive_in(self):
        if self.dz < 0:
            sp = self.speed
            # self.dz / 2
            self._cords[2] = self.dz * sp

    # def abs(self):


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):

    def speak(self):
        print("Click-click-click")



print(Duckbill.__mro__)



db = Duckbill(3)

print(db.live)
print(db.beak)
#
db.speak()
db.attack()
#
db.move(2, 4, -3)
db.get_cords()

db.lay_eggs()




db.dive_in()