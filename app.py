import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.Header(className ='header centerd black-bg',
        children=[
            html.Div(className= "nav centered notify-row",
                id="top-menu",
                     style={'margin-left': '-10px',
                            'margin-bottom': '8px'},
                children=[
                    html.Ul(className="top-menu",
                        children=[
                            html.Li(style={'font-size': '28px',
                                           'margin-top': '8px',
                                           'color': '#f2f2f2',
                                            'text-transform': 'uppercase'},
                                className="centered",
                                children='da'),
                            html.Li(style={'font-size': '28px',
                                           'margin-top': '8px',
                                           'color': '#4ECDC4',
                                            'text-transform': 'uppercase'},
                                children=':'),
                            html.Li(style={'font-size': '28px',
                                           'margin-top': '8px',
                                            'color': '#f2f2f2',
                                            'text-transform': 'uppercase'},
                                children='TA'),

                            ]),
                    html.H6(style={'color': '#4ECDC4',
                                   'text-transform': 'uppercase'},
                        children='Dash Application to Test Algorythms')
                    ])
        ]),
    html.Aside(children=[
        html.Div(id= "sidebar",
            className="nav-collapse",
            children=[
                html.Ul(className="sidebar-menu",
                        style={"margin-top": "115px"},
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
            html.Div(className='row',
                children=[
                html.Div(className="col-lg-9 main-chart",
                         children=["gnagna"]),
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

