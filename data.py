from movie import Pelicula
from genre_graph import GenreGraph
from inverted_index import construir_inverted_index
from decision_tree import construir_arbol
from decision_data import arbol_data

# Árbol de decisiones
decision_tree = construir_arbol(arbol_data)

# Base de datos de películas
peliculas_db = {
    "Inception": Pelicula("Inception", ["Ciencia Ficción", "Acción", "Suspenso"]),
    "Titanic": Pelicula("Titanic", ["Romance", "Drama", "Histórico"]),
    "Toy Story": Pelicula("Toy Story", ["Animación", "Comedia", "Familiar"]),
    "Interstellar": Pelicula("Interstellar", ["Ciencia Ficción", "Drama", "Espacial"]),
    "Avengers": Pelicula("Avengers", ["Acción", "Ciencia Ficción", "Superhéroes"]),
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
    "V de Venganza": Pelicula("V de Venganza", ["Acción", "Drama", "Ciencia Ficción"]),
    "Volver al Futuro": Pelicula("Volver al Futuro", ["Ciencia Ficción", "Comedia", "Aventura"]),
    "Pesadilla en Elm Street": Pelicula("Pesadilla en Elm Street", ["Terror", "Sobrenatural", "Suspenso"]),
}

# Subgéneros extra
subgeneros_map = {
    "Inception": ["Aventura"],
    "Titanic": ["Acción"],
    "Toy Story": ["Fantasía"],
    "Interstellar": ["Aventura"],
    "Avengers": ["Aventura"],
    "Coco": ["Comedia"],
    "El Conjuro": ["Terror"],
    "La La Land": ["Musical"],
    "Gladiador": ["Acción"],
    "Frozen": ["Fantasía"],
    "Joker": ["Drama"],
    "Gravedad": ["Ciencia Ficción"],
    "Harry Potter": ["Fantasía"],
    "Spider-Man": ["Acción"],
    "Your Name": ["Drama"],
    "Shrek": ["Fantasía"],
    "Parasite": ["Drama"],
    "Mad Max: Fury Road": ["Ciencia Ficción"],
    "El Señor de los Anillos": ["Fantasía"],
    "Pulp Fiction": ["Acción"],
    "Forrest Gump": ["Drama"],
    "Blade Runner 2049": ["Acción"],
    "V de Venganza": ["Drama"],
    "Volver al Futuro": ["Comedia"],
    "Pesadilla en Elm Street": ["Terror"]
}

# Aqui aplicamos los subgeneros
for titulo, subgs in subgeneros_map.items():
    for s in subgs:
        peliculas_db[titulo].agregar_subgenero(s)

# Crear el grafo de géneros
genre_graph = GenreGraph()

# Lista completa de géneros
generos = [
    "Acción", "Ciencia Ficción", "Romance", "Drama", "Terror", "Fantasía",
    "Animación", "Comedia", "Aventura", "Familiar", "Histórico", "Musical",
    "Suspenso", "Psicológico", "Sobrenatural", "Escolar", "Épica", "Crimen",
    "Espacial", "Superhéroes"
]

# Agregamos al grafo
for genero in generos:
    genre_graph.add_genre(genero)

# Conexiones entre los géneros
conexiones = [
    ("Acción", "Aventura"),
    ("Ciencia Ficción", "Espacial"),
    ("Romance", "Drama"),
    ("Fantasía", "Sobrenatural"),
    ("Animación", "Familiar"),
    ("Musical", "Romance"),
    ("Suspenso", "Terror"),
    ("Superhéroes", "Acción"),
    ("Psicológico", "Crimen")
]

for g1, g2 in conexiones:
    genre_graph.connect_genres(g1, g2)

inverted_index = construir_inverted_index(peliculas_db)
