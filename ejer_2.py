# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
#algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
#cantidad de episodios en los que aparecieron juntos ambos personajes que se
#relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes,
# d) ue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, 
#Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
# e) camino mas corto desde Yoda a Rey

from lista import Lista as ListaArista
from cola import Cola
from pila import Pila
from heap_min import Heap
from random import randint

class Arista:

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

    def __str__(self):
        return f"{self.vertice} {self.peso}"

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')

class Grafo():

    def __init__(self, dirigido=True):
        self.__elements = []
        self.dirigido = dirigido

    def insert_vertice(self, value, criterio=None):
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaArista(), False])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaArista(), False])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaArista(), False])

    def insert_arist(self, vertice_ori, vertice_des, peso, criterio_vertice=None, criterio_arista='vertice'):
        origen = self.search_vertice(vertice_ori, criterio_vertice)
        destino = self.search_vertice(vertice_des, criterio_vertice)
        if origen is not None and destino is not None:
            self.get_element_by_index(origen)[1].insert(Arista(vertice_des, peso), criterio_arista)
            if not self.dirigido:
                self.get_element_by_index(destino)[1].insert(Arista(vertice_ori, peso), criterio_arista)

    def search_vertice(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def delete_vertice(self, value, criterio=None):
        return_value = None
        pos = self.search_vertice(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
            for vertice in self.__elements:
                vertice[1].delete(value, 'vertice')

        return return_value

    def delete_arista(self, origen, destino):
        pos_origen = self.search_vertice(origen)
        if pos_origen is not None:
            ver_origen = self.get_element_by_index(pos_origen)
            delete = ver_origen[1].delete(destino, 'vertice')
            if not self.dirigido:
                pos_destino = self.search_vertice(destino)
                if pos_destino is not None:
                    ver_destino = self.get_element_by_index(pos_destino)
                    ver_destino[1].delete(origen, 'vertice')
            return delete

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value[0])
            print('Arsitas --------------------')
            value[1].barrido()
            print()
    
    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                print(buscado, arbol)
                if buscado in arbol:
                    return index

        bosque = []
        aristas = Heap()
        for index in range(self.size()):
            vertice = self.get_element_by_index(index)
            bosque.append(criterio_comparacion(vertice[0], 'nombre'))
            aristas_adjacentes = vertice[1]
            for i in range(aristas_adjacentes.size()):
                arista = aristas_adjacentes.get_element_by_index(i)
                aristas.arrive([vertice[0], arista.vertice], arista.peso)

        while len(bosque) > 1 and aristas.size() > 0:
            arista = aristas.atention()
            origen = buscar_en_bosque(bosque, criterio_comparacion(arista[1][0], 'nombre'))
            destino = buscar_en_bosque(bosque, criterio_comparacion(arista[1][1], 'nombre'))
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')

        return bosque


mi_grafo = Grafo(dirigido=False)

# a)
mi_grafo.insert_vertice("Luke Skywaljer"),
mi_grafo.insert_vertice("Darth Vader"),
mi_grafo.insert_vertice("Yoda"),
mi_grafo.insert_vertice("Boba Fett"),
mi_grafo.insert_vertice("C-3PO"),
mi_grafo.insert_vertice("Leia"),
mi_grafo.insert_vertice("Rey"),
mi_grafo.insert_vertice("Kylo Ren"),
mi_grafo.insert_vertice("Chewbacca"),
mi_grafo.insert_vertice("Han Solo"),
mi_grafo.insert_vertice("R2-D2"),
mi_grafo.insert_vertice("BB-8"),


mi_grafo.insert_arist("Luke Skywalker", "Darth Vader", 5, 'nombre')
mi_grafo.insert_arist("Luke Skywalker", "Leia", 3, 'nombre')
mi_grafo.insert_arist("Luke Skywalker", "Han Solo", 4, 'nombre')
mi_grafo.insert_arist("Luke Skywalker", "Chewbacca", 2, 'nombre')
mi_grafo.insert_arist("Darth Vader", "Leia", 2, 'nombre')
mi_grafo.insert_arist("Darth Vader", "Chewbacca", 1, 'nombre')
mi_grafo.insert_arist("Darth Vader", "Boba Fett", 3, 'nombre')
mi_grafo.insert_arist("Yoda", "Rey", 6, 'nombre')
mi_grafo.insert_arist("Yoda", "Kylo Ren", 4, 'nombre')
mi_grafo.insert_arist("Boba Fett", "C-3PO", 2, 'nombre')
mi_grafo.insert_arist("C-3PO", "R2-D2", 1, 'nombre')
mi_grafo.insert_arist("Leia", "Han Solo", 5, 'nombre')
mi_grafo.insert_arist("Rey", "Kylo Ren", 3, 'nombre')
mi_grafo.insert_arist("Chewbacca", "Han Solo", 4, 'nombre')
mi_grafo.insert_arist("R2-D2", "BB-8", 2, 'nombre')

# b)
bosque = mi_grafo.kruskal()

yoda_presente = any('Yoda' in componente for componente in bosque)

if yoda_presente:
    print("El árbol de expansión mínimo contiene a Yoda.")
else:
    print("El árbol de expansión mínimo no contiene a Yoda.")

# c)
max_episodios = 0

for vertice in mi_grafo.elements:
    aristas = vertice[1]
    for i in range(aristas.size()):
        episodios = aristas.get_element_by_index(i).peso
        if episodios > max_episodios:
            max_episodios = episodios

print("El número máximo de episodios que comparten dos personajes es:", max_episodios)

# e)
def camino_mas_corto(desde, hasta):
    cola_pendientes = Cola()
    cola_pendientes.arrive(desde)
    padres = {desde: None}

    while not cola_pendientes.size() == 0:
        vertice = cola_pendientes.atention()
        if vertice == hasta:
            camino = [hasta]
            while padres[hasta] is not None:
                camino.insert(0, padres[hasta])
                hasta = padres[hasta]
            return camino

        for arista in mi_grafo.get_element_by_index(mi_grafo.search_vertice(vertice))[1]:
            vecino = arista.vertice
            if vecino not in padres:
                padres[vecino] = vertice
                cola_pendientes.arrive(vecino)

    return None

camino_yoda_a_rey = camino_mas_corto("Yoda", "Rey")

if camino_yoda_a_rey:
    print("Camino más corto desde Yoda hasta Rey:", camino_yoda_a_rey)
else:
    print("No hay un camino desde Yoda hasta Rey.")
