from mapa import Mapa
from playerObject import PlayerObject

class Juego:
    def __init__(self, mapa: Mapa, objeto: PlayerObject):
        self.mapa = mapa
        self.objeto = objeto
