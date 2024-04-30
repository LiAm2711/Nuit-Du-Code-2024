import pyxel
class Jeux:
    def __init__(self):
        pyxel.init(256,256, title = "Teste graphisme")
        pyxel.mouse(True)
        #self.joueur = Joueur(120,120,7,4)
        self.joueur1 = Joueur(234,242,7,4)
        self.joueur2 = Joueur(14,242,7,4)
        self.soleil_jeux_corde = Soleil_lune(190, 25, 15, 10, 9)
        self.lune_menu = Soleil_lune (20, 20, 10, 7, 6)
        self.sapin_menu = Sapin(10,10,4,11)
        self.etoile_menu = [Etoile(78,26,7),Etoile(63,68,7),Etoile(36,110,7),Etoile(126,105,7),Etoile(118,67,7),Etoile(184,39,7),Etoile(142,16,7),Etoile(184,104,7),Etoile(173,83,7),Etoile(218,75,7)]
        self.nuage_jeux_de_corde_1 = Nuage(50,100, 7, 6)
        self.nuage_jeux_de_corde_2 = Nuage(175,75, 7, 6)
        self.nuage_jeux_de_corde_3 = Nuage(121,113, 7, 6)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print(pyxel.mouse_x,pyxel.mouse_y)

    def draw(self):
        pyxel.cls(0)

        pyxel.rect(0,0,256,256,11)
        pyxel.circ(10,10,8,7)
        pyxel.circ(10,10,6,11)
        pyxel.circb(0,0,50,7)
        pyxel.circb(0,0,100,7)
        pyxel.circb(0,0,150,7)
        pyxel.circb(0,0,200,7)
        pyxel.circb(0,0,250,7)
        pyxel.circb(0,0,300,7)
        pyxel.tri(12,19,253,245,2,253,11)
        pyxel.tri(0,29,0,256,256,256,11)
        pyxel.tri(19,12,256,83,256,1,11)
        pyxel.rect(40,0,250,20,11)
        pyxel.line(12,18,253,241,7)
        pyxel.line(17,12,255,85,7)
        '''
        #pour ping pong
        pyxel.rect(0,0,256,256,5)
        pyxel.rect(0,0,10,256,7)
        pyxel.rect(246,0,250,256,7)
        pyxel.rect(0,0,256,10,7)
        pyxel.rect(10,246,256,256,7)
        pyxel.line(0,128,245,128,7)
        pyxel.line(128,10,128,245,0)
        '''
        '''
        #Pour Menu
        pyxel.rect(0,0,256,256,1)
        pyxel.circ(256,1350,1220,15)
        pyxel.circ(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r, self.lune_menu.coul_i)
        pyxel.circb(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r, self.lune_menu.coul_e)
        pyxel.circb(self.lune_menu.x, self.lune_menu.y, self.lune_menu.r - 1, self.lune_menu.coul_e)
        pyxel.circ(self.lune_menu.x - 8, self.lune_menu.y, self.lune_menu.r - 1, 1)

        pyxel.tri(177,192,203,166,229,192,11)
        pyxel.tri(183,175,223,175,203,153,11)
        pyxel.tri(185,160,218,158,202,142,11)
        pyxel.rect(199,193,10,10,4)

        for etoile in self.etoile_menu:
            pyxel.pset(etoile.x, etoile.y, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y - 1, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y + 1, etoile.coul)
            pyxel.pset(etoile.x + 2, etoile.y , etoile.coul)
'''
        '''
        #perso
        pyxel.line(self.joueur.x, self.joueur.y - 11, self.joueur.x - 11, self.joueur.y - 4, self.joueur.coul_bras)
        pyxel.circ(self.joueur.x, self.joueur.y, 7, self.joueur.coul)
        pyxel.circ(self.joueur.x, self.joueur.y - 11, 5, self.joueur.coul)
        pyxel.circ(self.joueur.x, self.joueur.y - 19, 3, self.joueur.coul)
        pyxel.line(self.joueur.x, self.joueur.y - 11, self.joueur.x - 11, self.joueur.y - 8, self.joueur.coul_bras)
        #soleil
        pyxel.circ(self.soleil.x, self.soleil.y, self.soleil.r, self.soleil.coul_i)
        pyxel.circb(self.soleil.x, self.soleil.y, self.soleil.r, self.soleil.coul_e)
        pyxel.circb(self.soleil.x, self.soleil.y, self.soleil.r - 1, self.soleil.coul_e)
        #Lune
        pyxel.circ(self.lune.x, self.lune.y, self.lune.r, self.lune.coul_i)
        pyxel.circb(self.lune.x, self.lune.y, self.lune.r, self.lune.coul_e)
        pyxel.circb(self.lune.x, self.lune.y, self.lune.r - 1, self.lune.coul_e)
        pyxel.circ(self.lune.x - 8, self.lune.y, self.lune.r - 1, 0)
        #etoile
        for etoile in self.etoile:
            pyxel.pset(etoile.x, etoile.y, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y - 1, etoile.coul)
            pyxel.pset(etoile.x + 1, etoile.y + 1, etoile.coul)
            pyxel.pset(etoile.x + 2, etoile.y , etoile.coul)
        #nuage
        pyxel.circ(self.nuage.x, self.nuage.y, self.nuage.r, self.nuage.coul)
        pyxel.circ(self.nuage.x + 5, self.nuage.y - 2, self.nuage.r, self.nuage.coul)
        pyxel.circ(self.nuage.x + 11, self.nuage.y, self.nuage.r, self.nuage.coul)
        pyxel.circ(self.nuage.x + 16, self.nuage.y - 2, self.nuage.r, self.nuage.coul)
        '''

'''
        #arriére plan jeux corde
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
'''

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

class Sapin:
    def __init__(self, x, y, coul_tronc, coul_leaf):
        self.x = x
        self.y = y
        self.coul_tronc = coul_tronc
        self.coul_leaf = coul_leaf

Jeux()