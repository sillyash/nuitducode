import pyxel
import time

class Car:
    def __init__(self,x,y,w,h,life):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.life = life
    
    def move(self):
        self.x += 1 

    def draw(self):
        if self.life > 0:
            pyxel.rect(self.x,self.y,self.w,self.h,7)

class Player:
    def __init__(self):
        self.tir = False

    def update(self):
        self.fire(voiture)
        voiture.move()
        print(voiture.life)

    def visor(self):
        pyxel.circb(pyxel.mouse_x,pyxel.mouse_y, 8, 9)
        if self.tir:
            pyxel.pset(pyxel.mouse_x,pyxel.mouse_y, 9)

    def fire(self,target):
        self.tir = pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)
        if self.tir and self.hit(target):
            target.life -= 1

    def hit(self,target):
        return pyxel.mouse_x > target.x and pyxel.mouse_y > target.y and\
        pyxel.mouse_x < target.x + target.w and\
        pyxel.mouse_y < target.y + target.h
