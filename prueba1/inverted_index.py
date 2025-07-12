def construir_inverted_index(peliculas_db):
    index = {}
    for pelicula in peliculas_db.values():
        for genero in pelicula.generos:
            index.setdefault(genero, []).append(pelicula)
    return index

{'accion': ['inception', ],

'ciencia_ficcion': ['Titanic'],

 'fantasia':[]

 }
