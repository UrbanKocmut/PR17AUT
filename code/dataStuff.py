
def merge():
    fout=open("../data/2016/podatki_2016.csv","a")
    # first file:
    for line in open("../data/2016/NPodatki_012016.csv"):
        fout.write(line)
    # now the rest:
    for num in range(2,13):
        f = open("../data/2016/NPodatki_"+"{:02d}".format(num)+"2016.csv")
        next(f) # skip the header
        print(num)
        for line in f:
             fout.write(line)
        f.close() # not really needed
    fout.close()

merge()