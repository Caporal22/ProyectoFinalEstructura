class NodoDecision:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

    def es_hoja(self):
        return self.si is None and self.no is None

    def ask(self):
        if self.es_hoja():
            return self.pregunta
        respuesta = input(self.pregunta + " (s/n): ").strip().lower()
        if respuesta == 's':
            return self.si.ask()
        elif respuesta == 'n':
            return self.no.ask()
        else:
            print("Por favor responde con 's' o 'n'.")
            return self.ask()

def recorrer_arbol(nodo):
    while not nodo.es_hoja():
        respuesta = input(nodo.pregunta + " (s/n): ").strip().lower()
        if respuesta == 's':
            nodo = nodo.si
        elif respuesta == 'n':
            nodo = nodo.no
        else:
            print("Por favor responde con 's' o 'n'.")
    return nodo.pregunta

def construir_arbol(data):
    if isinstance(data, str):
        return NodoDecision(data)
    pregunta = next(iter(data))
    opciones = data[pregunta]
    si = construir_arbol(opciones['s'])
    no = construir_arbol(opciones['n'])
    return NodoDecision(pregunta, si=si, no=no)

