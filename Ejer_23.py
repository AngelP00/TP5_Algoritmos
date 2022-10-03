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
    inorden_con_datos,
    busqueda,
    inorden_por_coincidencia,
    por_nivel,
)

arbol = nodoArbol()


#heroes = nodoArbol()
#villanos = nodoArbol()



#    Criatura, Derrotado por
lista = [
    ['Ceto', '-'],
    ['Tifon', 'Zeus'],
    ['Equidna', 'Argos Panoptes'],
    ['Dino', '-'],
    ['Pefredo', '-'],
    ['Enio', '-'],
    ['Escila', '-'],
    ['Caribdis', '-'],
    ['Euríale', '-'],
    ['Esteno', '-'],
    ['Medusa', 'Perseo'],
    ['Ladón', 'Heracles'],
    ['Águila del Cáucaso', '-'],
    ['Quimera', 'Belerofonte'],
    ['Hidra de Lerna', 'Heracles'],
    ['León de Nemea', 'Heracles'],
    ['Esfinge', 'Edipo'],
    ['Dragón de la Cólquida', '-'],
    ['Cerbero', '-'],
    ['Cerda de Cromión', 'Teseo'],
    ['Ortro', 'Heracles'],
    ['Toro de Creta', 'Teseo'],
    ['Jabalí de Calidón', 'Atalanta'],
    ['Carcinos', '-'],
    ['Gerión', 'Heracles'],
    ['Cloto', '-'],
    ['Láquesis', '-'],
    ['Átropos', '-'],
    ['Minotauro de Creta', 'Teseo'],
    ['Harpías', '-'],
    ['Argos Panoptes', 'Hermes'],
    ['Aves del Estínfalo', '-'],
    ['Talos', 'Medea'],
    ['Sirenas', '-'],
    ['Pitón', 'Apolo'],
    ['Cierva de Cerinea', '-'],
    ['Basilisco', '-'],
    ['Jabalí de Erimanto', '-'],
]

for nombre_criatura, derrotada_por in lista:
    datos = {'descripcion': None,
             'derrotada_por': derrotada_por.title(),
             'capturada_por':None,}
    
    insertar_nodo(arbol, nombre_criatura.title(), datos)

# inorden_heroes_villanos(arbol)
# print()
# inorden_villano(arbol)
# print()
# inorden_empieza_con(arbol, 'c')
# print()
# print(contar_heroes(arbol))


print()
print('23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:')
#inorden(arbol)

def cantidad_de_nodos_del_arbol(arbol, cant_nodos):
    if(arbol is not None):
        cantidad_de_nodos_del_arbol(arbol['izq'],cant_nodos)
        cant_nodos['cant_nodos']+=1
        cantidad_de_nodos_del_arbol(arbol['der'],cant_nodos)

dic_cant_nodos_criaturas = {'cant_nodos': 0,}
cantidad_de_nodos_del_arbol(arbol, dic_cant_nodos_criaturas)
print('El arbol de criaturas tiene', dic_cant_nodos_criaturas['cant_nodos'],'nodos')

print()
print('a. listado inorden de las criaturas y quienes la derrotaron;')
#inorden_con_datos(arbol)
def inorden_de_criaturas(arbol):
    if(arbol is not None):
        inorden_de_criaturas(arbol['izq'])
        print(arbol['info'], '| ',arbol['datos']['derrotada_por'])
        inorden_de_criaturas(arbol['der'])

print('Criaturas', '| Derrotada por')
inorden_de_criaturas(arbol)

print()
print('b. se debe permitir cargar una breve descripción sobre cada criatura;')
def cambiar_datos_de_x_criatura(criatura,descripcion = None, derrotada_por = None, capturada_por = None):
    if(descripcion is not None):
        criatura['datos']['descripcion'] = descripcion
    if(derrotada_por is not None):
        criatura['datos']['derrotada_por'] = derrotada_por.title()
    if(capturada_por is not None):
        criatura['datos']['capturada_por'] = capturada_por.title()
    print('datos cambiados')

def buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,clave, info_nueva= None,descripcion = None, derrotada_por = None, capturada_por = None):
    criatura = busqueda(arbol, clave.title())
    if criatura is not None:
        #print('valor encontrado en el arbol')
        cambiar_datos_de_x_criatura(criatura,descripcion, derrotada_por, capturada_por)
        if (info_nueva is not None):#si se introdujo una info nueva
            criatura = eliminar_nodo(arbol, clave.title())
            insertar_nodo(arbol, info_nueva.title(), criatura[1])
    else:
        print('valor no encontrado en el arbol')




print()
clave = input('desea cargar descripciones a las criaturas? ingrese la letra "Y" si lo desea, o cualquier otra letra si no lo desea: ')
while clave.upper() == 'Y':
    print()
    clave = input('ingrese el nombre de la criatura: ')
    criatura = busqueda(arbol, clave.title())
    #print(pos)
    if criatura is not None:
        #name = input('ingrese nuevo nombre:')
        #insertar_nodo(arbol, name, False)
        descripcion_introducida = input('ingrese su descripcion: ')
        print('valor encontrado en el arbol')
        #criatura['datos']['descripcion'] = descripcion
        cambiar_datos_de_x_criatura(criatura, descripcion = descripcion_introducida)
    else:
        print('valor no encontrado en el arbol')
    
    print()
    clave = input('desea seguir cargando descripciones a las criaturas? ingrese la letra "Y" si lo desea, o cualquier otra letra si no lo desea: ')

inorden_con_datos(arbol)
print()

print()
print('c. mostrar toda la información de la criatura Talos;')

#clave = input('ingrese el nombre de la criatura: ')
clave = 'Talos'
criatura = busqueda(arbol, clave.title())
if criatura is not None:
    print('Todo la informacion de', clave,':')
    print(criatura['info'],criatura['datos'])
else:
    print('valor no encontrado en el arbol')

print()
print('d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;')

def cantidad_de_criaturas_derrotadas_de_cada_heroe(arbol, contadores):
    if(arbol is not None):
        cantidad_de_criaturas_derrotadas_de_cada_heroe(arbol['izq'],contadores)

        #cuenta la cantidad de veces que aparecen los heroes
        derrotada_por = arbol['datos']['derrotada_por']
        if derrotada_por != '-':
            if derrotada_por in contadores.keys():
                contadores[derrotada_por]+= 1
            else:
                contadores[derrotada_por] = 1

        cantidad_de_criaturas_derrotadas_de_cada_heroe(arbol['der'],contadores)

def los_3_heroes_que_derrotaron_mayor_cantidad_de_criaturas(contadores, lista_heroes):
    #busca los 3 heroes con mayor cantidad de criaturas derrotadas
    #heroes = []
    if len(contadores.values()) > 0:# si hay heroes que derrotaron criaturas
        numero_maximo = max(contadores.values())
        while (len(lista_heroes) < 3) and (numero_maximo > 0):#sigue buscando heroes si todavia no hay 3 heroes y si el numero maximo es mayor a 0
            for item in contadores.items():#va a iterar en todos los heroes el item se divide en (nombre del heroe, cantidad de criaturas derrotadas)
                #print(item[1])
                if(item[1] == numero_maximo) and (len(lista_heroes)< 3):# si el heroe actual derrotó la mayor cantidad de criaturas y todavia no se encontró los 3 heroes con mayor cantidad de criaturas derrotadas
                    lista_heroes.append(item)#agrega el heroe a la lista
                    contadores[item[0]] = 0#se iguala a cero la cantidad de crituras derrotadas porque este heroe ya se usó y para que no interfiera en el calculo del numero maximo

            numero_maximo = max(contadores.values())

    
contadores= {}
cantidad_de_criaturas_derrotadas_de_cada_heroe(arbol, contadores)
#print(contadores.items())
print('Contadores:')
print('Heroes|Cantidad de criaturas derrotadas')
for item in contadores.items():
    print(item)

lista_de_3_heroes = []
los_3_heroes_que_derrotaron_mayor_cantidad_de_criaturas(contadores, lista_de_3_heroes)
print()
print('los 3 heroes con mayor cantidad de criaturas derrotadas son:')
print(lista_de_3_heroes)


print()
print('e. listar las criaturas derrotadas por Heracles;')
def listar_las_criaturas_derrotadas_por_x_heroe(arbol, heroe):
    if(arbol is not None):
        listar_las_criaturas_derrotadas_por_x_heroe(arbol['izq'],heroe)
        if (arbol['datos']['derrotada_por'] == heroe.title()):
            print(arbol['info'])
        listar_las_criaturas_derrotadas_por_x_heroe(arbol['der'],heroe)

print('las criaturas derrotadas por Heracles son:')
listar_las_criaturas_derrotadas_por_x_heroe(arbol,'Heracles')

print()
print('f. listar las criaturas que no han sido derrotadas;')
print('las criaturas que no fueron derrotadas son:')
listar_las_criaturas_derrotadas_por_x_heroe(arbol,'-')

print()
print('g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;')

print()
print('h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;')


#clave = 'Talos'
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Cerbero',capturada_por = 'Heracles')
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Toro de Creta',capturada_por = 'Heracles')
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Cierva de Cerinea',capturada_por = 'Heracles')
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Jabalí de Erimanto',capturada_por = 'Heracles')
#inorden_con_datos(arbol)


print()
print('i. se debe permitir búsquedas por coincidencia;')
clave = input('ingrese parte de lo que desea buscar:')
inorden_por_coincidencia(arbol,clave)

print()
print('j. eliminar al Basilisco y a las Sirenas;')
def eliminar_criatura(arbol, clave):
    criatura = eliminar_nodo(arbol,clave.title())
    if(criatura[0] is not None):
        print('la criatura',clave.title(),'se eliminó')
    else:
        print('la criatura',clave.title(),'no se pudo eliminar porque no se encuentra en el arbol')
    return criatura

eliminar_criatura(arbol, 'basilisco')
eliminar_criatura(arbol, 'sirenas')

print()
print('k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;')
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Aves del Estínfalo', descripcion = 'Heracles derroto a varias')
print()
clave = 'Aves del Estínfalo'
criatura = busqueda(arbol, clave.title())
if criatura is not None:
    print('Todo la informacion de', clave,':')
    print(criatura['info'],criatura['datos'])
else:
    print('valor no encontrado en el arbol')

print()
print('l. modifique el nombre de la criatura Ladón por Dragón Ladón;')
buscar_x_criatura_y_cambiar_su_info_o_datos(arbol,'Ladón', info_nueva='Dragón Ladón')

print()
print('m. realizar un listado por nivel del árbol;')
print('listado por nivel del arbol:')
por_nivel(arbol)


print()
print('n. muestre las criaturas capturadas por Heracles.')
def listar_las_criaturas_capturadas_por_x_heroe(arbol, heroe):
    if(arbol is not None):
        listar_las_criaturas_capturadas_por_x_heroe(arbol['izq'],heroe)
        if (arbol['datos']['capturada_por'] == heroe.title()):
            print(arbol['info'])
        listar_las_criaturas_capturadas_por_x_heroe(arbol['der'],heroe)

print('las criaturas capturadas por Heracles son:')
listar_las_criaturas_capturadas_por_x_heroe(arbol,'Heracles')