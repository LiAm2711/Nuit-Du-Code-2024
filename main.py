import pyxel

class Jeu:
    def __init__(self) -> None:
        pyxel.init(128, 128)
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        pass
    
    def draw(self):
        pass

Jeu()