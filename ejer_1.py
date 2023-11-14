# Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, 
#planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        def __insert(root, value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)

            return root

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if(self.root is not None):
            __postorden(self.root)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

arbol = BinaryTree()

class Pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo

class Pokedex:
    def __init__(self):
        self.arbol_nombre = BinaryTree()
        self.arbol_numero = BinaryTree()
        self.arbol_tipo = BinaryTree()

    def insert_pokemon(self, pokemon):
        self.arbol_nombre.insert_node(pokemon.nombre)
        self.arbol_numero.insert_node(pokemon.numero)
        self.arbol_tipo.insert_node(pokemon.tipo)

    def search_by_name(self, key):
        return self.arbol_nombre.search(key)

    def search_by_number(self, key):
        return self.arbol_numero.search(key)

    def search_by_type(self, key):
        return self.arbol_tipo.search(key)

    def count_pokemons_by_type(self, tipo):
        count = [0]

        def __count_by_type(root, tipo):
            if root is not None:
                if tipo.lower() in root.value.lower():
                    count[0] += 1
                __count_by_type(root.left, tipo)
                __count_by_type(root.right, tipo)

        if self.arbol_tipo.root is not None:
            __count_by_type(self.arbol_tipo.root, tipo.lower())

        return count[0]

    def show_all_data_by_name(self, key):
        def __show_by_name(root, key):
            if root is not None:
                if key.lower() in root.value.lower():
                    print(f"Datos del Pokémon con nombre que contiene '{key}': {root.value}")
                __show_by_name(root.left, key)
                __show_by_name(root.right, key)

        if self.arbol_nombre.root is not None:
            __show_by_name(self.arbol_nombre.root, key.lower())

    def show_all_names_by_type(self, tipo):
        def __show_by_type(root, tipo):
            if root is not None:
                if tipo.lower() in root.value.lower():
                    print(f"Nombre del Pokémon de tipo '{tipo}': {root.value}")
                __show_by_type(root.left, tipo)
                __show_by_type(root.right, tipo)

        if self.arbol_tipo.root is not None:
            __show_by_type(self.arbol_tipo.root, tipo.lower())

    def list_all_pokemons(self):
        print("Listado en orden ascendente por número:")
        self.arbol_numero.inorden()
        print("Listado en orden ascendente por nombre:")
        self.arbol_nombre.inorden()

    def list_all_pokemons_by_level(self):
        print("Listado por nivel por nombre:")
        self.arbol_nombre.by_level()

pokedex = Pokedex()

# a)
pokedex.insert_pokemon(Pokemon("Blaziken",257, ["Fuego", "Lucha"]))
pokedex.insert_pokemon(Pokemon("Ivysaur",2, ["Planta", "Veneno"]))
pokedex.insert_pokemon(Pokemon("Jolteon",135, ["Electrico"]))
pokedex.insert_pokemon(Pokemon("Lycanroc",745, ["Roca"]))
pokedex.insert_pokemon(Pokemon("Tyrantrum",697, ["Dragón"]))
pokedex.insert_pokemon(Pokemon("Bulbasaur",1, ["Planta", "Veneno"]))
pokedex.insert_pokemon(Pokemon("Steelix",208, ["Acero", "Tierra"]))
pokedex.insert_pokemon(Pokemon("Empoleon",395,["Agua", "Acero"]))
pokedex.insert_pokemon(Pokemon("Shaymin",492,["Planta"]))
pokedex.insert_pokemon(Pokemon("Palpitoad",536,["Agua", "Tierra"]))
pokedex.insert_pokemon(Pokemon("Dusknoir",477,["Fantasma"]))
pokedex.insert_pokemon(Pokemon("Luxray",405,["Electrico"]))
pokedex.insert_pokemon(Pokemon("Roserade",407,["Planta", "Veneno"]))
pokedex.insert_pokemon(Pokemon("Metagross",376,["Acero", "Psiquico"]))
pokedex.insert_pokemon(Pokemon("Hitmonchan",107,["Lucha"]))

# b)
pokedex.show_all_data_by_name("Jolteon")

# c)
pokedex.show_all_names_by_type("Agua")
pokedex.show_all_names_by_type("Fuego")
pokedex.show_all_names_by_type("Planta")
pokedex.show_all_names_by_type("Electrico")

# d)
pokedex.list_all_pokemons()

# e)
pokemon_jolteon = pokedex.search_by_name("Jolteon")
if pokemon_jolteon:
    print("Datos de Jolteon:", pokemon_jolteon.value)
else:
    print("Jolteon no encontrado en la Pokedex")
pokemon_lycanroc = pokedex.search_by_name("Lycanroc")
if pokemon_lycanroc:
    print("Datos de Lycanroc:", pokemon_lycanroc.value)
else:
    print("Lycanroc no encontrado en la Pokedex")

pokemon_tyrantrum = pokedex.search_by_name("Tyrantrum")
if pokemon_tyrantrum:
    print("Datos de Tyrantrum:", pokemon_tyrantrum.value)
else:
    print("Tyrantrum no encontrado en la Pokedex")

# f)
count_electric = pokedex.count_pokemons_by_type("Electrico")
print(f"Cantidad de Pokémon de tipo Eléctrico: {count_electric}")

count_steel = pokedex.count_pokemons_by_type("Acero")
print(f"Cantidad de Pokémon de tipo Acero: {count_steel}")
