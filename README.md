# pygame-engine

Motor base personal para juegos 2D con Python + Pygame.
Usá este repo como template en GitHub para arrancar proyectos nuevos con la estructura ya lista.

## Estructura

```
pygame-engine/
├── engine/              # El motor — no modificar entre proyectos
│   ├── settings.py      # Configuración global (resolución, FPS, volumen)
│   ├── loop.py          # Game loop con delta time
│   ├── scene_manager.py # Clase base Scene + SceneManager
│   ├── input_handler.py # Input unificado (teclado, mouse)
│   └── audio_manager.py # Música y efectos de sonido
│
├── game/                # Tu lógica de juego — esto cambia por proyecto
│   ├── scenes/          # Tus escenas (menú, gameplay, game over...)
│   ├── entities/        # Jugador, enemigos, proyectiles...
│   └── systems/         # Colisiones, IA, física personalizada...
│
├── assets/
│   ├── images/          # Sprites, fondos, tilesets
│   ├── audio/           # Música .ogg, efectos .wav
│   └── fonts/           # Fuentes .ttf
│
├── main.py              # Punto de entrada — sí lo modificás por proyecto
└── requirements.txt
```

## Cómo usar este template

1. En GitHub: **Use this template → Create a new repository**
2. Cloná el nuevo repo
3. Instalá dependencias: `pip install -r requirements.txt`
4. Modificá `main.py` con el título y resolución de tu juego
5. Creá tus escenas en `game/scenes/` heredando de `Scene`
6. Arrancá: `python main.py`

## Crear una escena nueva

```python
# game/scenes/gameplay.py
import pygame
from engine.scene_manager import Scene, SceneManager

class GameplayScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        self.player_x = 400

    def on_enter(self):
        self.audio.play_music("assets/audio/game.ogg")

    def update(self, dt: float):
        if self.input.is_held(pygame.K_RIGHT):
            self.player_x += 200 * dt  # velocidad independiente del FPS

        if self.input.is_pressed(pygame.K_ESCAPE):
            from game.scenes.menu import MenuScene
            self.manager.change(MenuScene(self.manager))

    def render(self, screen: pygame.Surface):
        screen.fill((20, 20, 40))
        pygame.draw.rect(screen, (255, 100, 100), (self.player_x, 300, 32, 32))
```

## Cargar efectos de sonido

```python
def on_enter(self):
    self.audio.load_sfx("salto", "assets/audio/jump.wav")

def update(self, dt):
    if self.input.is_pressed(pygame.K_SPACE):
        self.audio.play_sfx("salto")
```

## Debug mode

En `main.py` activá `settings.DEBUG_MODE = True` para ver el FPS en pantalla.

## Dependencias opcionales

Si tu juego necesita física más avanzada, podés agregar `pymunk` al `requirements.txt`.
El motor está diseñado para ser extendido sin modificar `engine/`.
