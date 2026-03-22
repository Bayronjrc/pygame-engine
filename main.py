# main.py
# Punto de entrada del juego. Este archivo SÍ lo modificás por proyecto.
# Ajustá las settings y cambiá la escena inicial según tu juego.

from engine import settings

# ── Configuración del proyecto (modificar por juego) ──────────────────────
settings.SCREEN_WIDTH  = 800
settings.SCREEN_HEIGHT = 600
settings.SCREEN_TITLE  = "Mi Juego"
settings.FPS_TARGET    = 60
settings.DEBUG_MODE    = False

# ── Iniciar el motor ───────────────────────────────────────────────────────
from engine.loop import Engine
from game.scenes.menu import MenuScene   # Cambiá esto por tu escena inicial

if __name__ == "__main__":
    engine = Engine()
    engine.run(MenuScene(engine.scenes))
