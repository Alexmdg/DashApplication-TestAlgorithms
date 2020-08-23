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
import DashApps.service.Dunod.listSorting as svc

log = CheckLog()
log.dataProc.setLevel(poglevel['1'])

app = DjangoDash('lists')
# app.css.append_css('AlgoWebSite/static/css/style.css')


app.layout = html.Div(className='row',
children=[
    html.Div(className='col-lg-9 main-chart',
        children=[
        html.Div(className='border-head',
            children=[
            html.H2(children='List Sorting')
            ]),
        html.Div(className='message-header',
            children=[
            html.H5(children='List Generator')
            ]),
        html.Div(className='row mt',
            children=[
            html.Div(className='col-md-4 col-sm-4 mb',
                children=[
                html.P('Enter a length to generate a new random list',
                        className='message'),
                html.Form(className='form-inline', role='form',
                    children=[
                    html.Div(className='form-group',
                        children=[
                        dbc.Input(type="number",
                                  className='form-control',
                                  id="new_list_len",
                                  value='')
                        ]),
                    dbc.Button('Generate list',
                               n_clicks=0,
                               id='list_gen_bttn',
                               key='list_gen',
                               className='btn btn-default')
                    ]),
                ]),
                html.Div(className='col-md-4 col-sm-4 mb',
                    children=[
                    html.P(children='',
                           id='new_list',
                           style={'height': '160px',
                                  'overflow': 'scroll'})
                    ]),
                html.Div(className='col-md-4 col-sm-4 mb',
                    children=[
                    html.P('Registered lists :',
                            className='message'),
                    html.Form(className='form-inline', role='form',
                        children=[
                        html.Div(className='form-group',
                            children=[
                            dbc.DropdownMenu(className='form-control',
                                             id="new_list_len",
                                children=[])
                            ]),
                        dbc.Button('Delete List',
                                   n_clicks=0,
                                   id='list_del_bttn',
                                   key='list_del',
                                   className='btn btn-theme')
                        ]),
                    ]),
                ])
            ]),
        html.Div(className='col-lg-3',
            children=[])
        ])



@app.callback(
    Output('new_list', 'children'),
    [Input('list_gen_bttn', 'n_clicks')],
    [State('new_list_len', 'value')]
)
def newList(bttn_input, list_len):
    with log.cbugCheck(log.dataProc):
        if bttn_input > 0:
            new_list = svc.generateListe(list_len)
            return str(new_list)


if __name__ == '__main__':
    app.run_server(debug = True)

