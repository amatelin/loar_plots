# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

# Importing data in panda 
path = "C:/Users/amate_000/Google Drive/Projects/LOAR/loar_plots/datasets/chemical_elements_discovery.csv"
raw_df = pd.read_csv(path, sep=",")

# Creating df organised on the number of discovered elements/year
df = pd.DataFrame()
group = raw_df.groupby("Discovery")
df["year"] = group.size().index
df["count"] = group.size().values
df["total"] = df["count"].cumsum()

# Creating group flag and associating corresponding color
def assignValue(year, values):
    if year<0:
        return values[0]
    elif year<2002:
        return values[1]
    else:
        return values[2]
        
df["group"] = df["year"]    
df["group"] = df["year"].apply(assignValue, args=([0,1,2],))

# Making description string for each year
def make_description(year, df):
    description = "<b>{0}</b><br>".format(year)
    year_data = df[df["Discovery"]==year]
    for i, row in year_data.iterrows():
        description += "<b>Element</b> : {0}({1}) <br>".format(row["Element"], row["Z"])
        description += "by {0} <br>".format(row["Discoverer"])
        
    return description
    
df["description"] = df["year"].apply(make_description, args=(raw_df,))

# Creating plotly trace

trace = Scatter(
    x = df["year"],
    y = df["total"],
    mode = "lines+markers",
    line=Line(
        shape="hv",
        width=2,
        color="#4183D7"
    ),
    marker=Marker(
        color="#4183D7",
        size=4,
        line=Line(
        color='white',
        width=0.5
        )
    ),
    text = df["description"],    
)
        
data = Data([trace])

# Setting up layout parameters
layout = Layout(
    title="Chemical elements discovered over time",
    xaxis=XAxis(
        title = "Year",
        autorange=True
    ), 
    yaxis=YAxis(
        title = "Total elements discovered",
    autorange=True

    ),
    annotations=[Annotation(xref="paper", yref="paper", x=-0.1, y=-0.2, 
                           xanchor="left", yanchor="top",
                           text="Source: https://en.wikipedia.org/wiki/Timeline_of_chemical_element_discoveries",
                           font=Font(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False,)]
)    
    
# Putting it all together in a Figure
fig = Figure(data=data, layout=layout)
 
# Generating online plot
unique_url = py.plot(fig, layout=layout, filename = 'Chemical elements discovery timeline')
        