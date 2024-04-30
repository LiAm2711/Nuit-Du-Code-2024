import pyxel
import os

class Jeu:
    pyxel.init(256, 256, caption = "Mini JO")
    def __init__(self) -> None:
        pyxel.mouse(True)
        
        self.bouton = Bouton(0, 0, 100, 100, 9, "Test", Accueil)
        self.boutons = [self.bouton]
        
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        print("a")
        for bouton in self.boutons:
            bouton.clique()
    
    def draw(self):
        pyxel.rect(0, 0, 256, 256, 7)
        for bouton in self.boutons:
            bouton.dessiner()

class Accueil:
    def __init__(self):
        self.bouton = Bouton(0, 0, 100, 100, 8, "Test", Jeu)
        self.boutons = [self.bouton]
        pyxel.run(self.update, self.draw)
        
    def update(self):
        print("b")
        for bouton in self.boutons:
            bouton.clique()

    def draw(self):
        pyxel.rect(0, 0, 256, 256, 7)
        for bouton in self.boutons:
            bouton.dessiner()
class Bouton:
    def __init__(self, x, y, w, h, couleur, texte, action = None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.couleur = couleur
        self.texte = texte
        self.action = action
    
    def dessiner(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.couleur)
        pyxel.text(self.w / 2 - 7, self.h / 2 - 5, self.texte, 0)

    def clique(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x > self.x and pyxel.mouse_x < self.x + self.w and pyxel.mouse_y > self.y and pyxel.mouse_y < self.y + self.h:
                if self.action != None:
                    self.action()
                print("cliqué")
Jeu()