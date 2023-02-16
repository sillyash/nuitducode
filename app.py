import pyxel
from elements import Car, Player

voiture = Car(0,100,32,16,10)
joueur = Player()

class App:
    def __init__(self):
        pyxel.init(300, 200,title="Sniper",fps=60,quit_key=pyxel.KEY_NONE,display_scale=4)
        pyxel.run(self.update, self.draw)

    def update(self):
        voiture.move()
        joueur.fire(voiture)

    def draw(self):
        pyxel.cls(0)
        voiture.draw()
        joueur.draw_visor()

App()