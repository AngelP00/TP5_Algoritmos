from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    contar_heroes_villanos,
)

arbol = nodoArbol()


#heroes = nodoArbol()
#villanos = nodoArbol()


lista = [
    ['iron man', False, 1960],
    ['capitana marvel', False, 1890],
    ['thor', False, 1962],
    ['dotor strange', False, 1961],
    ['aquaman', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
]

for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}
    
    insertar_nodo(arbol, nombre, datos)

# inorden_heroes_villanos(arbol)
# print()
# inorden_villano(arbol)
# print()
# inorden_empieza_con(arbol, 'c')
# print()
# print(contar_heroes(arbol))

# crear_bosque(arbol, heroes, villanos)
# while not arbol_vacio(arbol):
#     info, datos = eliminar_nodo(arbol, arbol['info'])
#     print(info, datos)
#     if datos['villano'] == True:
#         insertar_nodo(villanos, info)
#     else:
#         insertar_nodo(heroes, info)
#cantidad = {'villanos': 0, 'heroes': 0}
#contar_heroes_villanos(arbol, cantidad)
#print('cantidad de heroes y villanos', cantidad)


#print('heroes:')
#inorden(heroes)
#print()

#print('villanos:')
#inorden(villanos)
#print()

#print('arbol completo:')
#inorden(arbol)
#print()


#print(eliminar_nodo(arbol, 'spider-man'))
#print(eliminar_nodo(arbol, 'dotor strange'))


# clave = input('ingrese parte de lo que desea buscar ')
# inorden_empieza_con(arbol, clave)
# print()
# clave = input('ingrese nombre que desea modificar ')
# pos = eliminar_nodo(arbol, clave)
# if pos:
#     name = input('ingrese nuevo nombre ')
#     insertar_nodo(arbol, name, False)
# else:
#     print('valor no encontrado en el arbol')

# inorden(arbol)
# print()

# postorden_heroes(arbol)

print()   
print('5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe(MCU), desarrollar un algoritmo que contemple lo siguiente:')

print()   
print('a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;')
print('Arbol completo:')
inorden(arbol)

print()
print('b. listar los villanos ordenados alfabéticamente;')
def inorden_villano(arbol):
    if(arbol is not None):
        inorden_villano(arbol['izq'])
        if arbol['datos']['villano'] == True:
            print(arbol['info'])
        inorden_villano(arbol['der'])

inorden_villano(arbol)

print()
print('c. mostrar todos los superhéroes que empiezan con C;')
inorden_empieza_con(arbol, 'C')

print()
print('d. determinar cuántos superhéroes hay en el árbol;')
contadores = {
        'cant_heroes': 0,
        'cant_villanos': 0,
    }

def cantidad_de_heroes_y_villanos(arbol, contadores):
    if(arbol is not None):
        cantidad_de_heroes_y_villanos(arbol['izq'], contadores)
        if arbol['datos']['villano'] == True:
            print(arbol['info'])
            contadores['cant_villanos']+=1
        else:
            contadores['cant_heroes']+=1
        cantidad_de_heroes_y_villanos(arbol['der'], contadores)

cantidad_de_heroes_y_villanos(arbol, contadores)
#print(contadores)
print('En el arbol hay', contadores['cant_heroes'], 'heroes')


print()
print('e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;')

print()
clave = input('ingrese parte de lo que desea buscar:')
inorden_empieza_con(arbol, clave)

print()
clave = input('ingrese el nombre que desea modificar:')
pos = eliminar_nodo(arbol, clave)

#print(pos)
if pos[0] is not None:
    name = input('ingrese nuevo nombre:')
    insertar_nodo(arbol, name, False)
else:
    print('valor no encontrado en el arbol')

inorden(arbol)
print()

print()
print('f. listar los superhéroes ordenados de manera descendente;')

#inorden(arbol)
def listar_heroes_de_manera_descendente(arbol):
    if(arbol is not None):
        listar_heroes_de_manera_descendente(arbol['der'])
        if arbol['datos']['villano'] == False:
            print(arbol['info'])
        listar_heroes_de_manera_descendente(arbol['izq'])
        
print()
listar_heroes_de_manera_descendente(arbol)


print()
print('g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:')
arbol_heroes = nodoArbol()
arbol_villanos = nodoArbol()
def crear_bosque_de_heroes_y_villanos(arbol, bosque1, bosque2):
    if(arbol is not None):
        crear_bosque_de_heroes_y_villanos(arbol['izq'], bosque1, bosque2)
        if arbol['datos']['villano'] == True:
            insertar_nodo(bosque2, arbol['info'])
        else:
            insertar_nodo(bosque1, arbol['info'])
        crear_bosque_de_heroes_y_villanos(arbol['der'], bosque1, bosque2)

crear_bosque_de_heroes_y_villanos(arbol,arbol_heroes,arbol_villanos)
#inorden(heroes)
#inorden(villanos)

print()
print('I. determinar cuántos nodos tiene cada árbol;')
def cantidad_de_nodos_del_arbol(arbol, cant_nodos):
    if(arbol is not None):
        cantidad_de_nodos_del_arbol(arbol['izq'],cant_nodos)
        cant_nodos['cant_nodos']+=1
        cantidad_de_nodos_del_arbol(arbol['der'],cant_nodos)

dic_cant_nodos_heroes = {'cant_nodos': 0,}
cantidad_de_nodos_del_arbol(arbol_heroes,dic_cant_nodos_heroes)
print('El arbol de heroes tiene',dic_cant_nodos_heroes['cant_nodos'],'nodos')

dic_cant_nodos_villanos = {'cant_nodos': 0,}
cantidad_de_nodos_del_arbol(arbol_villanos,dic_cant_nodos_villanos)
print('El arbol de villanos tiene',dic_cant_nodos_villanos['cant_nodos'],'nodos')


print()
print('II. realizar un barrido ordenado alfabéticamente de cada árbol.')
print('Arbol heroes:')
inorden(arbol_heroes)
print()
print('Arbol villanos:')
inorden(arbol_villanos)