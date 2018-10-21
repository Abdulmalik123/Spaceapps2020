import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import sqlite3

#reading data
dfNormal = pd.read_csv('Data//dfNormal.csv')
dfStorm = pd.read_csv('Data//dfStorm.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='JCIB ForensX'),
    dcc.Graph(
        id='example-graph',
    ),
    dcc.Interval(
        id='graph-update',
        interval=1*1000),
    dcc.Graph(
        id='graph-example',
        figure={
            'data':[
                {
                    'x':dfStorm['time'],
                    'y':dfStorm['value'],
                    'name':'Sand Storm',
                },
                {
                    'x':dfNormal['time'],
                    'y':dfNormal['value'],
                    'name':'Sand Storm',
                }
            ],
            'layout':{
                'title': 'Sand Storm vs Normal',
                'xaxis':{
                    'title':'Time (seconds)'
                },
                'yaxis':{
                    'title':'Light Intensity'
                }
            }
        }
    )
])

@app.callback(Output('example-graph', 'figure'),
events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    print('update')
    #Column names are TimeStamp and Value
    #Value is the reading from photon resistor                                                              m the sensor
    #range is roughtly 0-3000 right now
    conn = sqlite3.connect('Data//marsSensor.db')
    c = conn.cursor() # contians table light with columns time and value    
    df = pd.read_sql_query("select * from light", conn)
    x = df['time']
    y = df['value']
    figure={
        'data':[
            {'x':x,
            'y':y,
            'type':'scatter',}
        ],
        'layout':{
            'title':'Live Graph of Light Intensity Vs Time',
            'xaxis':{
                'title':'Time (seconds)'
            },
            'yaxis':{
                'title':'Light Intensity'
            }
        }
    }
    return figure

if __name__ == "__main__":
    app.run_server(debug=True)