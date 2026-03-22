# engine/audio_manager.py
# Maneja música de fondo y efectos de sonido.
# Soporta pygame.mixer por defecto. Si no hay audio disponible, falla silenciosamente.

import pygame
from engine import settings


class AudioManager:
    def __init__(self):
        self._initialized = False
        self._sounds: dict[str, pygame.mixer.Sound] = {}
        self._current_music: str | None = None

        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self._initialized = True
        except pygame.error as e:
            print(f"[AudioManager] No se pudo inicializar el audio: {e}")

    # ── Música ─────────────────────────────────────────────────────────────
    def play_music(self, path: str, loops: int = -1, fade_ms: int = 0):
        """Reproduce música en loop. loops=-1 = infinito."""
        if not self._initialized:
            return
        if self._current_music == path:
            return
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(settings.MUSIC_VOLUME * settings.MASTER_VOLUME)
            pygame.mixer.music.play(loops, fade_ms=fade_ms)
            self._current_music = path
        except pygame.error as e:
            print(f"[AudioManager] Error cargando música '{path}': {e}")

    def stop_music(self, fade_ms: int = 0):
        if not self._initialized:
            return
        if fade_ms > 0:
            pygame.mixer.music.fadeout(fade_ms)
        else:
            pygame.mixer.music.stop()
        self._current_music = None

    def set_music_volume(self, volume: float):
        """volume: 0.0 a 1.0"""
        settings.MUSIC_VOLUME = max(0.0, min(1.0, volume))
        if self._initialized:
            pygame.mixer.music.set_volume(settings.MUSIC_VOLUME * settings.MASTER_VOLUME)

    # ── Efectos de sonido ──────────────────────────────────────────────────
    def load_sfx(self, name: str, path: str):
        """Precarga un efecto de sonido con un nombre clave."""
        if not self._initialized:
            return
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(settings.SFX_VOLUME * settings.MASTER_VOLUME)
            self._sounds[name] = sound
        except pygame.error as e:
            print(f"[AudioManager] Error cargando sfx '{name}' en '{path}': {e}")

    def play_sfx(self, name: str):
        """Reproduce un efecto previamente cargado."""
        if not self._initialized:
            return
        sound = self._sounds.get(name)
        if sound:
            sound.play()
        else:
            print(f"[AudioManager] SFX '{name}' no encontrado. Llamá load_sfx primero.")

    def set_sfx_volume(self, volume: float):
        settings.SFX_VOLUME = max(0.0, min(1.0, volume))
        for sound in self._sounds.values():
            sound.set_volume(settings.SFX_VOLUME * settings.MASTER_VOLUME)

    # ── Volumen maestro ────────────────────────────────────────────────────
    def set_master_volume(self, volume: float):
        settings.MASTER_VOLUME = max(0.0, min(1.0, volume))
        self.set_music_volume(settings.MUSIC_VOLUME)
        self.set_sfx_volume(settings.SFX_VOLUME)

    def quit(self):
        if self._initialized:
            pygame.mixer.quit()
