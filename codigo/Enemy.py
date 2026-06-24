import pygame
from codigo.Entity import Entity
from codigo.Const import ENEMY_HEALTH

class Enemy(Entity):
    def __init__(self,image_path: str,position: tuple,score_value: int):
        super().__init__(image_path,position)
        self.image = pygame.transform.rotate(
        self.image,
        180
        )
        self.image = pygame.transform.scale(self.image,(64, 64))
        self.health = ENEMY_HEALTH
        self.score = score_value
        self.arrived = False

    def move(self):
        if not self.arrived:
            self.rect.y += 2
            if self.rect.y >= self.target_y:
                self.arrived = True