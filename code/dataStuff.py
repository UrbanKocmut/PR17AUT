

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




