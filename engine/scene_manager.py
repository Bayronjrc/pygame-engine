# engine/scene_manager.py
# Define la clase base Scene y el SceneManager que controla cuál escena está activa.
# Todas tus escenas en game/scenes/ heredan de Scene.

from __future__ import annotations
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.input_handler import InputHandler
    from engine.audio_manager import AudioManager


# ── Clase base ─────────────────────────────────────────────────────────────
class Scene:
    """
    Clase base para todas las escenas del juego.
    Heredá de esta clase en game/scenes/ y sobreescribí los métodos que necesités.
    """

    def __init__(self, manager: SceneManager):
        self.manager = manager
        self.input: InputHandler = manager.input
        self.audio: AudioManager = manager.audio

    def on_enter(self):
        """Se llama una vez cuando la escena se vuelve activa."""
        pass

    def on_exit(self):
        """Se llama una vez antes de cambiar a otra escena."""
        pass

    def update(self, dt: float):
        """
        Lógica del juego. dt = delta time en segundos desde el frame anterior.
        Multiplicá velocidades por dt para que sean independientes del FPS.
        """
        pass

    def render(self, screen: pygame.Surface):
        """Dibujá todo lo que necesita verse en pantalla."""
        pass


# ── Manager ────────────────────────────────────────────────────────────────
class SceneManager:
    def __init__(self, input_handler: InputHandler, audio_manager: AudioManager):
        self.input = input_handler
        self.audio = audio_manager
        self._current: Scene | None = None
        self._next: Scene | None = None

    def change(self, scene: Scene):
        """
        Solicita un cambio de escena. El cambio ocurre al inicio del próximo frame
        para evitar problemas si se llama desde dentro de update().
        """
        self._next = scene

    def _apply_pending_change(self):
        if self._next is not None:
            if self._current:
                self._current.on_exit()
            self._current = self._next
            self._next = None
            self._current.on_enter()

    def update(self, dt: float):
        self._apply_pending_change()
        if self._current:
            self._current.update(dt)

    def render(self, screen: pygame.Surface):
        if self._current:
            self._current.render(screen)

    @property
    def current(self) -> Scene | None:
        return self._current
