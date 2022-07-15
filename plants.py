import arcade
import animate

class Sun(arcade.Sprite):
    def __init__(self):
        super().__init__('plants/sun1.png', 0.2)

class Pea(animate.Animate):
    def __init__(self):
        super().__init__('plants/pea1.png', 0.2)
        self.frames = 3
        for i in range(1, self.frames):
            self.append_texture(arcade.load_texture(f"plants/pea{i}.png"))

class Nut(arcade.Sprite):
    def __init__(self):
        super().__init__('plants/nut1.png', 0.2)

class Tree(arcade.Sprite):
    def __init__(self):
        super().__init__('plants/tree1.png', 0.2)
