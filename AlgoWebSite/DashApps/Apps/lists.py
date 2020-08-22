import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

lists = DjangoDash('lists', serve_locally=True, add_bootstrap_links=True)

lists.layout = dbc.Card(style ={'background': '#eaeaea'},
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
                                    dbc.Form(children=[
                                        dbc.FormGroup(children=[
                                            dbc.Label
                                        ])
                                    ])
                                ])
                            ])
                    ])

            ])

if __name__ == '__main__':
    lists.run_server(debug = True)

