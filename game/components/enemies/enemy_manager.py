
import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy2
from game.utils.constants import SCREEN_HEIGHT


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemy_types = [Enemy, Enemy2]
    
    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
            self.enemies.append(Enemy2())
            

        for enemy in self.enemies:
            enemy.update(self.enemies)
                     
    
    def draw(self, Screen):
        for enemy in self.enemies:
            enemy.draw(Screen)
        

