#En este archivo pondremos las funciones que usaremos en el proyecto :)
import re
from unidecode import unidecode
import matplotlib.pyplot as plt
import stopwordsiso as stopwords
import spacy

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

# Punto 5
def get_frecuencia_palabras(string):
    lista=string.split()
    dicci={}
    for i in lista:
        fre=dicci.get(i,0)
        dicci[i]=fre+1
    return dicci

def get_100_palabras_frecuentes(string):
    frecuencia = get_frecuencia_palabras(string)
    frecuencia = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
  
    return dict(frecuencia[:100]).keys()

# Punto 6
def get_distinct_words(string):
    return list(set(string.split()))

# Punto 7
def get_language(palabras):
    counter = {"en": 0, "es": 0, "fr": 0, "de": 0, "pt": 0}
    for palabra in palabras:
        for idioma in counter:
            if palabra in stopwords.stopwords(idioma):
                counter[idioma] += 1
    return max(counter.items(), key=lambda x: x[1])[0]

# Punto 8
def get_frecuencia_not_stopwords(string, lang):
    lista=string.split()
    dicc= {}
    for i in lista:
      if i not in stopwords.stopwords(lang):
        fre=dicc.get(i,0)
        dicc[i]=fre+1
    max_50 = sorted(dicc.items(), key=lambda x: x[1], reverse=True)[:50]
    return dict(max_50).keys()


#Alejandro 
e = spacy.load('es_core_news_md')
def places_or_names(x):
    f = {}
    t = False

    for p in x:
        if p.endswith(".") or x.index(p) == 0:
            t = True
        elif p.istitle() and not t:
            if p in f:
                f[p] += 1
            else:
                f[p] = 1
        else:
            t = False

    return f

def places(x):
    lugares = {}
    nombres = {}
    x = places_or_names(x)
    for lugar, veces in x.items():
        d = e(lugar)
        l = []
        for i in d.ents:
            if i.label_ == "LOC":
                l.append(i.text)
        if l:
            lugares[lugar] = l * veces
        else:
            nombres[lugar] = [lugar] * veces
    return(lugares, nombres)


#Punto 12, por mejorar
def encontrar_fechas(texto):
    patron_años = r'\d{4}'
    años_texto = re.findall(patron_años, texto)
    años = set(años_texto)
    set1, set2, set3 = set(), set(), set()
    
    for i in años:
        i = int(i)  
        if i < 1789:
            set1.add(i)
        elif 1789 <= i <= 2023:
            set2.add(i)
        else:
            set3.add(i)

    mayor_longitud = 0
    conjunto_mayor_longitud = None

    if len(set1) > mayor_longitud:
        conjunto_mayor_longitud = set1
        mayor_longitud = len(set1)
    if len(set2) > mayor_longitud:
        conjunto_mayor_longitud = set2
        mayor_longitud = len(set2)
    if len(set3) > mayor_longitud:
        conjunto_mayor_longitud = set3
        mayor_longitud = len(set3)

    if conjunto_mayor_longitud == set1:
        print('Época antigua')
    elif conjunto_mayor_longitud == set2:
        print('Época contemporanea')
    elif conjunto_mayor_longitud == set3:
        print('Futurista')

#Pruebas de Alejandro :)
'''
x = input().split()
l, n = places(x)
r = {}
for i, j in n.items():
    if i not in r:
        r[i] = len(j)
z = dict(sorted(r.items(), key=lambda item:item[1], reverse= True))
principales = list(z.keys())[:5]
for k, m in n.items():
    print(k,(len(m)))
print("" + " ".join(principales))
print("" + " ".join(l.keys()))
'''

todo=cargar_libro('r_y_j.txt')
print(contar_caracteres(todo))
print(contar_letras(todo))
print(frecuencia_letras(todo))

# Punto 5
palabras_mas_frec = get_100_palabras_frecuentes(todo)
print(f'5. 100 Palabras mas frecuentes: {palabras_mas_frec}')
# Punto 6
print(f'6. Distintas palabras: {len(get_distinct_words(todo))}')
# Punto 7
lang = get_language(palabras_mas_frec)
print(f'7. Idioma: {lang}')
# Punto 8
print(f'8. 50 Palabras mas frecuentes no stopwords: {get_frecuencia_not_stopwords(todo, lang)}')
# Punto 9


# Punto 4
histograma_frecuencia(todo)
