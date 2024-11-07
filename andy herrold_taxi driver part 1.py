#andyherrold_taxidriver
#slide and catch game part 1
import pygame, simpleGE, random
"""
taxidriver.py
slide and catch game
andy herrold
"""

class Molly(simpleGE.Sprite):
    def__init__(self, scene):
        super()__init__(scene)
        self.setImage("Molly.png")
        self.setSize(25, 25)
        
class Taxi(simpleGE.Sprite):
    def__init__(self, scene):
        super().__init__(scene)
        self.setImage("Taxi.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_right):
            self.x += self.moveSpeed
            
            
            
        
class Game(simpleGE.scene):
    def__init__(self):
        super().__init__()
        self.setImage("cityscape.png")
        self.taxi = Taxi(self)
        
        
        self.sprites = [self.taxi,self.molly]
        
    
def main():
    game = Game()
    game.start()

if __name__==__ "main__":
    main()
