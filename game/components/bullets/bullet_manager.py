import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE


class BulletManager:
    def __init__(self):
        self.player_bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] =[]
        

    def update(self, game):
        enemies = game.enemy_manager.get_enemies()
        for player_bullet in self.player_bullets:
            player_bullet.update(self.player_bullets)

            for enemy in enemies:
                if player_bullet.rect.colliderect(enemy.rect):
                    self.player_bullets.remove(player_bullet)
                    game.enemy_manager.remove_enemy(enemy)
                    game.score += 1 
                    break


        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            #verifivar si hemos chocado con el jugador
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_count += 1
                pygame.time.delay(1000)
                break


    def draw(self, screen):
        for player_bullet in self.player_bullets:
            player_bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == PLAYER_TYPE and len(self.player_bullets) < 5:
            self.player_bullets.append(bullet)