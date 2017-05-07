import pandas as pd
import matplotlib.pyplot as plt

from code.dataStuff import getDict

data14 = pd.DataFrame(getDict(2014))
data15 = pd.DataFrame(getDict(2015))
data16 = pd.DataFrame(getDict(2016))
data17 = pd.DataFrame(getDict(2017))

data14["D.1-Znamka"] = data14["D.1-Znamka"].astype("category")
data15["D.1-Znamka"] = data15["D.1-Znamka"].astype("category")
data16["D.1-Znamka"] = data16["D.1-Znamka"].astype("category")
data17["D.1-Znamka"] = data17["D.1-Znamka"].astype("category")

data14.groupby("D.1-Znamka").size().plot(kind="line")
data15.groupby("D.1-Znamka").size().plot(kind="line")
data16.groupby("D.1-Znamka").size().plot(kind="line")
data17.groupby("D.1-Znamka").size().plot(kind="line")
plt.show()