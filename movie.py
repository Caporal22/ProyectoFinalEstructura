class Pelicula:
    def __init__(self, titulo, generos):
        self.titulo = titulo
        self.generos = generos
        self.subgeneros = []

    def agregar_subgenero(self, subgenero):
        if subgenero not in self.subgeneros:
            self.subgeneros.append(subgenero)

    def contiene_subgenero(self, subgenero):
        return subgenero.lower() in [s.lower() for s in self.subgeneros]
