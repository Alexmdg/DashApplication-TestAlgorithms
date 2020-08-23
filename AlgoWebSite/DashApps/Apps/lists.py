import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
from dash.dependencies import Output, Input, State
import os, sys, inspect
from prelog import CheckLog
from prelog import LEVELS as poglevel
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
dir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)
from DashApps.service.Dunod.listSortings import *

log = CheckLog()
log.dataProc.setLevel(poglevel['1'])

app = DjangoDash('lists')
# app.css.append_css('AlgoWebSite/static/css/style.css')

app.layout = html.Div(className='col-lg-9 main-chart',
                             children=[
                        html.Div(className='border-head',
                            children=[
                            html.H2(children='List Sorting')
                            ]),
                    dbc.CardBody(children=[
                        dbc.Card(children=[
                            dbc.CardHeader(children=[html.H5(className='card-title',
                                                         children='List Generator')]),
                            dbc.CardBody(children=[
                                dbc.Row(children=[
                                    dbc.Col(children=[
                                        dbc.Form(style={'width': '350px',
                                                        'vertical-align': 'center'},
                                            children=[
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
                                    dbc.Col(style={'width': '350px'},
                                        children=[
                                        html.P(children='',
                                               id='new_list',
                                               style={'width': '200px',
                                                  'height': '200px',
                                                  'overflow': 'scroll'})
                                        ])
                                    ])
                                ]),
                            dbc.CardFooter(style = {'align': 'center'},
                                           children=[
                                html.P(children=['List 1'])
                                ])
                            ])
                        ])
                    ])


# @app.callback(
#     Output('new_list', 'children'),
#     [Input('list_gen_bttn', 'n_clicks')],
#     [State('new_list_len', 'value')]
# )
# def newList(bttn_input, list_len):
#     with log.cbugCheck(log.dataProc):
#         if bttn_input > 0:
#             new_list = generateListe(list_len)
#             return str(new_list)

if __name__ == '__main__':
    app.run_server(debug = True)

