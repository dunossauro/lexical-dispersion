from re import compile
from collections import defaultdict
import matplotlib.pyplot as mpl
from matplotlib import colors
from random import choice

regex = compile('\w+')
index = {}

def dict_mount(arq, palavras):
    with open(arq) as arq:
        for n_linha, linha in enumerate(arq,1):
            for elemento in regex.finditer(linha):
                if elemento.group() in palavras:
                    palavra = elemento.group()
                    coluna = elemento.start()+1
                    location = (n_linha, coluna)
                    index.setdefault(palavra,[]).append(location)

def mount_plot(palavra, chave = 0):
    x = []
    y = []
    color = choice(list(colors.cnames.keys()))
    try:
        for a,b in index[palavra]:
            x.append(a)
            y.append(b)
        palavra = ('%s (%s Ocorrências)') % (palavra , len(index[palavra]))
        mpl.plot(x,y, 'bo', color = color, label = palavra)
        if chave == 1:
            mpl.plot(x,y, color = color)

    except KeyError:
        print("A palavra não existe no arquivo")

def same_line(palavras):
    try:
        palavra_1 = set(a for a,b in index[palavras[0]])
        palavra_2 = set(a for a,b in index[palavras[1]])
        inter = palavra_1.intersection(palavra_2)
        quantidade = (("%s Ocorrências na mesma linha")%(len(inter)))
        mpl.plot(0,0,label = quantidade)
    except KeyError:
        pass

def plot(frase):
    if len(frase) > 1:
        same_line(frase)

    mpl.legend(loc='upper left')
    mpl.ylabel('Posição da palavra na linha')
    mpl.xlabel('Número da linha')
    mpl.title("Disperção Lexical")
    mpl.show()

frase = 'a gestão'.split()
dict_mount('s_1000.txt', frase)
for x in sorted(frase, key=len):
        mount_plot(x)
plot(frase)
