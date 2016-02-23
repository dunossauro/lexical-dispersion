#!/bin/python3
#
#   Authors:
#       Eduardo Mendes - github.com/z4r4tu5tr4
#
#   Version:
#       0.1 - (Feb/16)
#
#   License:
#       GPL3+

# Imports
from re import compile
import matplotlib.pyplot as mpl
from matplotlib import colors       #Only colors for the graph
from random import choice           #Choose color

regex = compile('\w+')
index = {}

#   assemble a dictionary containing
#   the row and column of the selected
#   words in text
#
#   ex: {word1 : [(line,column)],word2 : [(line,column),(line,column)]}
#
def dict_mount(arq, words):
    with open(arq) as arq:
        for n_line, line in enumerate(arq,1):
            for element in regex.finditer(line):
                if element.group() in words:
                    word = element.group()
                    column = element.start()+1
                    location = (n_line, column)
                    index.setdefault(word,[]).append(location)

#    assemble two lists containing the
#    positions of the words chosen in
#    the Cartesian plane and plots
def mount_plot(word, switching = 0):
    lines = []
    columns = []
    color = choice(tuple(colors.cnames.keys()))
    try:
        for line,column in index[word]:
            lines.append(line)
            columns.append(column)
        word = ('%s (%s Occurrences)') % (word , len(index[word]))
        mpl.plot(lines,columns, 'bo', color = color, label = word)
        if switching == 1:
            mpl.plot(x,y, color = color)

    except KeyError:
        print("Word does not exist in the file")

#says the relationship between
#the words
def same_line(words):
    try:
        word_1 = {a for a,b in index[words[0]]}

        for word in words[1:]:
            word_set = {line for line,column in index[word]}
            inter = word_1.intersection(word_set)

        amount = (("%s Occurrences on the same line")%(len(inter)))
        mpl.plot(0,0,label = amount)

    except KeyError:
        mpl.plot(0,0,label = "One of the chosen words do not exist in the file")

def plot(phrase):
    if len(phrase) > 1:
        same_line(phrase)

    mpl.legend(loc='best')
    mpl.ylabel('Word position on the line')
    mpl.xlabel('Line number')
    mpl.title("Lexical dispersion")
    mpl.show()

# Test for the GUI
phrase = 'a os as o'.split()
dict_mount('s_1000.txt', phrase)
for x in sorted(phrase, key=len):
        mount_plot(x)
plot(phrase)
