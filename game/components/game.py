import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.score_manager import ScoreManager
from game.components.spaceship import Spaceship
from game.components.powerups.manager import Manager

from game.utils.constants import BG, BG_SOUND, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        
        self.death_count = 0
        
        self.power_up_manager = Manager()
        self.score_manager = ScoreManager()
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu("press any key to start")

    def run(self):
        pygame.mixer.music.load("game/assets/Sounds/bg.mp3")
        
        pygame.mixer.music.play(-1)
        self.adjust_background_sound_volume(0.2)
       # Game loop: events - update - draw
        self.running = True
        while self.running: 
            if not self.playing:
                self.show_menu()


        pygame.mixer.music.stop()            
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.enemy_manager.reset()
        self.playing = True
        #self.score = 0
        self.score_manager.start_new_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update(self.screen.get_rect())
        self.power_up_manager.draw(self.screen)
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        self.score_manager.draw(self.screen)

    def max(self):
        self.score_manager.draw_max_score_ever(self.screen)

    def deaths(self):
        self.score_manager.draw_games_played(self.screen)

    def show_menu(self):
        if self.death_count > 0:
            self.menu.update_message("Game over, press any key")
            self.draw_score()
            self.max()
            self.deaths()
            pygame.display.flip()
           
    
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)
        pygame.display.flip()

    def on_close(self):
        self.playing = False
        self.running = False 

    
    def adjust_background_sound_volume(self, volume):
        pygame.mixer.music.set_volume(volume)