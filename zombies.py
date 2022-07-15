import arcade
import animate

class Zom(arcade.Sprite):
    def __init__(self):
        super().__init__('zombies/zom1.png', 0.2)

class Cone(arcade.Sprite):
    def __init__(self):
        super().__init__('zombies/cone1.png', 0.2)

class Buck(arcade.Sprite):
    def __init__(self):
        super().__init__('zombies/Buck1.png', 0.2)