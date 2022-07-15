import arcade
import random
import time
import animate
import plants
import zombies

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants vs Zombies"

class Menu_vertical(arcade.Sprite):
    def __init__(self):
        super().__init__('textures/menu_vertical.png', 0.1)
        self.center_x = 60
        self.center_y = 290

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("textures/background.jpg")
        self.pea = plants.Pea()
        self.sun = plants.Sun()
        self.nut = plants.Nut()
        self.tree = plants.Tree()
        self.zom = zombies.Zom()
        self.cone = zombies.Cone()
        self.buck = zombies.Buck()
        self.menu_vertical = Menu_vertical()
        self.pea = arcade.SpriteList()

    def on_draw(self):
        self.clear((0, 0, 0))
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.pea.draw()
        self.sun.draw()
        self.nut.draw()
        self.tree.draw()
        self.menu_vertical.draw()
        self.zom.draw()
        self.cone.draw()
        self.buck.draw()

    def update(self, delta_time):
        self.pea.update()
        self.sun.update()
        self.nut.update()
        self.tree.update()
        self.zom.update()
        self.cone.update()
        self.buck.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if 16 <= x <=116:
            print(y)
            if 370 <= y <= 480:
                print('SunFlower')
            if 250 <= y <= 360:
                print('pea')
            if 130 <= y <= 240:
                print('nut')
            if 10 <= y <= 115:
                print('tree')


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()