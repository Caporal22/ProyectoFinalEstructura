class SubgenreNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, subgenre):
        if not self.head:
            self.head = SubgenreNode(subgenre)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = SubgenreNode(subgenre)

    def contains(self, subgenre):
        current = self.head
        while current:
            if current.name.lower() == subgenre.lower():
                return True
            current = current.next
        return False

class GenreGraph:
    def __init__(self):
        self.genres = {}

    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres[genre] = []

    def connect_genres(self, g1, g2):
        if g1 in self.genres and g2 in self.genres:
            self.genres[g1].append(g2)
            self.genres[g2].append(g1)

    def get_related_genres(self, genre):
        return self.genres.get(genre, [])

class DecisionTreeNode:
    def __init__(self, question=None, yes=None, no=None, result=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.result = result

    def ask(self):
        if self.result is not None:
            return self.result
        while True:
            answer = input(self.question + " (sí/no): ").strip().lower()
            if answer in ['sí', 'si']:
                return self.yes.ask()
            elif answer == 'no':
                return self.no.ask()
            else:
                print("Responde con 'sí' o 'no'.")

class Pelicula:
    def __init__(self, titulo, generos, subgeneros):
        self.titulo = titulo
        self.generos = generos
        self.subgeneros = subgeneros

peliculas_db = {
    "Inception": Pelicula("Inception", ["Ciencia Ficción", "Acción", "Suspenso"], LinkedList()),
    "Titanic": Pelicula("Titanic", ["Romance", "Drama", "Histórico"], LinkedList()),
    "Toy Story": Pelicula("Toy Story", ["Animación", "Comedia", "Familiar"], LinkedList()),
    "Interstellar": Pelicula("Interstellar", ["Ciencia Ficción", "Drama", "Espacial"], LinkedList()),
    "Avengers": Pelicula("Avengers", ["Acción", "Ciencia Ficción", "Superhéroes"], LinkedList()),
    "Coco": Pelicula("Coco", ["Animación", "Familiar", "Musical"], LinkedList()),
    "El Conjuro": Pelicula("El Conjuro", ["Terror", "Sobrenatural", "Suspenso"], LinkedList()),
    "La La Land": Pelicula("La La Land", ["Romance", "Drama", "Musical"], LinkedList()),
    "Gladiador": Pelicula("Gladiador", ["Acción", "Épica", "Histórico"], LinkedList()),
    "Frozen": Pelicula("Frozen", ["Animación", "Familiar", "Fantasía"], LinkedList()),
    "Joker": Pelicula("Joker", ["Psicológico", "Crimen", "Drama"], LinkedList()),
    "Gravedad": Pelicula("Gravedad", ["Ciencia Ficción", "Drama", "Espacial"], LinkedList()),
    "Harry Potter": Pelicula("Harry Potter", ["Fantasía", "Aventura", "Sobrenatural"], LinkedList()),
    "Spider-Man": Pelicula("Spider-Man", ["Acción", "Superhéroes", "Aventura"], LinkedList()),
    "Your Name": Pelicula("Your Name", ["Animación", "Romance", "Escolar"], LinkedList()),
}

peliculas_db["Inception"].subgeneros.append("Sueños")
peliculas_db["Titanic"].subgeneros.append("Tragedia")
peliculas_db["Toy Story"].subgeneros.append("Amistad")
peliculas_db["Interstellar"].subgeneros.append("Viajes espaciales")
peliculas_db["Avengers"].subgeneros.append("Héroes")
peliculas_db["Coco"].subgeneros.append("Música")
peliculas_db["El Conjuro"].subgeneros.append("Fantasmas")
peliculas_db["La La Land"].subgeneros.append("Baile")
peliculas_db["Gladiador"].subgeneros.append("Imperio Romano")
peliculas_db["Frozen"].subgeneros.append("Magia")
peliculas_db["Joker"].subgeneros.append("Locura")
peliculas_db["Gravedad"].subgeneros.append("Astronautas")
peliculas_db["Harry Potter"].subgeneros.append("Hechicería")
peliculas_db["Spider-Man"].subgeneros.append("Mutaciones")
peliculas_db["Your Name"].subgeneros.append("Destino")

genre_graph = GenreGraph()
for g in ["Acción", "Ciencia Ficción", "Romance", "Drama", "Terror", "Fantasía",
          "Animación", "Comedia", "Aventura", "Familiar", "Histórico", "Musical",
          "Suspenso", "Psicológico", "Sobrenatural", "Escolar", "Épica", "Crimen",
          "Espacial", "Superhéroes"]:
    genre_graph.add_genre(g)

genre_graph.connect_genres("Acción", "Aventura")
genre_graph.connect_genres("Ciencia Ficción", "Espacial")
genre_graph.connect_genres("Romance", "Drama")
genre_graph.connect_genres("Fantasía", "Sobrenatural")
genre_graph.connect_genres("Animación", "Familiar")
genre_graph.connect_genres("Musical", "Romance")
genre_graph.connect_genres("Suspenso", "Terror")
genre_graph.connect_genres("Superhéroes", "Acción")
genre_graph.connect_genres("Psicológico", "Crimen")

decision_tree = DecisionTreeNode(
    "¿Te gustan las películas con temas psicológicos?",
    yes=DecisionTreeNode(result="Psicológico"),
    no=DecisionTreeNode(
        "¿Prefieres películas con elementos sobrenaturales?",
        yes=DecisionTreeNode(result="Sobrenatural"),
        no=DecisionTreeNode(
            "¿Te interesan los conflictos históricos?",
            yes=DecisionTreeNode(result="Histórico"),
            no=DecisionTreeNode(result="Familiar")
        )
    )
)

def mostrar_menu_generos(grafo):
    print("------- MENÚ GÉNEROS -------")
    for i, genero in enumerate(grafo.genres.keys(), 1):
        print(f"{i}. {genero}")
    return list(grafo.genres.keys())

def seleccionar_generos(generos):
    elecciones = []
    while len(elecciones) < 3:
        try:
            seleccion = int(input(f"Selecciona el género #{len(elecciones)+1} (1-{len(generos)}): "))
            if 1 <= seleccion <= len(generos):
                elegido = generos[seleccion-1]
                if elegido not in elecciones:
                    elecciones.append(elegido)
                else:
                    print("⚠️ Ya seleccionaste ese género.")
            else:
                print("❗ Número fuera de rango.")
        except ValueError:
            print("❗ Ingresa un número válido.")
    return elecciones

def recomendar_peliculas():
    print("\nBienvenido al recomendador de películas \n")

    generos_disponibles = mostrar_menu_generos(genre_graph)
    generos_usuario = seleccionar_generos(generos_disponibles)

    print("\nResponde unas preguntas para afinar la recomendación:")
    subgenero_sugerido = decision_tree.ask()

    recomendaciones = []

    for pelicula in peliculas_db.values():
        coincidencias = len(set(pelicula.generos) & set(generos_usuario))
        if coincidencias > 0:
            prioridad = coincidencias
            if pelicula.subgeneros.contains(subgenero_sugerido):
                prioridad += 1
            recomendaciones.append((prioridad, pelicula.titulo))

    recomendaciones.sort(reverse=True)

    print("\nRecomendaciones personalizadas:")
    if recomendaciones:
        for prioridad, titulo in recomendaciones:
            print(f"- {titulo} (prioridad: {prioridad})")
    else:
        print("No se encontraron películas que coincidan con tus preferencias.")

if __name__ == "__main__":
    recomendar_peliculas()
