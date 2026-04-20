from .Jugador import JugadorJuego
class Lobo (JugadorJuego):
    def AccionNocturna(self, objetivo=None):
        if objetivo: 
            objetivo.esta_vivo=False
            return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."