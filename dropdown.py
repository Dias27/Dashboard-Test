import pandas as pd
import plotly
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


df = pd.read_csv("Data/titanic.csv")

app.layout = html.Div([

    dcc.Dropdown(id='my_dropdown',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.columns)],

                 optionHeight=35,  # height/space between dropdown options
                 value='name',  # dropdown value selected automatically when page loads
                 disabled=False,  # disable dropdown value selection
                 multi=True,  # allow multiple dropdown values to be selected
                 searchable=True,  # allow user-searching of dropdown values
                 search_value='',  # remembers the value searched in dropdown
                 # gray, default text shown when no option is selected
                 placeholder='Please select...',
                 clearable=True,  # allow user to removes the selected value
                 # use dictionary to define CSS styles of your dropdown
                 style={'width': "50%"},
                 ),
    # 'session': browser tab is closed
    # 'local': browser cookies are deleted
    #

    html.Div([
        dcc.Graph(id='bar-graph', figure={'data': [
             {'x': df['pclass'], 'y':df['survived'],
                 'type':'bar', 'name':'survived per class'},
             {'x': df['pclass'], 'y':df['age'],
                 'type':'bar', 'name':'survived per age'}
             ],

            'layout':{'title': 'BAR PLOTS !'}}),

    ])


])

if __name__ == '__main__':
    app.run_server()
