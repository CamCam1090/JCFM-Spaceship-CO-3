
import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    PLAYER_BULLETS_IMG = pygame.transform.scale(BULLET, (13, 20))
    BULLETS = {ENEMY_TYPE: ENEMY_BULLET_IMG,
               PLAYER_TYPE: PLAYER_BULLETS_IMG}

    
    def __init__(self, spcaceship):
        self.image = self.BULLETS[spcaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spcaceship.rect.center
        self.owner = spcaceship.type


    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)  

        if self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
          

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))