from .Jugador import JugadorJuego
class Vidente (JugadorJuego):
    """
    Reprenta a un Vidente
    """
    def AccionNocturna(self, objetivo=None):
        if objetivo: 
            objetivo.esta_vivo=False
            return f"El aldeano {self.Nombre} duerme profundamente."
        