import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
from dash.dependencies import Output, Input, State, MATCH, ALL
import os, sys, inspect, ujson
from prelog import CheckLog
from prelog import LEVELS as poglevel
from prelog import FORMATS as pogformat

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
dir = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)

import DashApps.algos.Dunod.list_sorting as svc
import DashApps.toolbox.list_datas as slt

log = CheckLog(fmt=pogformat['locate'])
log.dataProc.setLevel(poglevel['1'])
log.dataIO.setLevel(poglevel['1'])

data_set = slt.DataSet()

app = DjangoDash('lists', suppress_callback_exceptions=True)
app.layout = html.Div(className='row',
children=[
    html.Div(className='col-lg-9',
        children=[
        html.Div(className='border-head',
            children=[
            html.H2(children='List Sorting'),
            html.H5('Use the list generator to generate some random lists of '),
            ]),
        html.Div(className='row mt',
            children=[
            html.Div(className='content-panel',
                children=[
                html.H4('Sort by : Insertion'),
                html.Section(className='unseen',
                    children=[
                    html.Table(style={'border': '0'},
                        className='table table-striped table-condensed',
                        children=[
                            html.Thead(children=[
                            html.Tr(children=[
                                html.Td('', style={'max-width': '100px'}),
                                html.Td('Desc', style={'max-width': '200px'}),
                                html.Td('Complexity', style={'max-width': '200px'}),
                                html.Td('Time results'),
                                html.Td('Graph results')
                                ])
                            ]),
                        html.Tbody(style={'border': '0'},
                            children=[
                            html.Tr(style={'border': '0'},
                                children=[
                                html.Td(children=[
                                    dbc.Button('Run Tests',
                                             style={'max-width': '100px'},
                                             n_clicks=0,
                                             id="insert_run_bttn",
                                             key='insert_run_bttn',
                                             className='btn btn-theme'),
                                    dcc.Store(id='insert_result_store', data='')
                                    ]),
                                html.Td('This algorithm will compare each element to every other element',
                                        style={'max-width': '100px'}),
                                html.Td('Complexity for the worst case is n². For best case it is n²/2',
                                        style={'max-width': '100px'}),
                                html.Td(id='insert_sort_results', children=[]),
                                html.Td(id='insert_sort_graph', children=[]),
                                ])
                            ]),
                        ])
                    ])
                ])
            ]),
        html.Div(className='row mt',
            children=[
            html.Div(className='content-panel',
                children=[
                html.H4('Sort by : Recursive Merging'),
                html.Section(className='unseen',
                    children=[
                    html.Table(style={'border': '0'},
                        className='table table-striped table-condensed',
                        children=[
                            html.Thead(children=[
                            html.Tr(children=[
                                html.Td('', style={'max-width': '100px'}),
                                html.Td('Desc', style={'max-width': '200px'}),
                                html.Td('Complexity', style={'max-width': '200px'}),
                                html.Td('Time results'),
                                html.Td('Graph results')
                                ])
                            ]),
                        html.Tbody(style={'border': '0'},
                            children=[
                            html.Tr(style={'border': '0'},
                                children=[
                                html.Td(children=[
                                    dbc.Button('Run Tests',
                                             n_clicks=0,
                                             id="merge_run_bttn",
                                             key='merge_run_bttn',
                                             className='btn btn-theme')
                                    ]),
                                    html.Td('This algorithm will compare each element to every other element',
                                            style={'max-width': '100px'}),
                                    html.Td('Complexity for the worst case is n². For best case it is n²/2',
                                            style={'max-width': '100px'}),
                                    html.Td(id='merge_sort_results', children=[]),
                                    html.Td(id='merge_sort_graph', children=[]),
                                ])
                            ]),
                        ])
                    ])
                ])
            ]),
        html.Div(className='row mt',
            children=[
            html.Div(className='content-panel',
                children=[
                html.H4("Sort by : 'heapq' Module"),
                html.Section(className='unseen',
                    children=[
                    html.Table(style={'border': '0'},
                        className='table table-striped table-condensed',
                        children=[
                            html.Thead(children=[
                            html.Tr(children=[
                                html.Td('', style={'max-width': '100px'}),
                                html.Td('Desc', style={'max-width': '200px'}),
                                html.Td('Complexity', style={'max-width': '200px'}),
                                html.Td('Time results'),
                                html.Td('Graph results')
                                ])
                            ]),
                        html.Tbody(style={'border': '0'},
                            children=[
                            html.Tr(style={'border': '0'},
                                children=[
                                html.Td(children=[
                                    dbc.Button('Run Tests',
                                             n_clicks=0,
                                             id="heapify_run_bttn",
                                             key='heapify_run_bttn',
                                             className='btn btn-theme')
                                    ]),
                                html.Td('This algorithm will compare each element to every other element',
                                        style={'max-width': '100px'}),
                                html.Td('Complexity for the worst case is n². For best case it is n²/2',
                                        style={'max-width': '100px'}),
                                html.Td(id='heapify_sort_results', children=[]),
                                html.Td(id='heapify_sort_graph', children=[]),
                                ])
                            ]),
                        ])
                    ])
                ])
            ])
        ]),
    html.Div(className='col-lg-3 ds',
        children=[
        html.Div(className='message-header',
            style={'margin-bottom': '30px'},
            children=[
             html.H3(children='List Generator')
            ]),
        html.H5('Enter a length to generate a new random list',
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
                     style={'margin-bottom': '19px'},
                     className='btn btn-theme')
            ]),
        dcc.Store(id='new_list_store', data=''),
        html.H4('Selected list:',
                className='message'),
        html.P(children='',
               id='show_list',
               style={'height': '160px',
                      'margin-bottom': '19px',
                      'overflow': 'scroll'}),
        html.H4('Registered lists :',
                className='message'),
        html.Form(className='form', role='form',
            children=[
            html.Div(className='form-group',
                children=[
                dcc.Store(id='selected_list_store',
                          data=''),
                dcc.Dropdown(id="all_lists",
                             options=[],
                             value=None),
                ]),
            dbc.Button('Delete List',
                       n_clicks=0,
                       id='list_del_bttn',
                       key='list_del',
                       className='btn btn-theme'),
            dcc.Store(id='del_list_store', data='')
            ]),
        ])
    ])

##          List generator callbacks            ##
@app.callback(
    Output('new_list_store', 'data'),
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
            return (ujson.dumps(data.datas))


@app.callback(
    Output('selected_list_store', 'data'),
    [Input('all_lists', 'value')]
)
def selectedList(list_index):
    log.dataIO.cmn_dbg(list_index)
    return ujson.dumps(data_set.datas[list_index].data)


@app.callback(
    Output('del_list_store', 'data'),
    [Input('list_del_bttn', 'n_clicks')],
    [State('all_lists', 'value')]
)
def deletedList(click, list_index):
    data_set.raw_datas.remove(data_set.raw_datas[list_index])
    data_set.sort()
    return f'List {list_index} deleted'


@app.callback(
    Output('show_list', 'children'),
    [Input('new_list_store', 'data'),
    Input('selected_list_store', 'data'),
    Input('del_list_store', 'data')]
)
def show_list(new, selected, deleted):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'].split('.')[0] == 'new_list_store':
        return str(ujson.loads(new))
    elif ctx.triggered[0]['prop_id'].split('.')[0] == 'del_list_store':
        return deleted
    else:
        return str(ujson.loads(selected))


@app.callback(
    Output('all_lists', 'options'),
    [Input('new_list_store', 'data'),
     Input('del_list_store', 'data')],
)
def allListsMenuOptions(gen_trig, del_trig):
    return [{'label': f'List {data_set.raw_datas.index(item)}: n = {len(item.datas)}',
      'value': data_set.raw_datas.index(item)} for item in data_set.raw_datas]

##          List generator callbacks end            ##

@app.callback(
    Output('insert_sort_results', 'children'),
    [Input('insert_run_bttn', 'n_clicks')]
)
def insertTest(click):
    data_set.run_tests('insert')
    children = [html.P(f'n = {len(item.datas)} : {round(item.insert_sort_time, 3)}s')\
                       for item in data_set.raw_datas]
    children.append(html.P(f'Total : {round(data_set.insert_sort_time, 3)}s'))
    return children

@app.callback(
    Output('merge_sort_results', 'children'),
    [Input('merge_run_bttn', 'n_clicks')]
)
def mergeTest(click):
    data_set.run_tests('merge')
    children = [html.P(f'n = {len(item.datas)} : {round(item.merge_sort_time, 3)}s')\
                       for item in data_set.raw_datas]
    children.append(html.P(f'Total : {round(data_set.merge_sort_time, 3)}s'))
    return children

@app.callback(
    Output('heapify_sort_results', 'children'),
    [Input('heapify_run_bttn', 'n_clicks')]
)
def insertTest(click):
    data_set.run_tests('heapify')
    children = [html.P(f'n = {len(item.datas)} : {round(item.heapify_sort_time, 3)}s')\
                       for item in data_set.raw_datas]
    children.append(html.P(f'Total : {round(data_set.heapify_sort_time, 3)}s'))
    return children


if __name__ == '__main__':
    app.run_server(debug=True)



