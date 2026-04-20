from ..Personajes.Jugador import JugadorJuego
class GestorPartida:  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, type):  
        self.jugadores.append(JugadorJuego(nombre,type)) 
        
    def votacionDia(self, NombreVotado):
        for jugador in self.jugadores:
            if jugador.Nombre == NombreVotado:
                if jugador.esta_vivo:
                    jugador.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
        

    def comprobarVictoria(self):  
        
        lista_jugador = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict_jugador = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if lista_jugador >= dict_jugador:
            return "¡Victoria de los Lobos!"
        elif lista_jugador ==0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."