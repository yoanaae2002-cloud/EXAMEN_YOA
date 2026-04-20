from ..Personajes.Jugador import JugadorJuego
class GestorPartida: 
    """
    Reprenta la Gestion de la partida
    """
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, type):  
        """
        Añade un Jugador
        Args:
            nombre (str):Nombre Jugador
        """
        self.jugadores.append(JugadorJuego(nombre,type)) 
        
    def VotacionDia(self, NombreVotado):
        """
        Votación del Día
        Args:
            nombreVotado (str):Nombre Jugador
        """
        for jugador in self.jugadores:
            if jugador.Nombre == NombreVotado:
                if jugador.esta_vivo == True:
                    jugador.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
        

    def ComprobarVictoria(self):  
        """
        Comprobación
        Args:
            nombreVotado (str):Nombre Jugador
        Returns:
            str
        """
        
        lista_jugador = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict_jugador = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if lista_jugador >= dict_jugador:
            return "¡Victoria de los Lobos!"
        elif lista_jugador ==0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."