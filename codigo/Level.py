import random
import sys

import pygame

from codigo.Const import *
from codigo.Player import Player
from codigo.Enemy import Enemy
from codigo.PlayerShot import PlayerShot
from codigo.EnemyShot import EnemyShot
from codigo.EntityMediator import EntityMediator


class Level:

    def __init__(self, window):

        self.window = window

        self.background = pygame.image.load(
            "./assets/background_level1.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.player = Player()

        self.entity_list = [self.player]

        self.last_enemy_shot = pygame.time.get_ticks()

        self.create_enemies()

    def create_enemies(self):

        start_x = 200
        spacing_x = 120

        rows = [
            ("./assets/nave_inimiga_um.png", ENEMY1_SCORE, 100),
            ("./assets/nave_inimiga_dois.png", ENEMY2_SCORE, 200),
            ("./assets/nave_inimiga_um.png", ENEMY1_SCORE, 300)
        ]

        for row_index, row_data in enumerate(rows):

            image, score, target_y = row_data

            for col in range(5):

                enemy = Enemy(
                    image,
                    (
                        start_x + col * spacing_x,
                        -100
                    ),
                    score
                )

                enemy.target_y = target_y

                self.entity_list.append(enemy)

    def player_shoot(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:

            current_time = pygame.time.get_ticks()

            if not hasattr(self, "last_player_shot"):
                self.last_player_shot = 0

            if current_time - self.last_player_shot > 300:

                self.last_player_shot = current_time

                shot = PlayerShot(
                    (
                        self.player.rect.centerx,
                        self.player.rect.top
                    )
                )

                self.entity_list.append(shot)

                pygame.mixer.Sound(
                    "./assets/tiro_nave_jogador.wav"
                ).play()

    def enemy_shoot(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_enemy_shot > random.randint(1000, 3000):

            enemies = []

            for ent in self.entity_list:

                if isinstance(ent, Enemy):
                    enemies.append(ent)

            if len(enemies) > 0:

                shooter = random.choice(enemies)

                shot = EnemyShot(
                    (
                        shooter.rect.centerx,
                        shooter.rect.bottom
                    )
                )

                self.entity_list.append(shot)

                pygame.mixer.Sound(
                    "./assets/tiro_nave_inimiga.wav"
                ).play()

            self.last_enemy_shot = current_time

    def draw_hud(self):

        font = pygame.font.SysFont(
            "Arial",
            30
        )

        lives_text = font.render(
            f"Vidas: {self.player.health}",
            True,
            WHITE
        )

        score_text = font.render(
            f"Score: {self.player.score}",
            True,
            WHITE
        )

        self.window.blit(
            lives_text,
            (20, 20)
        )

        self.window.blit(
            score_text,
            (20, 60)
        )

    def victory_screen(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(
        "./assets/level_victory_music.wav"
        )  
        pygame.mixer.music.play()
        background = pygame.image.load(
        "./assets/victory_background.png"
        ).convert()
        background = pygame.transform.scale(
           background,
           (WIN_WIDTH, WIN_HEIGHT)
        ) 
        font = pygame.font.SysFont(
           "Arial",
            80,
            bold=True
        )
        
        while True:
            self.window.blit(
               background,
               (0, 0)
            )
            text = font.render(
               "VOCE VENCEU!",
                True,
                WHITE
            )

            rect = text.get_rect(
                center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)
            )
 
            self.window.blit(
                text,
                rect
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       pygame.quit()
                       sys.exit()

    def game_over_screen(self):

        pygame.mixer.music.stop()

        pygame.mixer.music.load(
            "./assets/music_defeat.ogg"
        )

        pygame.mixer.music.play()

        font = pygame.font.SysFont(
            "Arial",
            80,
            bold=True
        )

        while True:

            self.window.blit(
                self.background,
                (0, 0)
            )

            text = font.render(
                "GAME OVER",
                True,
                RED
            )

            rect = text.get_rect(
                center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)
            )

            self.window.blit(
                text,
                rect
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self):

        pygame.mixer.music.load(
            "./assets/music_level.wav"
        )

        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(FPS)

            self.window.blit(
                self.background,
                (0, 0)
            )

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player_shoot()

            self.enemy_shoot()

            for entity in self.entity_list:

                entity.move()

                self.window.blit(
                    entity.image,
                    entity.rect
                )

            EntityMediator.verify_collisions(
                self.entity_list
            )

            EntityMediator.remove_offscreen(
                self.entity_list
            )

            self.draw_hud()

            if not EntityMediator.player_alive(
                self.entity_list
            ):
                self.game_over_screen()

            if EntityMediator.enemies_remaining(
                self.entity_list
            ) == 0:
                self.victory_screen()

            pygame.display.flip()