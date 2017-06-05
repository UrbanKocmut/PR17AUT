import pandas as pd
from csv import DictReader

"""
Združi podatke po standardni obliki, če je bog dal blagoslov
"""


def merge(leto):
    leto = str(leto)
    fout = open("../data/" + leto + "/podatki_" + leto + ".csv", "a")
    # first file:
    for line in open("../data/" + leto + "/NPodatki_01" + leto + ".csv"):
        fout.write(line)
    # now the rest:
    for num in range(2, 13):
        f = open("../data/" + leto + "/NPodatki_" + "{:02d}".format(num) + leto + ".csv", encoding="UTF-8")
        next(f)  # skip the header
        print(num)
        for line in f:
            fout.write(line)
        f.close()  # not really needed
    fout.close()


def getDict(leto, mesec=1):
    leto = str(leto)
    file = "../data/" + leto + "/NPodatki_"+"{:02d}".format(mesec) + leto + ".csv"
    dict_list = []
    with open(file,encoding='ANSI') as csvfile:
        reader = DictReader(csvfile, delimiter=';')
        for row in reader:
            dict_list.append(row)
    return dict_list

