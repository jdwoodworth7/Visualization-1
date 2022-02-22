import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [
    go.Scatter(x=df['actual_max_temp'],
               y=df['actual_min_temp'],
               text=df['date'],
               mode='markers',
               marker=dict(size=df['actual_max_temp'],color=df['actual_min_temp'], showscale=True))
]

# Preparing layout
layout = go.Layout(title='Temperatures', xaxis_title="Actual Max Temperature",
                   yaxis_title="Actual Min Temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')