# game/scenes/menu.py
# Escena de menú de ejemplo. Reemplazala o modificala para tu juego.
# Esta es la escena que carga main.py por defecto.

import pygame
from engine.scene_manager import Scene, SceneManager


class MenuScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        self._font_big   = pygame.font.SysFont("monospace", 48)
        self._font_small = pygame.font.SysFont("monospace", 22)

    def on_enter(self):
        # Acá podés iniciar música de menú, por ejemplo:
        # self.audio.play_music("assets/audio/menu.ogg")
        pass

    def update(self, dt: float):
        # Presionar Enter para pasar a la escena de juego
        if self.input.is_pressed(pygame.K_RETURN):
            # from game.scenes.gameplay import GameplayScene
            # self.manager.change(GameplayScene(self.manager))
            pass

        # Presionar Escape para salir
        if self.input.is_pressed(pygame.K_ESCAPE):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def render(self, screen: pygame.Surface):
        screen.fill((15, 15, 30))

        title = self._font_big.render("MI JUEGO", True, (255, 255, 255))
        hint  = self._font_small.render("ENTER para jugar  |  ESC para salir", True, (120, 120, 160))

        cx = screen.get_width() // 2
        cy = screen.get_height() // 2

        screen.blit(title, title.get_rect(center=(cx, cy - 40)))
        screen.blit(hint,  hint.get_rect(center=(cx, cy + 30)))
