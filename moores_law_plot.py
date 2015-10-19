import pandas as pd
from numpy import log
import plotly.plotly as py
from plotly.graph_objs import *

# Importing data in panda and preparing plot args
path = "C:/Users/amate_000/Google Drive/Projects/LOAR/loar_plots/datasets/moores_law.csv"
df = pd.read_csv(path, sep=",")
df["Transistors"] = df["Transistors"]*1000
traces_colors = ["#4183D7", "#F2784B", "#66CC99", "#264348", "#1BA39C", "#4D8FAC", "#D91E18"]

# Create category trace
trace1 = Scatter(
    x=df["Year"],
    y=df["ClockRate"],
    mode="markers",
    name="Clock rate",
#    text=descriptions,
    marker=Marker(
        color=traces_colors[0],
        size=8,
        line=Line(
            color='white',
            width=0.5
        )
    ),
    yaxis="y2"
)

trace2 = Scatter(
    x=df["Year"],
    y=df["Transistors"],
    mode="markers",
    name="Number of transistors",
    marker=Marker(
        color=traces_colors[5],
        size=8,
        line=Line(
            color='white',
            width=0.5
        )
    )
)

data = Data([trace1, trace2])

# Setting up layout parameters
layout = Layout(
    title="Number of transistors \ Clock rate over time",
    xaxis=XAxis(
        title = "Year",
        autorange=True
    ), 
    yaxis=YAxis(
        title = "Mhz",
        autorange=True,
        exponentformat="e"

    ),
    yaxis2=YAxis(
        title = "Transistors",
        overlaying="y",
        side="right",
        anchor="x",
        type="linear",
        autorange=True,
        exponentformat="e"
    )
    
)


# Putting it all together in a Figure
fig = Figure(data=data, layout=layout)
 
# Generating online plot
unique_url = py.plot(fig, layout=layout, filename = "Moore's law")
                