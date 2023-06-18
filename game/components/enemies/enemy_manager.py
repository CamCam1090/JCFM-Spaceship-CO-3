
import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy2
from game.utils.constants import SCREEN_HEIGHT


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemy_types = [Enemy, Enemy2]
    
    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())
            self.enemies.append(Enemy2())
            

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
                     
    
    def draw(self, Screen):
        for enemy in self.enemies:
            enemy.draw(Screen)

    def get_enemies(self):
        return self.enemies
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []

