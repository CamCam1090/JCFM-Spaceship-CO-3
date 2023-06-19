import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 

class ScoreManager:
    def __init__(self):
        self.max_score_ever = 0
        self.score = 0
        self.games_played = 0
        self.death_count = 0

        self.font = pygame.font.Font(FONT_STYLE, 22)

    def start_new_game(self):
        self.score = 0

    def increase_score(self, amount):
        self.score += amount

    def end_game(self):
        self.games_played += 1
        if self.score > self.max_score_ever:
            self.max_score_ever = self.score

    def draw(self, screen):
        text_score = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_score_rect = text_score.get_rect()
        text_score_rect.center = (1000, 50)
        screen.blit(text_score, text_score_rect) 
        
        

    def draw_max_score_ever(self,screen):
        text_max_score = self.font.render(f'Max Score: {self.max_score_ever}', True, (255, 0, 0))
        text_max_score_rect = text_max_score.get_rect()
        text_max_score_rect.center = (1000, 80)
        screen.blit(text_max_score, text_max_score_rect)
        

    def draw_games_played(self, screen):
        text_games_played = self.font.render(f'Games Played: {self.games_played}', True, (0, 0, 255))
        text_games_played_rect = text_games_played.get_rect()
        text_games_played_rect.center = (1000, 110)
        screen.blit(text_games_played, text_games_played_rect)
    

       