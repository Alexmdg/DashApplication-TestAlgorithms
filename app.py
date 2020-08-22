import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(
    meta_tags=[
        {'name': 'viewport',
         'content': 'width=device-width, initial-scale=1.0'}
    ]
)

app.layout = html.Div(id='container',
                      className='sidebar-close sidebar-closed',
                      children=[
    html.Header(className ='header black-bg',
        children=[
            html.Div(className= "nav centered notify-row",
                id="top-menu",
                     style={'margin-left': '-10px',
                            'margin-bottom': '10px'},
                children=[
                    html.Ul(className="nav top-menu",
                        children=[
                            html.Li(style={'font-size': '32px',
                                           'color': '#f2f2f2',
                                            'text-transform': 'uppercase'},
                                className="centered",
                                children='da'),
                            html.Li(style={'font-size': '32px',
                                           'color': '#4ECDC4',
                                            'text-transform': 'uppercase'},
                                children=':'),
                            html.Li(style={'font-size': '32px',
                                            'color': '#f2f2f2',
                                            'text-transform': 'uppercase'},
                                children='TA'),
                            html.Li(style={'color': '#4ECDC4',
                                           'margin-top': '10px',
                                           'margin-left': '15px',
                                           'font-size': '14px',
                                           'text-transform': 'uppercase'},
                                children='Dash Application -'),
                            html.Li(style={'color': '#4ECDC4',
                                   'margin-top': '10px',
                                   'font-size': '14px',
                                   'text-transform': 'uppercase'},
                                children='- Test Algorithms'),
                            ]),
                    ]),
            html.Div(className="top-menu",
                     style={'display': 'block'},
                children=[
                    html.Ul(className="top-nav pull-right top-menu",
                     style={'display': 'block'},
                        children=[
                            html.Li(style={'color': '#4ECDC4',
                                          'font-size': '12px',
                                          'text-transform': 'uppercase'},
                                    children='sourc'),
                            html.Li(style={'font-size': '12px',
                                           'color': '#4ECDC4',
                                           'text-transform': 'uppercase'},
                                children='e code'),
                            html.Li(style={'font-size': '12px',
                                           'font-weight': 'bold',
                                           'color': '#4ECDC4',
                                           'text-transform': 'uppercase'},
                                children=':'),
                            html.Li(style={'font-size': '12px',
                                           'color': '#f2f2f2',
                                           'text-transform': 'uppercase'},
                                children='https://github.com/Alexmdg/DashApplication-TestAlgorithms'),

                            ]),
                    html.Ul(className="top-nav pull-right top-menu",
                     style={'display': 'block'},
                        children=[
                            html.Li(style={'color': '#4ECDC4',
                                          'font-size': '12px',
                                          'text-transform': 'uppercase'},
                                    children='E-mail:'),
                            html.Li(style={'font-size': '12px',
                                           'color': '#f2f2f2',
                                           'text-transform': 'uppercase'},
                                children='alexmdg@protonmail.com')
                            ]),
                    html.Ul(className="top-nav pull-right top-menu",
                     style={'display': 'block'},
                        children=[
                            html.Li(style={'font-size': '12px',
                                           'font-weight': 'bold',
                                           'color': '#4ECDC4',
                                           'text-transform': 'uppercase'},
                                children='Telegram'),
                            html.Li(style={'font-size': '12px',
                                           'color': '#f2f2f2',
                                           'text-transform': 'uppercase'},
                                children='gnagnagnatelegram'),

                            ]),
                    ])
            ]),
    html.Aside(children=[
        html.Div(id= "sidebar",
            className="nav-collapse",
                 style={'overflow': 'hidden',
                        'outline': 'none'},
            children=[
                html.Ul(className="sidebar-menu",
                        id="nav-accordion",
                    children=[
                        html.H5(className="centered",
                            children="Algorythm Types"),
                        html.Li(className="mt",
                            children=[
                                html.Span(style = {'color': '#aeb2b7'},
                                    children="List Sorting")
                            ])
                        ])
                    ])
                ]),
    html.Section(id = "main-content",
        children=[
            html.Section(className = "wrapper",
                children=[
                    html.H2(children='List Sorting'),
                    html.Div(className='row',
                        children=[
                            html.Div(className="col-lg-9 main-chart",
                                children=[
                                    html.Div(className="row",
                                        children=[
                                            html.Div(className="col-md-8 mb",
                                                children=[
                                                    html.Div(className="message-p pn",
                                                        children=[
                                                            html.Div(className="message-header",
                                                                children=[html.H5('Lists Generator')]),
                                                            html.Div(className='row',
                                                                children=[
                                                                    html.Div(className='col-md-9',
                                                                        children=[])
                                                                ])
                                                            ])
                                                    ])

                                            ])
                                    ]),

                            html.Div(className="col-lg-3 ds",
                                     children="gnagnagna")
                            ]),
                        ])
            ]),
    html.Footer(className="site-footer",
                children=[])
])


if __name__ == '__main__':
    app.run_server(debug = True)

