# engine/loop.py
# El corazón del motor. Inicializa pygame y corre el game loop.
# Este archivo no lo tocás entre proyectos.

import pygame
import sys
from engine import settings
from engine.input_handler import InputHandler
from engine.audio_manager import AudioManager
from engine.scene_manager import SceneManager, Scene


class Engine:
    def __init__(self):
        pygame.init()

        # Pantalla
        flags = pygame.FULLSCREEN if settings.FULLSCREEN else 0
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), flags
        )
        pygame.display.set_caption(settings.SCREEN_TITLE)

        # Sistemas del motor
        self.clock        = pygame.time.Clock()
        self.input        = InputHandler()
        self.audio        = AudioManager()
        self.scenes       = SceneManager(self.input, self.audio)

        # Debug
        self._debug_font = pygame.font.SysFont("monospace", 14) if settings.DEBUG_MODE else None

    def run(self, initial_scene: Scene):
        """
        Punto de entrada del juego. Pasale la primera escena.
        Ejemplo en main.py:
            engine = Engine()
            engine.run(MenuScene(engine.scenes))
        """
        self.scenes.change(initial_scene)

        running = True
        while running:
            # Delta time en segundos, capado a 0.05s para evitar saltos grandes
            dt = min(self.clock.tick(settings.FPS_TARGET) / 1000.0, 0.05)

            # 1. Input
            self.input.process_events()
            if self.input.quit_requested():
                running = False
                break

            # 2. Update
            self.scenes.update(dt)

            # 3. Render
            self.screen.fill((0, 0, 0))
            self.scenes.render(self.screen)

            if settings.DEBUG_MODE:
                self._render_debug()

            pygame.display.flip()

        self._quit()

    def _render_debug(self):
        fps_text = self._debug_font.render(
            f"FPS: {self.clock.get_fps():.0f}", True, (0, 255, 0)
        )
        self.screen.blit(fps_text, (8, 8))

    def _quit(self):
        self.audio.quit()
        pygame.quit()
        sys.exit()
