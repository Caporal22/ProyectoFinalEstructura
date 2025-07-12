from data import peliculas_db, genre_graph, decision_tree


def mostrar_menu_generos(grafo):
    print("\nGÉNEROS DISPONIBLES:")
    for i, genero in enumerate(grafo.graph.keys(), 1):
        print(f"{i}. {genero}")
    return list(grafo.graph.keys())

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
                    print("Ya seleccionaste ese género.")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Ingresa un número válido.")
    return elecciones

def recomendar_peliculas():
    print("\n=== RECOMENDADOR DE PELÍCULAS ===")

    generos_disponibles = mostrar_menu_generos(genre_graph)
    generos_usuario = seleccionar_generos(generos_disponibles)

    print("\nRESPONDE ALGUNAS PREGUNTAS PARA PERSONALIZAR AÚN MÁS:")
    subgenero_sugerido = decision_tree.ask()

    recomendaciones = []
    for pelicula in peliculas_db.values():
        coincidencias = len(set(pelicula.generos) & set(generos_usuario))
        if coincidencias > 0:
            prioridad = coincidencias
            if pelicula.contiene_subgenero(subgenero_sugerido):
                prioridad += 1
            recomendaciones.append((prioridad, pelicula.titulo))

    recomendaciones.sort(reverse=True)

    print("\nRECOMENDACIONES PERSONALIZADAS:")
    if recomendaciones:
        for prioridad, titulo in recomendaciones:
            print(f"- {titulo} (prioridad: {prioridad})")
    else:
        print("No se encontraron películas que coincidan con tus preferencias.")

if __name__ == "__main__":
    recomendar_peliculas()
