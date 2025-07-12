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
            answer = input(self.question + " (s/n): ").strip().lower()
            if answer in ['s']:
                return self.yes.ask()
            elif answer == 'n':
                return self.no.ask()
            else:
                print("Responde con 's' o 'n'.")

peliculas_db = {
    "Inception": Pelicula("Inception", ["Ciencia Ficción", "Acción", "Suspenso"]),
    "Titanic": Pelicula("Titanic", ["Romance", "Drama", "Histórico"]),
    "Toy Story": Pelicula("Toy Story", ["Animación", "Comedia", "Familiar"]),
    "Interstellar": Pelicula("Interstellar", ["Ciencia Ficción", "Drama", "Espacial"]),
    "Avengers": Pelicula("Avengers", ["Acción", "Ci1encia Ficción", "Superhéroes"]),
    "Coco": Pelicula("Coco", ["Animación", "Familiar", "Musical"]),
    "El Conjuro": Pelicula("El Conjuro", ["Terror", "Sobrenatural", "Suspenso"]),
    "La La Land": Pelicula("La La Land", ["Romance", "Drama", "Musical"]),
    "Gladiador": Pelicula("Gladiador", ["Acción", "Épica", "Histórico"]),
    "Frozen": Pelicula("Frozen", ["Animación", "Familiar", "Fantasía"]),
    "Joker": Pelicula("Joker", ["Psicológico", "Crimen", "Drama"]),
    "Gravedad": Pelicula("Gravedad", ["Ciencia Ficción", "Drama", "Espacial"]),
    "Harry Potter": Pelicula("Harry Potter", ["Fantasía", "Aventura", "Sobrenatural"]),
    "Spider-Man": Pelicula("Spider-Man", ["Acción", "Superhéroes", "Aventura"]),
    "Your Name": Pelicula("Your Name", ["Animación", "Romance", "Escolar"]),
    "Shrek": Pelicula("Shrek", ["Animación", "Comedia", "Aventura"]),
    "Parasite": Pelicula("Parasite", ["Comedia", "Drama", "Suspenso"]), 
    "Mad Max: Fury Road": Pelicula("Mad Max: Fury Road", ["Acción", "Ciencia Ficción", "Aventura"]), 
    "El Señor de los Anillos": Pelicula("El Señor de los Anillos", ["Fantasía", "Aventura", "Épica"]), 
    "Pulp Fiction": Pelicula("Pulp Fiction", ["Crimen", "Drama", "Comedia"]),
    "Forrest Gump": Pelicula("Forrest Gump", ["Drama", "Romance", "Histórico"]), 
    "Blade Runner 2049": Pelicula("Blade Runner 2049", ["Ciencia Ficción", "Drama", "Psicológico"]), 
    "V de Vendetta": Pelicula("V de Vendetta", ["Acción", "Drama", "Ciencia Ficción"]), 
    "Volver al Futuro": Pelicula("Volver al Futuro", ["Ciencia Ficción", "Comedia", "Aventura"]), 
    "Pesadilla en Elm Street": Pelicula("Pesadilla en Elm Street", ["Terror", "Sobrenatural", "Suspenso"]), 
}


peliculas_db["Inception"].agregar_subgenero("Aventura")
peliculas_db["Titanic"].agregar_subgenero("Acción")
peliculas_db["Toy Story"].agregar_subgenero("Fantasía")
peliculas_db["Interstellar"].agregar_subgenero("Aventura")
peliculas_db["Avengers"].agregar_subgenero("Aventura")
peliculas_db["Coco"].agregar_subgenero("Comedia")
peliculas_db["El Conjuro"].agregar_subgenero("Terror")
peliculas_db["La La Land"].agregar_subgenero("Musical")
peliculas_db["Gladiador"].agregar_subgenero("Acción")
peliculas_db["Frozen"].agregar_subgenero("Fantasía")
peliculas_db["Joker"].agregar_subgenero("Drama")
peliculas_db["Gravedad"].agregar_subgenero("Ciencia Ficción")
peliculas_db["Harry Potter"].agregar_subgenero("Fantasía")
peliculas_db["Spider-Man"].agregar_subgenero("Acción")
peliculas_db["Your Name"].agregar_subgenero("Drama")
peliculas_db["Shrek"].agregar_subgenero("Fantasía")
peliculas_db["Parasite"].agregar_subgenero("Drama")
peliculas_db["Mad Max: Fury Road"].agregar_subgenero("Ciencia Ficción")
peliculas_db["El Señor de los Anillos"].agregar_subgenero("Fantasía")
peliculas_db["Pulp Fiction"].agregar_subgenero("Acción")
peliculas_db["Forrest Gump"].agregar_subgenero("Drama")
peliculas_db["Blade Runner 2049"].agregar_subgenero("Acción")
peliculas_db["V de Vendetta"].agregar_subgenero("Drama")
peliculas_db["Volver al Futuro"].agregar_subgenero("Comedia")
peliculas_db["Pesadilla en Elm Street"].agregar_subgenero("Terror")


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
    "¿Disfrutas de peliculas con mucha adrenalina, donde hay explosiones y combates intensos?",
    yes=DecisionTreeNode(result="Acción"),
    no=DecisionTreeNode(
        "¿Te gusta ver personajes explorando mundos nuevos, superando grandes desafios o embarcándose en busqueda epicas?",
        yes=DecisionTreeNode(result="Aventura"),
        no=DecisionTreeNode(
            "¿Buscas peliculas que te hagan reír a carcajadas con situaciones expotaneas o dialogos ingeniosos?",
            yes=DecisionTreeNode(result="Comedia"),
            no=DecisionTreeNode(
                "¿Prefieres historias que te hagan reflexionar sobre las emociones humanas, las relaciones o los desafios de la vida real? ",
                yes=DecisionTreeNode(result="Drama"),
                no=DecisionTreeNode(    
                    "¿Te atraen las peliculas con conceptos futuristas, tecnologia avanzada o viajes espaciales?",
                    yes=DecisionTreeNode(result="Ciencia Ficción"),
                    no=DecisionTreeNode(
                        "¿Te sumerges facilmente en mundos de magia, criaturas miticas o hechizos?",
                        yes=DecisionTreeNode(result="Fantasía"),
                        no=DecisionTreeNode(
                            "¿Disfrutas de sentir el suspenso, los sobresaltos y el miedo?",
                            yes=DecisionTreeNode(result="Terror"),
                            no=DecisionTreeNode(result="Musical")
                        )
                    )
                )
            )
        )
    )
)

def mostrar_menu_generos(grafo):
    print("GÉNEROS DISPONIBLES:")
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
                    print("⚠ Ya seleccionaste ese género.")
            else:
                print(" Número fuera de rango.")
        except ValueError:
            print(" Ingresa un número válido.")
    return elecciones

def recomendar_peliculas():
    print("\n Bienvenido al recomendador de películas \n")

    generos_disponibles = mostrar_menu_generos(genre_graph)
    generos_usuario = seleccionar_generos(generos_disponibles)

    print("\n Responde unas preguntas para afinar la recomendación:")
    subgenero_sugerido = decision_tree.ask()

    recomendaciones = []

    for pelicula in peliculas_db.values():
        coincidencias = len(set(pelicula.generos) & set(generos_usuario))
        if coincidencias > 0:
            prioridad = coincidencias
            if pelicula.contiene_subgenero(subgenero_sugerido):  # Cambiado a contiene_subgenero
                prioridad += 1
            recomendaciones.append((prioridad, pelicula.titulo))

    recomendaciones.sort(reverse=True)

    print("\n Recomendaciones personalizadas:")
    if recomendaciones:
        for prioridad, titulo in recomendaciones:
            print(f"- {titulo} (prioridad: {prioridad})")
    else:
        print("⚠ No se encontraron películas que coincidan con tus preferencias.")

if __name__ == "__main__":
    recomendar_peliculas()
