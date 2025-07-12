class GenreGraph:
    def __init__(self):
        self.graph = {}

    def add_genre(self, genre):
        if genre not in self.graph:
            self.graph[genre] = set()

    def connect_genres(self, g1, g2):
        self.add_genre(g1)
        self.add_genre(g2)
        self.graph[g1].add(g2)
        self.graph[g2].add(g1)

    def get_neighbors(self, genre):
        return self.graph.get(genre, set())
