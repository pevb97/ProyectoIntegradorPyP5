import os
from readchar import readkey, key

class Presentacion:
    MOVS = {key.UP: "U", key.DOWN: "D", key.RIGHT: "R", key.LEFT: "L"}
    
    
    @staticmethod
    def presentar_mapa(laberinto: list):
        os.system('cls' if os.name=='nt' else 'clear')
        laberinto_print = ""
        for fila in laberinto:
            laberinto_print += "\n"
            for columna in fila:
                laberinto_print += str(columna)
        print(laberinto_print)


    @staticmethod
    def presentar(msg: str):
        os.system('cls' if os.name=='nt' else 'clear')
        print(str(msg))


    @staticmethod
    def presentar_opcion(path: str):
        os.system('cls' if os.name=='nt' else 'clear')
        print (dict(zip(range(len(path)), os.listdir(path))))


    @staticmethod
    def capturar_dato(msg: str):
        os.system('cls' if os.name=='nt' else 'clear')
        return str(input(msg))


    @staticmethod
    def capturar_mov():
        print("Los movimientos se realizan con las flechas")
        mov = readkey()
        return Presentacion.MOVS[mov] if (mov in Presentacion.MOVS) else Presentacion.capturar_mov()

