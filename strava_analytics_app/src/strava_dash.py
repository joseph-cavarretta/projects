"""
Created on Nov 13, 2022 14:11:23
Created by Joe Cavarretta
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()
df = pd.read_csv('data/processed_activities.csv')

app.layout = html.Div(id = 'parent', children = [
     html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                             'marginTop':40,'marginBottom':40}),
         dcc.Dropdown( id = 'dropdown',
         options = [
             {'label':'Run', 'value':'Run' },
             {'label': 'Bike', 'value':'Bike'},
             {'label': 'Strength', 'value':'WeightTraining'},
             ],
         value = 'Run'),
         dcc.Graph(id = 'bar_plot')
     ])

    
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
               [Input(component_id='dropdown', component_property= 'value')])
def graph_update(dropdown_value):
     print(dropdown_value)
     fig = go.Figure([go.Scatter(x = df['year'], y = df['{}'.format(dropdown_value)],\
                      line = dict(color = 'firebrick', width = 4))
                      ])
    
     fig.update_layout(title = 'Stock prices over time',
                       xaxis_title = 'Dates',
                       yaxis_title = 'Prices'
                       )
     return fig  



if __name__ == '__main__': 
    app.run_server()