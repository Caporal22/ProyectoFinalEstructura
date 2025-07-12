##########
class NodoPuntaje:
    def __init__(self, pelicula, puntaje):
        self.pelicula = pelicula
        self.puntaje = puntaje
        self.izq = None
        self.der = None

class ArbolPuntaje:
    def __init__(self):
        self.raiz = None

    def insertar(self, pelicula, puntaje):
        self.raiz = self._insertar_rec(self.raiz, pelicula, puntaje)

    def _insertar_rec(self, nodo, pelicula, puntaje):
        if nodo is None:
            return NodoPuntaje(pelicula, puntaje)
        if puntaje < nodo.puntaje:
            nodo.izq = self._insertar_rec(nodo.izq, pelicula, puntaje)
        else:
            nodo.der = self._insertar_rec(nodo.der, pelicula, puntaje)
        return nodo

    def recorrer_descendente(self, nodo=None, resultados=None):
        if resultados is None:
            resultados = []
        if nodo is None:
            nodo = self.raiz
        if nodo:
            self.recorrer_descendente(nodo.der, resultados)
            resultados.append((nodo.pelicula, nodo.puntaje))
            self.recorrer_descendente(nodo.izq, resultados)
        return resultados



