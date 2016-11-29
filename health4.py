import requests
from bs4 import BeautifulSoup
import pandas as pd

elections=[]
for year in range(a, b):
    age=str(age)
    file_name= year + ".csv"
    header=pd.read_csv(file_name, nrows=1).dropna(axis=1)
    d=header.iloc[0].to_dict()

    data=pd.read_csv(file_name, index_col=0, thousands= ",", skiprows=[1])
    data.rename(inplace=True, columns=d)
    data.dropna(inplace=True, axis=1)

    data["Age"]=age
    data.append(df[["Country", "Age Group", "Cause of death", "Total deaths"]])

graph=results[results.index=="Accomack County"].plot(x="Cause", y="Total deaths")
graph.get_figure().savefig('fig1.png')
