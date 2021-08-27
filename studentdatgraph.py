import csv
import pandas as pd
import plotly.express as pe
data=pd.read_csv("pixelmathdata.csv")
mean=data.groupby("level")["attempt"].mean()
graph=pe.scatter(data,x="student_id",y="level",color="attempt")
graph.show()