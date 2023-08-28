import os, random

class Mapa:

    def __init__(self, path: str):
        self.__dir_mapa = path + "/" + random.choice(os.listdir(path))
        self.__laberinto = self.__get_laberinto()
        self.__data_laberinto = self.__get_data_laberinto()
    
    @property
    def data_mapa(self)->dict:
        return self.__data_laberinto

    def __get_laberinto(self) -> list:
        with open(self.__dir_mapa, "r") as arc_laberinto:
            arc_laberinto = arc_laberinto.read()
            laberinto = list(arc_laberinto.split("\n"))
            for index_fila in range(0, len(laberinto)):
                laberinto[index_fila] = list(laberinto[index_fila])
            return laberinto
    
    
    def __get_pasillo_mapa(self)->list:
        #Obtencion de las posiciones dentro del laberinto que tienen pared
        pos_camino = list()
        for fila in range(len(self.__laberinto)):
            for columna in range(len(self.__laberinto[0])):
                if(self.__laberinto[fila][columna] == "."):
                    pos_camino.append([fila, columna])
        return pos_camino
    

    def __get_bordes_mapa(self):
        #Obtencion de las posiciones de los bordes del laberinto
        x_borde_izq_der = range(len(self.__laberinto))
        y_borde_izq = [0]*len(self.__laberinto)
        y_borde_der = [len(self.__laberinto[0])-1]*len(self.__laberinto)

        x_borde_sup = [0]*len(self.__laberinto[0])
        x_borde_inf = [len(self.__laberinto)-1]*len(self.__laberinto[0])
        y_borde_sup_inf = range(len(self.__laberinto[0]))

        pos_borde_izq = list(zip(x_borde_izq_der, y_borde_izq))
        pos_borde_der = list(zip(x_borde_izq_der, y_borde_der))
        pos_borde_sup = list(zip(x_borde_sup, y_borde_sup_inf))
        pos_borde_inf = list(zip(x_borde_inf, y_borde_sup_inf))
        pos_bordes_laberinto = pos_borde_izq + pos_borde_der + pos_borde_sup + pos_borde_inf
        return pos_bordes_laberinto


    def __get_in_out_mapa(self, bordes: list)->list:
        #Obtencion de las posiciones en las que existe una entrada o salida del laberinto
        pos_in_out = list()
        for i in bordes:
            if self.__laberinto[(i[0])][(i[1])] == ".":
                pos_in_out.append(i)
        return pos_in_out
    
    
    def __get_data_laberinto(self):
        in_out_mapa = self.__get_in_out_mapa(self.__get_bordes_mapa())
        info_laberinto ={
            "pos_camino": self.__get_pasillo_mapa(),
            "pos_in": list(in_out_mapa[0]),
            "pos_out": list(in_out_mapa[1]),
        }
        return info_laberinto
    

    def update_mapa(self, obj: object):
        self.__laberinto[obj.posicion_anterior[0]][obj.posicion_anterior[1]] = "."
        self.__laberinto[obj.posicion[0]][obj.posicion[1]] = obj.representacion
        self.visualizacion_mapa()
    
    
    def visualizacion_mapa(self):
        os.system('cls' if os.name=='nt' else 'clear')
        laberinto_print = ""
        for fila in self.__laberinto:
            laberinto_print += "\n"
            for columna in fila:
                laberinto_print += str(columna)
        print(laberinto_print)
