class JugadorJuego:  
    """
    Reprenta a los Jugadores
    """
    def __init__(self, nombre, Rol): 
        self.Nombre = nombre 
        self.rol=Rol 
        self.esta_vivo=True
        
        
    def AccionNocturna(self, objetivo=None):
        return