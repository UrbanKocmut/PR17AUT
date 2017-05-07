import pandas as pd
import matplotlib.pyplot as plt

from code.dataStuff import getDict

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

