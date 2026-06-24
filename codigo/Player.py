import pygame
from codigo.Const import (PLAYER_SPEED, WIN_WIDTH,KEY_LEFT,KEY_RIGHT,)

from codigo.Entity import Entity
class Player(Entity):
    def __init__(self):

        super().__init__(
            './assets/nave_player.png',
            (WIN_WIDTH // 2, 700)
        )

        self.health = 3
        self.score = 0
    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[KEY_LEFT]) and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED

        if (keys[KEY_RIGHT]) and self.rect.right < WIN_WIDTH:
            self.rect.x += PLAYER_SPEED