import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
from dash.dependencies import Output, Input, State, MATCH, ALL
import os, sys, inspect
from prelog import CheckLog
from prelog import LEVELS as poglevel
from prelog import FORMATS as pogformat
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
dir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)
import DashApps.service.Dunod.list_sorting as svc
import DashApps.toolbox.lists_data as slt

log = CheckLog(fmt=pogformat['locate'])
log.dataProc.setLevel(poglevel['1'])
log.dataIO.setLevel(poglevel['1'])

data_set = slt.DataSet()

app = DjangoDash('lists', suppress_callback_exceptions=True)
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
                               className='btn btn-theme')
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
                                             id="all_lists",
                                children=[]),
                            dcc.Store(id='selected_list',
                                      data='')
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
    [Output('new_list', 'children'),
     Output('all_lists', 'children')],
    [Input('list_gen_bttn', 'n_clicks')],
    [State('new_list_len', 'value')]
)
def newList(bttn_input, list_len):
    with log.sbugCheck(log.dataProc, 'newList'):
        if bttn_input > 0:
            log.dataIO.cmn_dbg(f'{list_len}')
            new_list = svc.generateListe(list_len)
            data = slt.Data(new_list)
            data_set.add(data)
            data_set.sort()
            return (str(data.data), [dbc.DropdownMenuItem(id={
                                    'index': data_set.datas.index(item),
                                    'type': f'list{data_set.datas.index(item)}'},
                                    children=
                       f'List {data_set.datas.index(item)}: n = {len(item.data)}') for item in data_set.datas])


@app.callback(
    Output('selected_list', 'data'),
    [Input({'type': 'registered_list', 'index': ALL}, 'n_clicks')]
)
def selectList(args):
    for item in args:
        if item > 0:
            item = 0
            return data_set.datas[args.index(item)]


if __name__ == '__main__':
    app.run_server(debug = True)

