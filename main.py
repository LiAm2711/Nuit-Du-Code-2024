import pyxel
from math import sqrt
import os

# ==================================== PAGES ====================================
class Accueil:
    pyxel.init(256, 256, caption = "Mini JO")
    def __init__(self) -> None:
        pyxel.mouse(True)
        
        # =============== RECTANGLES ===============
        self.rectangle1 = Rectangle(32, 25, 192, 60, 7,decalageTexteX = 16, decalageTexteY = 4, couleurOmbre = 8)
        self.rectangle2 = Rectangle(82, 83, 92, 60, 7,decalageTexteX = 16, decalageTexteY = 4, couleurOmbre = 8)
        self.rectangle3 = Rectangle(33, 150, 90, 30, 7,decalageTexteX = 16, decalageTexteY = 4, couleurOmbre = 8, action = PingPong, texte = "Ping-Pong")
        self.rectangle4 = Rectangle(132, 150, 90, 30, 7,decalageTexteX = 27, decalageTexteY = 4, couleurOmbre = 8, action = Corde, texte = "Tir a la corde")        
        self.rectangle5 = Rectangle(33, 190, 190, 30, 7,decalageTexteX = 30, decalageTexteY = 4, couleurOmbre = 8, action = Lancer, texte = "Lancer de poids")      
        self.rectangles = [self.rectangle1, self.rectangle2, self.rectangle3, self.rectangle4, self.rectangle5]
        
        # =============== ELEMENTS FONDS ===============
        self.lune_menu = Soleil_lune (20, 20, 10, 7, 6)
        self.etoile_menu = [Etoile(78,26,7),Etoile(63,68,7),Etoile(36,110,7),Etoile(126,105,7),Etoile(118,67,7),Etoile(184,39,7),Etoile(142,16,7),Etoile(184,104,7),Etoile(173,83,7),Etoile(218,75,7)]
        
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        for rectangle in self.rectangles:
            rectangle.clique()
    
    def draw(self):
        # =============== FOND ===============
        pyxel.rect(0,0,256,256,1)
        pyxel.circ(256,1350,1220,15)
        pyxel.circ(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r, self.lune_menu.coul_i)
        pyxel.circb(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r, self.lune_menu.coul_e)
        pyxel.circb(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r - 1, self.lune_menu.coul_e)
        pyxel.circ(self.lune_menu.x - 8, self.lune_menu.y, self.lune_menu.r - 1, 1)

        for etoile in self.etoile_menu:
            pyxel.pset(etoile.x, etoile.y, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y - 1, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y + 1, etoile.coul)
            pyxel.pset(etoile.x + 2, etoile.y , etoile.coul)
        
        # =============== RECTANGLES ===============
        for rectangle in self.rectangles:
            rectangle.dessiner()
            
        # =============== TITRE ===============
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
class Corde:
    def __init__(self):
        # =============== RECTANGLES ===============
        self.rectangle1 = Rectangle(5, 5, 40, 15, 7, "Accueil", 13, 2, Accueil, 8)
        self.rectangles = [self.rectangle1]
        
        # =============== ELEMENTS FONDS ===============
        self.nuage_jeux_de_corde_1 = Nuage(50,100, 7, 6)
        self.nuage_jeux_de_corde_2 = Nuage(175,75, 7, 6)
        self.nuage_jeux_de_corde_3 = Nuage(121,113, 7, 6)
        self.joueur1 = Joueur(234,242,7,4)
        self.joueur2 = Joueur(14,242,7,4)
        self.soleil_jeux_corde = Soleil_lune(190, 25, 15, 10, 9)
        
        # =============== ELEMENTS JEU ===============
        self.corde_rouge = [128, 236, 323, 236, 8]
        self.corde_bleu = [-100, 236, 128, 236, 1]
        self.pilier_bleu = [77, 239, 3, 11, 9]
        self.pilier_rouge = [178, 239, 3, 11, 9]
        self.milieu = [125, 236, 6, 1, 7]
        
        self.fin = False
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if not self.fin:
            if pyxel.btnp(pyxel.KEY_A):
                self.corde_rouge[0] -= 10
                self.corde_bleu[2] -= 10
                self.milieu[0] -= 10
            
            if pyxel.btnp(pyxel.KEY_P):
                self.corde_rouge[0] += 10
                self.corde_bleu[2] += 10
                self.milieu[0] += 10
        
            if self.corde_rouge[0] >= self.pilier_rouge[0]:
                print('a')
                self.fin = "Rouge"
            elif self.corde_bleu[2] <= self.pilier_bleu[0]:
                self.fin = "Bleu"
        
        for rectangle in self.rectangles:
            rectangle.clique()
    
    def draw(self):
        # =============== FOND ===============
        pyxel.rect(0,0,256,256,6)
        pyxel.circ(256,1350,1220,11)
        pyxel.rect(10,250,230,120,4)
        pyxel.rectb(10,250,230,120,0)
        pyxel.line(self.joueur1.x, self.joueur1.y - 11, self.joueur1.x - 11, self.joueur1.y - 4, self.joueur1.coul_bras)
        pyxel.circ(self.joueur1.x, self.joueur1.y, 7, self.joueur1.coul)
        pyxel.circ(self.joueur1.x, self.joueur1.y - 11, 5, self.joueur1.coul)
        pyxel.circ(self.joueur1.x, self.joueur1.y - 19, 3, self.joueur1.coul)
        pyxel.line(self.joueur1.x, self.joueur1.y - 11, self.joueur1.x - 11, self.joueur1.y - 8, self.joueur1.coul_bras)

        pyxel.line(self.joueur2.x, self.joueur2.y - 11, self.joueur2.x + 11, self.joueur2.y - 4, self.joueur2.coul_bras)
        pyxel.circ(self.joueur2.x, self.joueur2.y, 7, self.joueur2.coul)
        pyxel.circ(self.joueur2.x, self.joueur2.y - 11, 5, self.joueur2.coul)
        pyxel.circ(self.joueur2.x, self.joueur2.y - 19, 3, self.joueur2.coul)
        pyxel.line(self.joueur2.x, self.joueur2.y - 11, self.joueur2.x + 11, self.joueur2.y - 8, self.joueur2.coul_bras)

        pyxel.circ(self.soleil_jeux_corde.x, self.soleil_jeux_corde.y, self.soleil_jeux_corde.r, self.soleil_jeux_corde.coul_i)
        pyxel.circb(self.soleil_jeux_corde.x, self.soleil_jeux_corde.y, self.soleil_jeux_corde.r, self.soleil_jeux_corde.coul_e)
        pyxel.circb(self.soleil_jeux_corde.x, self.soleil_jeux_corde.y, self.soleil_jeux_corde.r - 1, self.soleil_jeux_corde.coul_e)
        
        pyxel.circ(self.nuage_jeux_de_corde_1.x, self.nuage_jeux_de_corde_1.y, self.nuage_jeux_de_corde_1.r, self.nuage_jeux_de_corde_1.coul)
        pyxel.circ(self.nuage_jeux_de_corde_1.x + 5, self.nuage_jeux_de_corde_1.y - 2, self.nuage_jeux_de_corde_1.r, self.nuage_jeux_de_corde_1.coul)
        pyxel.circ(self.nuage_jeux_de_corde_1.x + 11, self.nuage_jeux_de_corde_1.y, self.nuage_jeux_de_corde_1.r, self.nuage_jeux_de_corde_1.coul)
        pyxel.circ(self.nuage_jeux_de_corde_1.x + 16, self.nuage_jeux_de_corde_1.y - 2, self.nuage_jeux_de_corde_1.r, self.nuage_jeux_de_corde_1.coul)
        pyxel.circ(self.nuage_jeux_de_corde_2.x, self.nuage_jeux_de_corde_2.y, self.nuage_jeux_de_corde_2.r, self.nuage_jeux_de_corde_2.coul)
        pyxel.circ(self.nuage_jeux_de_corde_2.x + 5, self.nuage_jeux_de_corde_2.y - 2, self.nuage_jeux_de_corde_2.r, self.nuage_jeux_de_corde_2.coul)
        pyxel.circ(self.nuage_jeux_de_corde_2.x + 11, self.nuage_jeux_de_corde_2.y, self.nuage_jeux_de_corde_2.r, self.nuage_jeux_de_corde_2.coul)
        pyxel.circ(self.nuage_jeux_de_corde_2.x + 16, self.nuage_jeux_de_corde_2.y - 2, self.nuage_jeux_de_corde_2.r, self.nuage_jeux_de_corde_2.coul)
        pyxel.circ(self.nuage_jeux_de_corde_3.x, self.nuage_jeux_de_corde_3.y, self.nuage_jeux_de_corde_3.r, self.nuage_jeux_de_corde_3.coul)
        pyxel.circ(self.nuage_jeux_de_corde_3.x + 5, self.nuage_jeux_de_corde_3.y - 2, self.nuage_jeux_de_corde_3.r, self.nuage_jeux_de_corde_3.coul)
        pyxel.circ(self.nuage_jeux_de_corde_3.x + 11, self.nuage_jeux_de_corde_3.y, self.nuage_jeux_de_corde_3.r, self.nuage_jeux_de_corde_3.coul)
        pyxel.circ(self.nuage_jeux_de_corde_3.x + 16, self.nuage_jeux_de_corde_3.y - 2, self.nuage_jeux_de_corde_3.r, self.nuage_jeux_de_corde_3.coul)
        
        pyxel.rect(12, 225, 5, 2, 1)
        pyxel.rect(232, 225, 5, 2, 8)
        pyxel.line(self.corde_bleu[0], self.corde_bleu[1], self.corde_bleu[2], self.corde_bleu[3], self.corde_bleu[4])
        pyxel.line(self.corde_rouge[0], self.corde_rouge[1], self.corde_rouge[2], self.corde_rouge[3], self.corde_rouge[4])
        pyxel.rect(self.milieu[0], self.milieu[1], self.milieu[2], self.milieu[3], self.milieu[4])
        pyxel.rect(self.pilier_bleu[0], self.pilier_bleu[1], self.pilier_bleu[2], self.pilier_bleu[3], self.pilier_bleu[4])
        pyxel.rect(self.pilier_rouge[0], self.pilier_rouge[1], self.pilier_rouge[2], self.pilier_rouge[3], self.pilier_rouge[4])
        if not self.fin:
            pyxel.text(80, 100, "Tirez jusqu'a votre poteau !", 0)
        else:
            pyxel.text(100, 100, f"{self.fin} a gagne !", 0)
        # =============== RECTANGLES ===============
        for rectangle in self.rectangles:
            rectangle.dessiner()

class PingPong:
    def __init__(self):
        self.rectangle1 = Rectangle(15, 15, 40, 15, 7, "Accueil", 13, 2, Accueil, 8)
        self.rectangles = [self.rectangle1]
        pyxel.run(self.update, self.draw)
    
    def update(self):
        for rectangle in self.rectangles:
            rectangle.clique()
    
    def draw(self):
        pyxel.rect(0,0,256,256,5)
        pyxel.rect(0,0,10,256,7)
        pyxel.rect(246,0,250,256,7)
        pyxel.rect(0,0,256,10,7)
        pyxel.rect(10,246,256,256,7)
        pyxel.line(0,128,245,128,7)
        pyxel.line(128,10,128,245,0)
        pyxel.text(55, 120, "Pas assez de temps, pas de raquettes !", 7)
        pyxel.text(85, 130, "Passez a un autre jeu !", 7)
        # =============== RECTANGLES ===============
        for rectangle in self.rectangles:
            rectangle.dessiner()
class Lancer:
    def __init__(self):
        # =============== RECTANGLES ===============
        self.rectangle1 = Rectangle(211, 5, 40, 15, 7, "Accueil", 13, 2, Accueil, 8)
        self.rectangles = [self.rectangle1]
        
        # =============== ELEMENTS JEU ===============
        self.jauge = [21, 221, 2, 8, 8]
        self.direction = "droite"
        self.stop = False
        self.distance_rouge = 0
        self.distance_bleu = 0
        self.plot_rouge = [0, 0]
        self.plot_bleu = [10, 0]
        self.zones = [[(61, 50), (70, 40)], [(95, 80), (110,61)], [(138, 111), (155, 75)], [(174, 144), (200, 98)], [(212, 176), (241, 132)]]
        self.gagnant = "..."
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if not self.stop:
            if self.direction == "droite":
                self.jauge[0] += 5
            elif self.direction == "gauche":
                self.jauge[0] -= 5
            
            if self.jauge[0] >= 165:
                self.direction = "gauche"
            elif self.jauge[0] <= 21:
                self.direction = "droite"

            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.distance_rouge == 0:
                    self.distance_rouge = sqrt((self.jauge[0] - 95)**2)
                    print(int(self.distance_rouge // 15))
                    self.plot_rouge = self.zones[4 - int(self.distance_rouge // 15)][0]
                elif self.distance_bleu == 0:
                    self.distance_bleu = sqrt((self.jauge[0] - 95)**2)
                    self.plot_bleu = self.zones[4 - int(self.distance_bleu // 15)][1]
                    
                    self.stop = True
                    if self.distance_bleu < self.distance_rouge:
                        self.gagnant = "le Bleu !"
                    elif self.distance_bleu > self.distance_rouge:
                        self.gagnant = "le Rouge !"
                    else:
                        self.gagnant = "le Bleu ET le Rouge !"
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            print(pyxel.mouse_x, pyxel.mouse_y)
        
        
        for rectangle in self.rectangles:
            rectangle.clique()
    
    def draw(self):
        pyxel.rect(0,0,256,256,11)
        pyxel.circ(10,10,8,7)
        
        pyxel.circ(0,0,300,6)
        pyxel.circb(0,0,300,7)
        pyxel.circ(0,0,250,2)
        pyxel.circb(0,0,250,7)
        pyxel.circ(0,0,200,8)
        pyxel.circb(0,0,200,7)
        pyxel.circ(0,0,150,14)
        pyxel.circb(0,0,150,7)
        pyxel.circ(0,0,100,10)
        pyxel.circb(0,0,100,7)
        pyxel.circb(0,0,50,9)
        pyxel.circb(0,0,50,7)
        pyxel.circ(10,10,8,7)
        pyxel.circ(10,10,6,11)

        pyxel.tri(12,19,253,245,2,253,11)
        pyxel.tri(0,29,0,256,256,256,11)
        pyxel.tri(19,12,256,83,256,1,11)
        pyxel.rect(40,0,250,20,11)
        pyxel.line(12,18,253,241,7)
        pyxel.line(17,12,255,85,7)
        
        pyxel.rect(20, 220, 150, 10, 7)
        pyxel.rectb(20, 220, 150, 10, 0)
        
        pyxel.text(20, 150, f"Distance Rouge : {self.distance_rouge}", 0)
        pyxel.text(20, 170, f"Distance Bleu : {self.distance_bleu}", 0)
        pyxel.text(20, 190, f"Le gagnant est {self.gagnant}", 0)

        pyxel.rect(95, 221, 2, 8, 3)
        pyxel.rect(self.jauge[0], self.jauge[1], self.jauge[2], self.jauge[3], self.jauge[4])
        
        # Plots
        pyxel.circ(self.plot_rouge[0], self.plot_rouge[1], 2, 8)
        pyxel.circ(self.plot_bleu[0], self.plot_bleu[1], 2, 1)
        
        for rectangle in self.rectangles:
            rectangle.dessiner()

# ==================================== ELEMENTS ====================================
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

class Joueur:
    def __init__(self, x, y, coul_corp, coul_bras):
        self.x = x
        self.y = y
        self.coul = coul_corp
        self.coul_bras = coul_bras

class Soleil_lune:
    def __init__(self, x, y, rayon, coul_inter, coul_exter):
        self.x = x
        self.y = y
        self.r = rayon
        self.coul_i = coul_inter
        self.coul_e = coul_exter

class Etoile:
    def __init__(self, x, y, coul):
        self.coul = coul
        self.x = x
        self.y = y

class Nuage:
    def __init__(self, x, y, coul, rayon):
        self.x = x
        self.y = y
        self.coul = coul
        self.r = rayon
Accueil()