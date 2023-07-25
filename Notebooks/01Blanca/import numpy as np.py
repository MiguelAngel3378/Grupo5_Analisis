import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


import os
for dirname, _, filenames in os.walk('../../Data/FuentesOriginales/USAR/world_population.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


filepath = "../../Data/FuentesOriginales/USAR/world_population.csv"
df = pd.read_csv(filepath)
df

LIMPIEAZA DATODS
print(f"Shape of DataFrame:\n {df.shape}")
print(df.columns.values)

for column in df.columns:
    print(f"{column} ---> {df[column].nunique()}")

df.info()

VISUALIZACION 
df.describe().T.sort_values("50%", ascending = False).style.background_gradient(cmap = "RdPu")\
    .bar(subset = ["mean"], color = "red").bar(subset = ["max"], color = "green")

REVISANDO NAM
for column in df.columns:
    print(column)
    print(f"{df[column].isnull().value_counts()}\n")

REVISANDO VALORES NULOS
df.isnull().sum().values

REVISANDO VALORES DUPLICADOS
df.duplicated().sum()

ELIMINANDO COLUMNAS NO NECESARIAS PARA ESTA VISUALIZACION
df.drop("CCA3", axis = 1, inplace = True)
df.rename({"Country/Territory":"Country", 
          '2022 Population': 2022,
          '2020 Population': 2020,
          '2015 Population': 2015, 
          '2010 Population': 2010, 
          '2000 Population': 2000, 
          '1990 Population': 1990, 
          '1980 Population': 1980, 
          '1970 Population': 1970}, axis = 1, inplace = True)

VERIFICANDO
df

FORMATEANDO LA DATA
for column in df.columns[4:12]:
    df[column] = df[column].astype(int)

VISUALIZACION DE LA DATA
* Nueva columna llamada Densidad para usa pairplot

bins = np.linspace(min(df[2022]), max(df[2022]), 3)
df["Density"] = pd.cut(df[2022], bins, labels = ["Low", "High"])

bins = np.linspace(min(df[2022]), max(df[2022]), 3)
df["Density"] = pd.cut(df[2022], bins, labels = ["Low", "High"])
sns.pairplot(data = df, hue = "Density")
plt.tight_layout
plt.show()


ANALIZAREMOS LOS 2 PAISE CON MAYOR POBLACION EN EL MUNDO
df_china_india = df.set_index("Country")
df_china_india = df_china_india.loc[["China", "India"],2022:1970]
df_china_india = df_china_india.transpose()
df_china_india.rename_axis("Years", axis = 1, inplace = True)
df_china_india

BOXPLOT
df_china_india.plot(kind = "box", color = 'red', figsize = (13, 6), vert = True)

AHORA ANALIZAREMOS LAS 3 ECONOMIAS MAS GRANDES EN EL MUNDO
df_economic = df.set_index("Country")
df_economic = df_economic.loc[:, 2022:1970].transpose()
df_economic = df_economic.loc[:, ["United States", "China", "Japan"]].reset_index()
df_economic.rename({"index":"Years"}, axis = 1, inplace = True)
df_economic.rename_axis(None, axis = 1, inplace = True)
df_economic.style.background_gradient(cmap = "YlOrRd").bar(subset = ["United States"], color = "darkblue")\
    .bar(subset = ["Japan"], color = "green")


Poblacion de las 3 economias mas grandes del Mundo
ax = df_economic.plot(kind = "bar", x = "Years", y =["United States", "China", "Japan"], figsize = (13, 6), 
            color = ["red", "blue", "green"],alpha = 0.75)
 plt.title("Poblacion de las 3 economias mas grandes del Mundo", y = 1.11, fontsize = "x-large",
        fontweight = "bold")
plt.xlabel("Years", fontsize = "large", labelpad = 10)
plt.ylabel("Population", fontsize = "large", labelpad = 10)
plt.xticks(rotation = 0)
ax.bar_label(ax.containers[1], padding = 3.5)
plt.tight_layout()
plt.show()

RELACION ENTRE (AREA, CRECIMIENTO & PORCENTAJE)
df_relationship = df[["Area (km²)", "Density (per km²)", 
                    "Growth Rate", "World Population Percentage"]].corr()
sns.heatmap(data = df_relationship, annot = True)
plt.tight_layout()
plt.show()



















