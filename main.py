from .Logica import GestorPartida
from .Personajes import JugadorJuego
# Intenta estructurar el main.py con el siguiente orden.
# --- FASE 1: LA NOCHE 🌙 ---
juego=GestorPartida()
juego.anadirJugador("Nacho", "lobo")
juego.anadirJugador("Elena", "vidente")
juego.anadirJugador("Carlos","aldeano")
# Comprobamos estado antes de que amanezca
# --- FASE 2: EL DÍA ☀️ ---
# El motor de la partida ejecuta el linchamiento
juego=GestorPartida()
# --- FINAL DE LA PARTIDA ---