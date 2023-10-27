#En este archivo pondremos las funciones que usaremos en el proyecto :)
from unidecode import unidecode
import matplotlib.pyplot as plt

def cargar_libro(archivo):
    with open (archivo,'r',encoding='utf-8') as arc:
        libro=arc.read()
        return libro

def contar_caracteres(string):
    return len(string)

def contar_letras(string):
    contador=0
    for i in string:
        if i.isalpha():
            contador+=1

    return contador

def frecuencia_letras(string):
    limpio=sorted(unidecode(string).lower())
    dicci={}
    for i in limpio:
        if not i.isalpha():
            continue

        else:
            fre=dicci.get(i,0)
            dicci[i]=fre+1

    return dicci

def histograma_frecuencia(string):
    d=frecuencia_letras(string)
    #print(d)
    llaves=list(d.keys())
    valores=list(d.values())

    #print(llaves,valores)
    plt.figure(figsize=(10, 10))
    plt.bar(llaves, valores, color='skyblue',width=1)

    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de frecuencia de letras en el libro')

    plt.show()


todo=cargar_libro('r_y_j.txt')
print(contar_caracteres(todo))
print(contar_letras(todo))
print(frecuencia_letras(todo))
histograma_frecuencia(todo)