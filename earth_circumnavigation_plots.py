import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

##importing data in panda
path = "C:/Users/amate_000/Google Drive/Projects/LOAR/earth_circumnavigation.csv"
data_df = pd.read_csv(path, sep=",")

#loading data, first into Scatter then Data object
trace0 = Scatter(
    x=data_df["start_year"],
    y=data_df["duration"]
)

data = Data([trace0])

#setting up layout parameters
layout = Layout(
    xaxis=XAxis(
        type='log',
        autorange=True
    )
)

#putting it all together in a Figure
fig = Figure(data=data, layout=layout)
 
#generating online plot
unique_url = py.plot(fig, layout=layout, filename = 'earth_circumnavigation')