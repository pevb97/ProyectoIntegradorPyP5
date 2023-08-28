from readchar import readkey, key
from juego import Juego
from mapa import Mapa
from playerObject import PlayerObject
from presentacion import Presentacion

def main():
    Presentacion.presentar(f'Bienvenido: {(Presentacion.capturar_dato("Ingresa tu nombre: "))}')
    Presentacion.presentar("Oprima Enter para iniciar")
    while (readkey() != (key.ENTER or key.ENTER_2)):
        pass
    salir = ""
    while (salir != (key.ESC or key.ESC_2)):
        mapa = Mapa("maps")
        player = PlayerObject(mapa.data_mapa.get("pos_camino"), mapa.data_mapa.get("pos_in"), mapa.data_mapa.get("pos_in"), "P")
        juego = Juego(mapa, player)
        juego.mapa.update_mapa(juego.objeto)
        while(juego.objeto.posicion != juego.mapa.data_mapa["pos_out"]):
            juego.objeto.move_object()
            juego.mapa.update_mapa(juego.objeto)
        
        Presentacion.presentar("Para continuar presione cualquier tecla \nSi desea terminar de jugar oprima Esc")
        salir = readkey()

main()