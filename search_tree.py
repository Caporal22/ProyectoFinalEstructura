"""
search_tree.py
Módulo de búsqueda. Creación de un árbol binario para el ordenamiento y sugerencia
de películas tomando en cuenta la puntuación obtenidas
"""

class TreeNode:
    """
    Representa el nodo del árbol.
    Contiene metodos de inserción por medio de las recomendaciones y puntuaciones
    """
    def __init__(self, movie, score):
        """
        Nuestro constructor de la clase TreeNode

        Keyword arguments:
        :param movie: -- dict que contiene los datos de las películas
        :param score: -- float que contiene puntuaciones de las películas
        """
        self.movie = movie
        self.score = score
        self.left = None
        self.right = None



class MovieTree:
    """
    Árbol de búsqueda binaria donde vamos a insertar películas ordenadas por puntuación (score)
    """

    def __init__(self):
        """
        Constructor de la clase, inicializamos el árbol vacío
        """
        self.root = None 

    def insert(self, movie, score):
        """
        Inserta una nueva película al árbol, en posición según su puntuación

        Keyword arguments:
        :param movie: dict -- película a insertar
        :param score: float -- puntación de la película
        :return: No return
        """
        self.root = self._insert_recursive(self.root, movie, score)

    def _insert_recursive(self, node, movie, score):
        """
        Método recursivo para insertar películas

        Keyword arguments:
        :param node: Nodo en el que estamos
        :param movie: dict -- pelicula a insertar
        :param score: float -- puntuación de la pelicula
        :return: Nodo actualizado
        """
        if node is None:
            return TreeNode(movie, score)
        if score < node.score:
            node.left = self._insert_recursive(node.left, movie, score)
        else:
            node.right = self._insert_recursive(node.right, movie, score)
        return node

    def in_order(self):
        """
        Método de recorrido in-orden a las puntuaciones (menor a mayor)

        Keyword arguments:
        :return: pelicula y puntuaciones ordenadas
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        """
        Método cursivo del método in_orden

        Keyword arguments:
        :param node: Nodo en el que estamos
        :param result: Lista donde guardamos películas ordenadas
        :return: No return
        """
        if node:
            self._in_order_recursive(node.left, result)
            result.append((node.movie, node.score))
            self._in_order_recursive(node.right, result)


tree = MovieTree()
tree.insert({"title": "Kraven"}, 80)
tree.insert({"title": "Hotel Transilvania"}, 70)
tree.insert({"title": "En el abismo"}, 90)

print(tree.in_order())

