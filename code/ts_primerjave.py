import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from code.dataSortOut import getDict

# NE SPREMINJI MOJE KODE, PIŠ SPODI NAPREJ!
# IMENA FUNKCIJI POVEJO KA DELAJO, ZATO JE TOLK MAL KOMENTARJEV
# RAZLIKA CIFRE VRAČA POVPREČJE ZA PODAN ATRIBUT ZA MOŠKE, ŽENSKE IN POSLVNE UPORABNIKE
# RAZLIKA STRING VRAČA 3 SLOVARJE: ZA VSE KLJUČE KOLKRAT SE PONOVIJO, ZA MOŠKE, ŽENSKE, POSLOVNE. NPR. MOŠKI: RDEČA: 10, RUMENA: 20....



def razlika_moski_zenska_stringi(data, atribut):
    rez_z = {}
    rez_m = {}
    rez_posl = {}
    st = 0
    while (st < len(data[atribut])):
        if data["C2-Starost lastnika vozila"][st] == "":
            st += 1
        elif data["C2-Starost lastnika vozila"][st] == None:
            st += 1
        elif int(data["C2-Starost lastnika vozila"][st]) >= 50:   #DA UREJAŠ LETA ---> če hočeš brz omejitev daš 1000 al pa neki
            if (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "Z"):
                if (data[atribut][st] not in rez_z):
                    rez_z.update({data[atribut][st]: 1})
                else:
                    rez_z[data[atribut][st]] += 1
                st += 1
            elif (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "M"):
                if (data[atribut][st] not in rez_m):
                    rez_m.update({data[atribut][st]: 1})
                else:
                    rez_m[data[atribut][st]] += 1
                st += 1
            else:
                if (data[atribut][st] not in rez_posl):
                    rez_posl.update({data[atribut][st]: 1})
                else:
                    rez_posl[data[atribut][st]] += 1
                st += 1
        else:
            st+=1
    return np.array([rez_z, rez_m, rez_posl])


def razlika_moski_zenska_cifre(data, atribut): #brz omejitve let... prazne, tiste z / - ignoriraš, pa spremeniš "," v "."
    sum_z = 0
    sum_m = 0
    sum_pos = 0
    stev_z = 0
    stev_m = 0
    stev_pos = 0
    st = 0

    while (st < len(data[atribut])):
        if data[atribut][st] == "" or data[atribut][st] == None:
            st += 1
        elif "/" in data[atribut][st] or "-" in data[atribut][st]:
            st += 1
        elif (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "Z"):
            sum_z += float(data[atribut][st].replace(",", "."))
            stev_z += 1
            st += 1
        elif (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "M"):
            sum_m += float(data[atribut][st].replace(",", "."))
            stev_m += 1
            st += 1
        else:
            sum_pos += float(data[atribut][st].replace(",", "."))
            stev_pos += 1
            st += 1

        if (stev_z == 0):
            stev_z = 1
        if stev_m == 0:
            stev_m = 1
        if stev_pos == 0:
            stev_pos = 1

    return np.array([(sum_z / stev_z), (sum_m / stev_m), (sum_pos / stev_pos)])

#PREVERIŠ ČE JE INT
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

#ČE JE ATRIBUT INT, IZPIŠEŠ POVPREČJE... SEŠTEJEŠ IZ VSEH LET PA DELIŠ...
def izpisi_cifre(temp, atribut):
    st = 0
    print(atribut)
    for x in temp:
        if(st==0):
            print("Ženska")
            st+=1
        elif st==1:
            print("MOŠKI")
            st+=1
        else:
            print("POSLOVNI")
        print(str(x))

    print("--------------------------------------------------------------------------------------------" + "\n")

#ČE JE STRING DOBIŠ SLOVAR KEY: VALUES, KJER JE VALUE ŠT. PONOVITEV... ZRAČUNAŠ PROCENTE ZA VSE
def izpisi_string(temp, atribut):
    st = 0
    print(atribut)
    while st < 3:
        if(st==0):
            print("\n" + "ŽENSKE")
        elif(st==1):
            print("\n" + "MOŠKI")
        else:
            print("\n" + "POSLOVNI")

        for key, items in temp[st].items():
           print(key + " " + str(items))
        st += 1

    print("--------------------------------------------------------------------------------------------")


data17 = pd.DataFrame(getDict(2017))
'''
for x in data17:
    for y in data17[x]:
        if (y != ""):
            if check_int(y):
                temp = razlika_moski_zenska_cifre(data17, x)
                izpisi_cifre(temp, x)
            else:
                temp = razlika_moski_zenska_stringi(data17, x)
                if not "Datum" in x:
                    izpisi_string(temp, x)
            break
        else:
            break
'''

data14 = pd.DataFrame(getDict(2014))
data15 = pd.DataFrame(getDict(2015))
data16 = pd.DataFrame(getDict(2016))
#atribut = "C-Starost uporabnika vozila"
#atribut = "C2-Starost lastnika vozila"
atribut = "D.1-Znamka"

def izpisi_starot_voznika():
    print("2014")
    izpisi_cifre(razlika_moski_zenska_cifre(data14, atribut), atribut)
    print("2015")
    izpisi_cifre(razlika_moski_zenska_cifre(data15, atribut),atribut)
    print("2016")
    izpisi_cifre(razlika_moski_zenska_cifre(data16, atribut), atribut)
    print("2017")
def things():
    temp = razlika_moski_zenska_stringi(data17, atribut)

    zenske = temp[0]
    moski = temp[1]
    poslovni = temp[2]

    import operator
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    zenske = sorted(zenske.items(), key=operator.itemgetter(1))

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    moski = sorted(moski.items(), key=operator.itemgetter(1))

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    poslovni = sorted(poslovni.items(), key=operator.itemgetter(1))

    zenske.reverse()
    st=0
    for x in zenske:
        if(st<11):
            print(x[0]+ " ")
            st+=1
        else:
            st+=1

    print()
    moski.reverse()
    st=0
    for x in moski:
        if(st<11):
            print(x[0]+ " " )
            st+=1
        else:
            st+=1

    print()
    poslovni.reverse()
    st=0
    for x in poslovni:
        if(st<11):
            print(x[0]+ " ")
            st+=1
        else:
            st+=1

    sts_z = 0
    st=0
    for x in zenske:
        if(st<11):
            sts_z += x[1]
            temp = str(x[1]/788)
            print(temp.replace(".", ","))
            st+=1
        else:
            st+=1

    print()
    st=0
    sts_m = 0
    for x in moski:
        if(st<11):
            sts_m+=x[1]
            temp = str(x[1] / 1302)
            print(temp.replace(".", ","))
            st+=1
        else:
            st+=1

    print()
    st=0
    sts_p = 0
    for x in poslovni:

        if(st<11):
            sts_p += x[1]
            temp = str(x[1] / 5580)
            print(temp.replace(".", ","))
            st+=1
        else:
            st+=1

#RAZLIKE Z OMEJEITVO STAROSTI
def razlika_moski_zenska_cifre2(data, atribut):
    sum_z = 0
    sum_m = 0
    sum_pos = 0
    stev_z = 0
    stev_m = 0
    stev_pos = 0
    st = 0

    while (st < len(data[atribut])):
        if data["C2-Starost lastnika vozila"][st] == "":
            st+=1
        elif data["C2-Starost lastnika vozila"][st] == None:
            st+=1
        elif int(data["C2-Starost lastnika vozila"][st]) >= 50:  #OMEJITEV STAROSTI
            if data[atribut][st] == "" or data[atribut][st] == None:
                st += 1
            elif "/" in data[atribut][st] or "-" in data[atribut][st]:
                st += 1
            elif (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "Z"):
                sum_z += float(data[atribut][st].replace(",", "."))
                stev_z += 1
                st += 1
            elif (data["C2-Spol lastnika (ce gre za fizicno osebo)"][st] == "M"):
                sum_m += float(data[atribut][st].replace(",", "."))
                stev_m += 1
                st += 1
            else:
                sum_pos += float(data[atribut][st].replace(",", "."))
                stev_pos += 1
                st += 1

            if (stev_z == 0):
                stev_z = 1
            if stev_m == 0:
                stev_m = 1
            if stev_pos == 0:
                stev_pos = 1
        else:
            st+=1

    return np.array([(sum_z / stev_z), (sum_m / stev_m), (sum_pos / stev_pos)])
def prostornina():
    atribut = "P.1.1-Delovna prostornina"
    temp = razlika_moski_zenska_cifre2(data17, atribut)
    izpisi_cifre(temp, atribut)

atribut = "P.1.3-Vrsta goriva (opis)"
def tipi_vozl():
    temp = razlika_moski_zenska_stringi(data17, atribut)

    zenske = temp[0]
    moski = temp[1]
    poslovni = temp[2]

    import operator

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    zenske = sorted(zenske.items(), key=operator.itemgetter(1))

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    moski = sorted(moski.items(), key=operator.itemgetter(1))

    zenske.reverse()
    st = 0
    for x in zenske:
        if (st < 11):
            print(x[0] + " ")
            st += 1
        else:
            st += 1

    print()
    moski.reverse()
    st = 0
    for x in moski:
        if (st < 11):
            print(x[0] + " ")
            st += 1
        else:
            st += 1

    print()
    sts_z = 0
    st = 0
    for x in zenske:

        sts_z += x[1]
        temp = str(x[1] / 1071)
        print(temp.replace(".", ","))
        st += 1


    print()
    st = 0
    sts_m = 0
    for x in moski:
        if (st < 13):
            sts_m += x[1]
            temp = str(x[1] / 2012)
            print(temp.replace(".", ","))
            st += 1
        else:
            st += 1

def izpisi_string2(temp, atribut):
    st = 0
    z = {}
    m = {}
    print(atribut)
    while st < 3:
        if(st==0):
            print("\n" + "ŽENSKE")
        elif(st==1):
            print("\n" + "MOŠKI")
        else:
            print("\n" + "POSLOVNI")

        for key, items in temp[st].items():
            if(st==0):
                if key in z:
                    z[key] += items
                else:
                    z.update({key: items})
            else:
                if key in z:
                    m[key] += items
                else:
                    m.update({key: items})
        st += 1

    print("--------------------------------------------------------------------------------------------")
    return z


def oznaka():
    atribut="Komerc. oznaka  do prvega /"
    temp = razlika_moski_zenska_stringi(data16, atribut)
    zenske = temp[0]
    moski = temp[1]
    poslovni = temp[2]

    import operator

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    zenske = sorted(zenske.items(), key=operator.itemgetter(1))

    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    moski = sorted(moski.items(), key=operator.itemgetter(1))

    zenske.reverse()
    moski.reverse()
    sts_z=0
    st=0
    for x in zenske:
        if st < 8:
            sts_z += x[1]
            print(x[0])
            st+=1
        else:
            st+=1
    print()
    st=0
    sts_m = 0
    for x in moski:
        if st < 8:
            sts_m += x[1]
            print(x[0])
            st+=1
        else:
            st+=1
    print()
    sts_z=0
    st=0
    for x in zenske:
        if st < 8:
            sts_z += x[1]
            print(str(x[1]/128).replace(".", ","))
            st+=1
        else:
            st+=1
    st=0
    print()
    sts_m = 0
    for x in moski:
        if st < 8:
            sts_m += x[1]
            print(str(x[1]/185).replace(".", ","))
            st+=1
        else:
            st+=1


    print(sts_z)
    print(sts_m)