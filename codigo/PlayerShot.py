from codigo.Entity import Entity
from codigo.Const import PLAYER_SHOT_SPEED

class PlayerShot(Entity):
    def __init__(self, position):
        super().__init__(
            './assets/tiro_player.png',
            position
        )

    def move(self):
        self.rect.y -= PLAYER_SHOT_SPEED