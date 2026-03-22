# engine/settings.py
# Configuración global del motor.
# Podés sobreescribir estos valores en main.py antes de inicializar el engine.

# Pantalla
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE  = "Mi Juego"
FPS_TARGET    = 60
FULLSCREEN    = False

# Audio
MASTER_VOLUME = 1.0   # 0.0 a 1.0
MUSIC_VOLUME  = 0.7
SFX_VOLUME    = 1.0

# Debug
DEBUG_MODE    = False  # Muestra FPS y colisiones si es True
