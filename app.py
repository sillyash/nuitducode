import pyxel
from elements import Car, Player
class App:
    def __init__(self):
        pyxel.init(1920, 1080,title="Sniper",fps=60,quit_key=pyxel.KEY_NONE,display_scale=4)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x +=1

    def draw(self):
        pyxel.cls(0)

App()