import sys
import pygame
from codigo.Const import WIN_WIDTH, WIN_HEIGHT, WHITE

class Menu:
    def __init__(self, window):
        self.window = window
        self.background = pygame.image.load(
            "./assets/menu_background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.title_font = pygame.font.SysFont(
            "Arial",
            60,
            bold=True
        )

        self.text_font = pygame.font.SysFont(
            "Arial",
            30,
            bold=True 
        )

    def run(self):
        pygame.mixer.music.load(
            "./assets/menu_music.wav"
        )

        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.blit(
                self.background,
                (0, 0)
            )

            self.draw_text("SPACE INVADERS",self.title_font,WHITE,WIN_WIDTH // 2,120)

            self.draw_text(
                "CONTROLES",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                250
            )

            self.draw_text(
                "<- : Mover para esquerda",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                300
            )

            self.draw_text(
                "-> : Mover para direita",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                340
            )

            self.draw_text(
                "ESPACO : Atirar",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                380
            )

            self.draw_text(
                "ENTER : Iniciar Jogo",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                500
            )

            self.draw_text(
                "ESC : Sair",
                self.text_font,
                WHITE,
                WIN_WIDTH // 2,
                540
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        return True

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

    def draw_text(self, text, font, color, center_x, y):
        shadow_surface = font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_surface.get_rect(
            center=(center_x + 2, y + 2) 
        )
        self.window.blit(shadow_surface, shadow_rect)

        surface = font.render(text, True, color)
        rect = surface.get_rect(
            center=(center_x, y)
        )
        self.window.blit(surface, rect)