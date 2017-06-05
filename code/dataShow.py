import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from code.dataSortOut import getDict

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

"""
Vrne graf znamk z največ registriranimi vatomobili januarja po letih.
"""


def topZnamke(n=30):
    data14 = pd.DataFrame(getDict(2014))
    data15 = pd.DataFrame(getDict(2015))
    data16 = pd.DataFrame(getDict(2016))
    data17 = pd.DataFrame(getDict(2017))

    data14["D.1-Znamka"] = data14["D.1-Znamka"].astype("category")
    data15["D.1-Znamka"] = data15["D.1-Znamka"].astype("category")
    data16["D.1-Znamka"] = data16["D.1-Znamka"].astype("category")
    data17["D.1-Znamka"] = data17["D.1-Znamka"].astype("category")

    top = pd.DataFrame()
    top["2014"] = data14["D.1-Znamka"].value_counts().nlargest(n)
    top["2015"] = data15["D.1-Znamka"].value_counts().nlargest(n)
    top["2016"] = data16["D.1-Znamka"].value_counts().nlargest(n)
    top["2017"] = data17["D.1-Znamka"].value_counts().nlargest(n)

    plot = top.plot(kind="bar")
    plt.tight_layout()
    plt.show()


"""
Prikaže graf slovenskih top modelov po letih.
"""


def topModeli(n=30):
    polje = "D.3-Komerc. oznaka"
    dataOverYears = []
    top = pd.DataFrame()
    for yr in range(2014, 2017):
        df = pd.DataFrame(getDict(yr))
        df[polje] = df[polje].map(lambda x: x.split("/", 1)[0] if x is not None else x).astype("category")
        top[str(yr)] = df[polje].value_counts().nlargest(n)
    for x in top:
        print(x)

    plot = top.plot(kind="bar")
    plt.tight_layout()
    plt.show()


def moskiZenske():
    n = 10
    polje = "C2-Spol lastnika (ce gre za fizicno osebo)"
    dataOverYears = []
    top = pd.DataFrame()

    for yr in range(2014, 2018):
        df = pd.DataFrame(getDict(yr))
        df[polje] = df[polje].map(lambda x: x if x is not "" else None).astype("category")
        top[str(yr)] = df[polje].value_counts().nlargest(n)

    plot = top.plot(kind="bar")
    plt.tight_layout()
    plt.show()


def dizelBencin():
    n = 2
    polje = "P.1.3-Vrsta goriva (opis)"
    dataOverYears = []
    top = pd.DataFrame()

    for yr in range(2014, 2018):
        df = pd.DataFrame(getDict(yr))
        df[polje] = df[polje].map(lambda x: x if x is not "" else None).astype("category")
        top[str(yr)] = df[polje].value_counts().nlargest(n)

    plot = top.plot(kind="bar")
    plt.tight_layout()
    plt.show()


def povprecna_poraba(leto, po_mesecih=False):
    if leto < 2014 or leto > 2016:
        raise RuntimeError('Napacno leto, mora biti 2014-2016')
    co2 = []
    poraba = []
    for i in range(1, 13):
        vozilaLeta = pd.DataFrame(getDict(leto, mesec=i))
        vozilaLeta = vozilaLeta[vozilaLeta["J-Kategorija in vrsta vozila (opis)"] == "osebni avtomobil"]
        vozilaLeta['V.8-Kombinirana poraba goriva'] = pd.to_numeric(vozilaLeta['V.8-Kombinirana poraba goriva'].map(lambda x: x.replace(",", ".")))
        vozilaLeta['V.1-CO'] = pd.to_numeric(vozilaLeta['V.1-CO'].map(lambda x: x.replace(",", ".")))
        co2.append(vozilaLeta['V.1-CO'].mean())
        poraba.append(vozilaLeta['V.8-Kombinirana poraba goriva'].mean())
    if po_mesecih:
        return {"CO2": co2, "Poraba": poraba}
    else:
        return {"CO2": np.mean(co2), "Poraba": np.mean(poraba)}


def povprecni_avto(dfAvti=pd.DataFrame(getDict(2017))):
    osebniAvtomobili = dfAvti[dfAvti["J-Kategorija in vrsta vozila (opis)"] == "osebni avtomobil"]
    osebniAvtomobili['D.3-Komerc. oznaka'] = osebniAvtomobili['D.3-Komerc. oznaka'].map(lambda x: x.split("/")[0]).astype("category")
    osebniAvtomobili['R-Barva vozila (opis)'] = osebniAvtomobili['R-Barva vozila (opis)'].map(lambda x: x.split(" - ")[1]).astype("category")
    osebniAvtomobili['D.1-Znamka'] = osebniAvtomobili['D.1-Znamka'].astype("category")
    osebniAvtomobili['P.1.3-Vrsta goriva (opis)'] = osebniAvtomobili['P.1.3-Vrsta goriva (opis)'].astype("category")
    osebniAvtomobili['Okoljevarstvena oznaka'] = osebniAvtomobili['Okoljevarstvena oznaka'].astype("category")
    osebniAvtomobili['G-Masa vozila'] = pd.to_numeric(osebniAvtomobili['G-Masa vozila'])
    osebniAvtomobili['Y.1-Dolzina'] = pd.to_numeric(osebniAvtomobili['Y.1-Dolzina'])
    osebniAvtomobili['Y.2-Sirina'] = pd.to_numeric(osebniAvtomobili['Y.2-Sirina'])
    osebniAvtomobili['Y.3-Visina'] = pd.to_numeric(osebniAvtomobili['G-Masa vozila'])
    osebniAvtomobili['V.8-Kombinirana poraba goriva'] = pd.to_numeric(osebniAvtomobili['V.8-Kombinirana poraba goriva'].map(lambda x: x.replace(",", ".")))
    osebniAvtomobili['T-Najvisja hitrost'] = pd.to_numeric(osebniAvtomobili['T-Najvisja hitrost'])
    osebniAvtomobili['masaTovora'] = pd.to_numeric(osebniAvtomobili['F.1-Najvecja tehnicno dovoljena masa vozila']) - osebniAvtomobili['G-Masa vozila']
    osebniAvtomobili['P.1.1-Delovna prostornina'] = pd.to_numeric(osebniAvtomobili['P.1.1-Delovna prostornina'])
    osebniAvtomobili['P.1.2-Nazivna moc'] = pd.to_numeric(osebniAvtomobili['P.1.2-Nazivna moc'].map(lambda x: x.replace(",", ".")))
    povpModel = osebniAvtomobili["D.3-Komerc. oznaka"].mode()[0]
    povpZnamka = osebniAvtomobili["D.1-Znamka"].mode()[0]
    povpGorivo = osebniAvtomobili["P.1.3-Vrsta goriva (opis)"].mode()[0]
    povpNosilnost = osebniAvtomobili['masaTovora'].mean()
    povpMasa = osebniAvtomobili['G-Masa vozila'].mean()
    povpMaxSpeed = osebniAvtomobili['T-Najvisja hitrost'].mean()
    povpPoraba = osebniAvtomobili['V.8-Kombinirana poraba goriva'].mean()
    popvProstorninaMotorja = osebniAvtomobili['P.1.1-Delovna prostornina'].mean()
    povpMoc = osebniAvtomobili['P.1.2-Nazivna moc'].mean()
    povpDolzina = osebniAvtomobili['Y.1-Dolzina'].mean()
    povpSirina = osebniAvtomobili['Y.2-Sirina'].mean()
    povpVisina = osebniAvtomobili['Y.3-Visina'].mean()
    povpBarva = osebniAvtomobili['R-Barva vozila (opis)'].mode()[0]
    povpOkoljskaOznaka = osebniAvtomobili['Okoljevarstvena oznaka'].mode()[0]
    return {
        "povpZnamka": povpZnamka,
        "povpModel": povpModel,
        "povpGorivo": povpGorivo,
        "povpNosilnost": povpNosilnost,
        "povpMasa": povpMasa,
        "povpMaxSpeed": povpMaxSpeed,
        "povpPoraba": povpPoraba,
        "popvProstorninaMotorja": popvProstorninaMotorja,
        "povpMoc": povpMoc,
        "povpDolzina": povpDolzina,
        "povpSirina": povpSirina,
        "povpVisina": povpVisina,
        "povpBarva": povpBarva,
        "povpOkoljskaOznaka": povpOkoljskaOznaka
    }
