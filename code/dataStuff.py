
"""
Združi podatke po standardni obliki
"""
def merge(leto):
    leto = str(leto)
    fout=open("../data/"+leto+"/podatki_"+leto+".csv","a")
    # first file:
    for line in open("../data/"+leto+"/NPodatki_01"+leto+".csv", encoding="UTF-16LE"):
        fout.write(line)
    # now the rest:
    for num in range(2,13):
        f = open("../data/"+leto+"/NPodatki_"+"{:02d}".format(num)+leto+".csv", encoding="UTF-16LE")
        next(f) # skip the header
        print(num)
        for line in f:
             fout.write(line)
        f.close() # not really needed
    fout.close()

merge(2014)
merge(2015)
merge(2016)