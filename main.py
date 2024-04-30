import pyxel
import os

class Jeu:
    pyxel.init(256, 256, caption = "Mini JO")
    def __init__(self) -> None:
        pyxel.mouse(True)
        
        self.bouton1 = Rectangle(32, 25, 192, 60, 7,decalageTexteX = 16, decalageTexteY = 4, couleurOmbre = 8)
        self.bouton2 = Rectangle(82, 83, 92, 60, 7,decalageTexteX = 16, decalageTexteY = 4, couleurOmbre = 8)
        self.boutons = [self.bouton1, self.bouton2]
        
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        print("a")
        for bouton in self.boutons:
            bouton.clique()
    
    def draw(self):
        pyxel.rect(0, 0, 256, 256, 11)
        for bouton in self.boutons:
            bouton.dessiner()
        # Titre
        # M
        pyxel.rect(40, 30, 10, 50, 8)
        pyxel.rect(45, 35, 10, 10, 8)
        pyxel.rect(50, 40, 10, 10, 8)
        pyxel.rect(52, 45, 10, 8, 8)
        pyxel.rect(60, 35, 10, 10, 8)
        pyxel.rect(60, 40, 10, 10, 8)
        pyxel.rect(65, 30, 10, 50, 8)
        
        # I
        pyxel.rect(88, 30, 10, 10, 8)
        pyxel.rect(88, 45, 10, 35, 8)
        
        # N
        pyxel.rect(110, 30, 10, 50, 8)
        pyxel.rect(117, 35, 5, 10, 8)
        pyxel.rect(115, 40, 10, 10, 8)
        pyxel.rect(122, 45, 5, 10, 8)
        pyxel.rect(125, 50, 5, 10, 8)
        pyxel.rect(127, 55, 5, 10, 8)
        pyxel.rect(130, 60, 10, 10, 8)
        pyxel.rect(132, 65, 5, 10, 8)
        pyxel.rect(135, 30, 10, 50, 8)
        
        # I
        pyxel.rect(157, 30, 10, 10, 8)
        pyxel.rect(157, 45, 10, 35, 8)
        
        # S
        pyxel.rect(180, 30, 35, 10, 8)
        pyxel.rect(180, 30, 10, 20, 8)
        pyxel.rect(180, 50, 35, 10, 8)
        pyxel.rect(205, 60, 10, 20, 8)
        pyxel.rect(180, 70, 35, 10, 8)
        
        # J
        pyxel.rect(89, 88, 34, 10, 8)
        pyxel.rect(101, 88, 10, 50, 8)
        pyxel.rect(89, 128, 15, 10, 8)
        
        # O
        pyxel.rect(128, 88, 10, 50, 8)
        pyxel.rect(128, 88, 38, 10, 8)
        pyxel.rect(128, 128, 38, 10, 8)
        pyxel.rect(156, 88, 10, 50, 8)
        
class Accueil:
    def __init__(self):
        self.bouton = Rectangle(0, 0, 100, 100, 8, texte = "Test", action = Jeu)
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
class Rectangle:
    def __init__(self, x, y, w, h, couleur, texte = None, decalageTexteX = 5, decalageTexteY = 5, action = None, couleurOmbre = None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.couleur = couleur
        self.couleurOmbre = couleurOmbre
        self.texte = texte
        self.decalageTexteX = decalageTexteX
        self.decalageTexteY = decalageTexteY
        self.action = action
    
    def dessiner(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.couleur)
        if self.couleurOmbre is not None:
            pyxel.rectb(self.x, self.y, self.w, self.h, self.couleurOmbre)
            pyxel.rectb(self.x + 1, self.y + 1, self.w - 2, self.h - 2, self.couleurOmbre)
            
        if self.texte:
            pyxel.text((self.w / 2) + self.x - self.decalageTexteX, (self.h / 2) + self.y - self.decalageTexteY, self.texte, 0)

    def clique(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if pyxel.mouse_x > self.x and pyxel.mouse_x < self.x + self.w and pyxel.mouse_y > self.y and pyxel.mouse_y < self.y + self.h:
                if self.action != None:
                    self.action()
                print("cliqué")
Jeu()