from .Jugador import JugadorJuego
class Aldeano (JugadorJuego):
    """
    Reprenta a un Aldeano
    """
    def AccionNocturna(self, objetivo=None):
        if objetivo: 
            objetivo.esta_vivo=False
            return f"El aldeano {self.Nombre} duerme profundamente."