import pandas as pd
from numpy import log
import plotly.plotly as py
from plotly.graph_objs import *

# Helper function to format data point description
def make_description(entry):
    name = entry["name"]
    transport_name = entry["ship_name"]
    duration = entry["full_duration"]
    start_date = entry["start_date"]
    end_date = entry["end_date"]
    
    description = """{0} <br>{1}
                <b>Duration</b> : {2} 
                <b>Start date</b> : {3} 
                <b>End date</b> : {4} """.format(name, transport_name, \
                                                duration, start_date, end_date)
        
    return description
    
    
# Importing data in panda and preparing plot args
path = "C:/Users/amate_000/Google Drive/Projects/LOAR/loar_plots/datasets/earth_circumnavigation_records.csv"
df = pd.read_csv(path, sep=",")

categories = df["category"].unique()
traces = []
traces_colors = ["#4183D7", "#F2784B", "#66CC99", "#264348", "#1BA39C", "#4D8FAC", "#D91E18"]
i = 0

# Create specific trace/category and store in list
for category in categories:
    
    # Make description string for each data point
    descriptions = []
    for j, row in df[df["category"]==category].iterrows():
        text = make_description(row)
        descriptions.append(text)
        
    # Create category trace
    trace = Scatter(
        x=df[df["category"]==category]["start_year"],
        y=df[df["category"]==category]["duration"],
        mode="markers",
        name=category,
        text=descriptions,
        marker=Marker(
            color=traces_colors[i],
            size=12,
            line=Line(
                color='white',
                width=0.5
            )
        )
    )
    
    traces.append(trace)
    i+=1

data = Data(traces)

# Setting up layout parameters
layout = Layout(
    title="Earth circumnavigation record over time",
    xaxis=XAxis(
        title = "Year",
        autorange=True
    ), 
    yaxis=YAxis(
        title = "Duration (days)",
    autorange="reversed"

    )
)

# Putting it all together in a Figure
fig = Figure(data=data, layout=layout)
 
# Generating online plot
unique_url = py.plot(fig, layout=layout, filename = 'earth_circumnavigation')
                