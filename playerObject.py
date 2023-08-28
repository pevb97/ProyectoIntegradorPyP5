from gameObject import GameObject
from readchar import readkey, key

class PlayerObject(GameObject):
    MOVS = [key.UP, key.DOWN, key.RIGHT , key.LEFT]

    def __init__(self, lim_mapa: list, pos: list, pos_ant, repre: any) -> None:
        super().__init__(lim_mapa, pos, pos_ant)
        self.__repre = repre
        

    @property
    def representacion(self) -> list:
        return self.__repre
    

    def __capture_mov(self):
        print("Los movimientos se realizan con las flechas")
        mov = readkey()
        return mov if (mov in self.MOVS) else self.__capture_mov()
    
    
    def move_object(self):
        movement = self.__capture_mov()
        self.posicion_anterior = self.posicion
        if movement == self.MOVS[0]:
            self.posicion = [(self.posicion[0]-1), self.posicion[1]]
        elif movement == self.MOVS[1]:
            self.posicion = [(self.posicion[0]+1), self.posicion[1]]
        elif movement == self.MOVS[2]:
            self.posicion = [(self.posicion[0]), self.posicion[1]+1]
        elif movement == self.MOVS[3]:
            self.posicion = [(self.posicion[0]), self.posicion[1]-1]
