import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
from dash.dependencies import Output, Input, State
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
dir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)
from DashApps.service.Dunod.listSortings import *


app = DjangoDash('lists', serve_locally=True, add_bootstrap_links=True)

app.layout = dbc.Card(style ={'background': '#eaeaea',
                                'height': '800px'},
                children=[
                    dbc.CardHeader(children=[
                        html.H2(className='card-title',
                            children='List Sorting'),
                        ]),
                    dbc.CardBody(children=[
                        dbc.Card(children=[
                            dbc.CardHeader(children=[html.H5(className='card-title',
                                                         children='List Generator')]),
                            dbc.CardBody(children=[
                                dbc.Col(children=[
                                    dbc.Form(children=[
                                        dbc.FormGroup(children=[
                                            dbc.Label("Enter list length",
                                                          style={'width': '300px'}),
                                            dbc.Input(type="number",
                                                      style={'width': '300px'},
                                                      id="new_list_len",
                                                      value='')
                                            ]),
                                        dbc.Button('Generate list', n_clicks=0, id='list_gen_bttn', key='list_gen')
                                        ])
                                    ]),
                                dbc.Col(children=[
                                    html.P('', id='new_list')
                                    ])
                                ]),
                            dbc.CardFooter(style = {'align': 'center'},
                                           children=[
                                html.P(children=['List 1'])
                                ])
                            ])
                        ])
                    ])

@app.callback(
    Output('new_list', 'children'),
    [Input('list_gen_bttn', 'n_clicks')],
    [State('new_list_len', 'value'),
     State('list_tabs', 'value')]
)
def newList(bttn_input, list_len, list_number):
    if bttn_input > 0:
        new_list = generateListe(list_len)
        return new_list

if __name__ == '__main__':
    app.run_server(debug = True)

