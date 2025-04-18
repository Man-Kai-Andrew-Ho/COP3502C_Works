from dragon import *

class IceDragon(Dragon):
    def __int__(self, name, image):
        super().__init__(name)
        self.set_image(image)

    def can_breath_fire(self):
        return False
