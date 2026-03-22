# engine/input_handler.py
# Maneja todo el input del juego en un solo lugar.
# Las escenas consultan este módulo en vez de llamar pygame.key directamente.

import pygame


class InputHandler:
    def __init__(self):
        self._keys_held     = set()  # teclas sostenidas este frame
        self._keys_pressed  = set()  # teclas recién presionadas
        self._keys_released = set()  # teclas recién soltadas
        self._mouse_pos     = (0, 0)
        self._mouse_pressed = set()
        self._quit_requested = False

    # ── Llamar una vez por frame, antes de update ──────────────────────────
    def process_events(self):
        self._keys_pressed.clear()
        self._keys_released.clear()
        self._mouse_pressed.clear()
        self._quit_requested = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_requested = True

            elif event.type == pygame.KEYDOWN:
                self._keys_pressed.add(event.key)
                self._keys_held.add(event.key)

            elif event.type == pygame.KEYUP:
                self._keys_released.add(event.key)
                self._keys_held.discard(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_pressed.add(event.button)

        self._mouse_pos = pygame.mouse.get_pos()

    # ── API pública para las escenas ───────────────────────────────────────
    def is_held(self, key) -> bool:
        """Verdadero mientras la tecla esté sostenida."""
        return key in self._keys_held

    def is_pressed(self, key) -> bool:
        """Verdadero solo el frame en que se presionó."""
        return key in self._keys_pressed

    def is_released(self, key) -> bool:
        """Verdadero solo el frame en que se soltó."""
        return key in self._keys_released

    def mouse_pos(self) -> tuple:
        return self._mouse_pos

    def mouse_clicked(self, button=1) -> bool:
        """button: 1=izquierdo, 2=medio, 3=derecho"""
        return button in self._mouse_pressed

    def quit_requested(self) -> bool:
        return self._quit_requested
