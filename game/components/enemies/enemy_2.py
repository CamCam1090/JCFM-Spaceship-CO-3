import random
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = "left"
RIGHT = "right"
class Enemy2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.SPEED_X = random.randrange(1, 10)
        self.SPEED_Y = random.randrange(1, 10)

    def update(self, ships):
        super().update(ships)
       
        if self.movement == LEFT:
            self.rect.y -= self.speed_y +1 
            self.rect.y += self.speed_y +2
            self.rect.x += self.SPEED_X 
        else:
           
            self.rect.x += self.SPEED_X
        
        