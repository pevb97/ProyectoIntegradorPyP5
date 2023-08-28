from abc import ABC, abstractmethod

class GameObject():
    __pos_ant = None
    def __init__(self, lim_mapa: list, pos: list, pos_ant: list) -> None:
        self.__pos = list(pos)
        self.__limites = list(lim_mapa)
        self.__pos_ant = list(pos_ant)
    
    @property
    def posicion_anterior(self) -> list:
        return self.__pos_ant
    

    @posicion_anterior.setter
    def posicion_anterior(self, new_pos: list):
        self.__pos_ant = new_pos

    @property
    def posicion(self) -> list:
        return self.__pos
    
    
    @posicion.setter
    def posicion(self, new_pos: list):
        if (new_pos in self.__limites):
            self.__pos = new_pos
    
    
    @abstractmethod
    def move_object(self):
        pass
