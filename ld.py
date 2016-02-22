from re import compile
from collections import defaultdict
import matplotlib.pyplot as mpl
from matplotlib import colors
from random import choice

regex = compile('\w+')
index = {}

def dict_mount(arq, words):
    with open(arq) as arq:
        for n_line, line in enumerate(arq,1):
            for element in regex.finditer(line):
                if element.group() in words:
                    word = element.group()
                    column = element.start()+1
                    location = (n_line, column)
                    index.setdefault(word,[]).append(location)

def mount_plot(word, switching = 0):
    x = []
    y = []
    color = choice(list(colors.cnames.keys()))
    try:
        for a,b in index[word]:
            x.append(a)
            y.append(b)
        word = ('%s (%s Occurrences)') % (word , len(index[word]))
        mpl.plot(x,y, 'bo', color = color, label = word)
        if switching == 1:
            mpl.plot(x,y, color = color)

    except KeyError:
        print("Word does not exist in the file")

def same_line(words):
    try:
        word_1 = set(a for a,b in index[words[0]])
        word_2 = set(a for a,b in index[words[1]])
        inter = word_1.intersection(word_2)
        amount = (("%s Occurrences on the same line")%(len(inter)))
        mpl.plot(0,0,label = amount)
    except KeyError:
        pass

def plot(phrase):
    if len(phrase) > 1:
        same_line(phrase)

    mpl.legend(loc='best')
    mpl.ylabel('Word position on the line')
    mpl.xlabel('Line number')
    mpl.title("Lexical dispersion")
    mpl.show()

phrase = 'a gestão'.split()
dict_mount('s_1000.txt', phrase)
for x in sorted(phrase, key=len):
        mount_plot(x)
plot(phrase)
