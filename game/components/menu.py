import pygame
from game.components.score_manager import ScoreManager
from game.utils.constants import BG_2, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 

    def __init__(self, message, text_size=30):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON,(120, 80)) 
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        self.score = ScoreManager()

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()
                


    def draw(self, screen):
        background_image = pygame.image.load("game/assets/Other/zat.png") 
        background_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background_scaled, (0, 0))  
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)


    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center =(self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def draw_message(self, screen, message, x, y):
        text = self.font.render(message, True, (0, 0, 255))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    