from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, image_path: str, position: tuple):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(
            center=position
        )

        self.health = 1
    @abstractmethod
    def move(self):
        pass