# class JugadorJuego:  
#     def __init__(self, nombre, Rol): 
#         self.Nombre = nombre 
#         self.rol=Rol 
#         self.esta_vivo=True
          
#     def AccionNocturna(self, objetivo=None):  
#         if not self.esta_vivo:
#             return f"{self.Nombre} está muerto."
            
#         if self.rol=="lobo": 
#             if objetivo: 
#                 objetivo.esta_vivo=False
#                 return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."
#         elif self.rol== "vidente":
#             if objetivo: 
#                 return f"La vidente {self.Nombre} ve que {objetivo.Nombre} es {objetivo.rol}."
#         elif self.rol == "aldeano":
#             return f"El aldeano {self.Nombre} duerme profundamente."
#         return "Rol desconocido."


# class GestorPartida:  
#     def __init__(self):
#         self.jugadores =[]

#     def anadirJugador(self, nombre, type):  
#         self.jugadores.append(JugadorJuego(nombre,type)) 
        
#     def VotacionDia(self, NombreVotado):
#         for jugador in self.jugadores:
#             if jugador.Nombre == NombreVotado:
#                 if jugador.esta_vivo:
#                     jugador.esta_vivo=False
#                     return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
#         return "Nadie fue linchado."    
        

#     def ComprobarVictoria(self):  
        
#         lista_jugador = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
#         dict_jugador = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
#         if lista_jugador >= dict_jugador:
#             return "¡Victoria de los Lobos!"
#         elif lista_jugador ==0:
#             return "¡Victoria de los Aldeanos!"
#         return "La partida debe continuar..."

# # --- Ejecución caótica ---
# juego=GestorPartida()
# juego.anadirJugador("Nacho", "lobo")
# juego.anadirJugador("Elena", "vidente")
# juego.anadirJugador("Carlos","aldeano")

# print(juego.jugadores[0].AccionNocturna(juego.jugadores[2]))
# print(juego.ComprobarVictoria())
from .Personajes.Jugador import JugadorJuego
from .Logica.GestorPartida import GestorPartida

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