import random
import pygame
from game.components.bullets import bullet_manager
from game.components.bullets.bullet import Bullet
from game.utils.constants import PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP
from pygame.sprite import Sprite


class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = PLAYER_TYPE
       
        self.shooting_time = random.randint(30, 50)

    def update(self, user_input, game):
        
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
    
  
    def move_left(self):
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
        else:
            self.rect.x -= 10    
        
    def move_right(self):
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        else:
            self.rect.x  += 10
  
    def move_up(self):   
        if self.rect.y > SCREEN_HEIGHT //2:
            self.rect.y -= 10


    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT -50:
            self.rect.y += 10


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
       