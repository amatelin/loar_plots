import pandas as pd
from numpy import log
import plotly.plotly as py
from plotly.graph_objs import *

# Importing data in panda and preparing plot args
path = "C:/Users/amate_000/Google Drive/Projects/LOAR/loar_plots/datasets/life_expectancy_world.csv"
df = pd.read_csv(path, sep=",")
traces_colors = ["#4183D7", "#F2784B", "#66CC99", "#264348", "#1BA39C", "#4D8FAC", "#D91E18"]

traces = []
i = 0

for col_name in df.columns[1:]:
    # Create category trace
    trace = Scatter(
        x=df["year"],
        y=df[col_name],
        mode="lines+markers",
        connectgaps=True,
        name=col_name,
        line=Line(
            shape="spline",
            width=2,
            color=traces_colors[i]
        ),
        marker=Marker(
            color=traces_colors[i],
            size=6,
            line=Line(
                color='white',
                width=0.5
            )
        )
    )
    
    i+=1
    traces.append(trace)

data = Data(traces)

# Setting up layout parameters
layout = Layout(
    title="Worldwide life expectancy over time",
    xaxis=XAxis(
        title = "Year",
        autorange=True
    ), 
    yaxis=YAxis(
        title = "Life expectancy (at birth)",
        autorange=True,
    )
)


# Putting it all together in a Figure
fig = Figure(data=data, layout=layout)
 
# Generating online plot
unique_url = py.plot(fig, layout=layout, filename = "Worldwide life expectancy")
                