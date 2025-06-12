from data import peliculas_db, genre_graph, decision_tree
from colorama import init, Fore, Back, Style
init()


def mostrar_menu_generos(grafo):
    print(Fore.GREEN + Style.BRIGHT + "   ----------   MENÚ GENEROS   ---------- \n"+ Style.RESET_ALL)
    for i, genero in enumerate(grafo.graph.keys(), 1):
        print(f"{i}. {genero}")
    return list(grafo.graph.keys())

def seleccionar_generos(generos):
    elecciones = []
    print()
    while len(elecciones) < 3:
        try:
            seleccion = int(input(f"Selecciona el género #{len(elecciones)+1} (1-{len(generos)}): "))
            if 1 <= seleccion <= len(generos):
                elegido = generos[seleccion-1]
                if elegido not in elecciones:
                    elecciones.append(elegido)
                else:
                    print("  >Ya seleccionaste ese género.")
            else:
                print("  >Número fuera de rango.")
        except ValueError:
            print("  >Ingresa un número válido.")
    return elecciones

def recomendar_peliculas():
    print(Style.BRIGHT + Back.GREEN + "\n\n\n            BIENVENIDO A MOVIEMATCH            \n" + Style.RESET_ALL)

    generos_disponibles = mostrar_menu_generos(genre_graph)
    generos_usuario = seleccionar_generos(generos_disponibles)

    print(Fore.BLACK + Back.CYAN + Style.BRIGHT + "\n              RESPONDE UNAS PREGUNTAS              " + Style.RESET_ALL)
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

    print(Fore.BLACK + Back.MAGENTA + Style.BRIGHT + "\n           RECOMENDACIONES DE PELICULAS            \n" + Style.RESET_ALL)
    if recomendaciones:
        for prioridad, titulo in recomendaciones:
            print(f"   - {titulo} (prioridad: {prioridad})")
    else:
        print("No se encontraron películas que coincidan con tus preferencias.")

if __name__ == "__main__":
    recomendar_peliculas()
