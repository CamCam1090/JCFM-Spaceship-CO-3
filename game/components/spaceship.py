import random
import pygame
from game.components.bullets import bullet_manager
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP
from pygame.sprite import Sprite


class Spaceship(Sprite):
    def __init__(self):
        pygame.mixer.init()
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = PLAYER_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False 
        self.power_up_time = 0
        self.SonidoDisparo = pygame.mixer.music.load("game/assets/Sounds/shoot.mp3")
       
        self.shooting_time = random.randint(30, 50)

    def update(self, user_input, game):
        
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        
    
  
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
       
    def set_image(self, size = (60, 40), image= SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)