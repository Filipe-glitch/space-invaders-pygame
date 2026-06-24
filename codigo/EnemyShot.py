import pygame

from codigo.Entity import Entity
from codigo.Const import ENEMY_SHOT_SPEED

class EnemyShot(Entity):

    def __init__(self, position):
        super().__init__(
            './assets/tiro_inimigo.png',
            position
        )

        self.image = pygame.transform.rotate(
            self.image,
            180
        )

    def move(self):
        self.rect.y += ENEMY_SHOT_SPEED