import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.Header(className ='header black-bg',
            children='Algorithm Testing App'),
    html.Aside(className='sidebar',
        children=[
        html.Div(id= 'sidebar',
                 className= 'header black-bg',
                 children='gna')
    ]),
    html.Section(id = "main-content",
         children=[
         html.Section(className = "wrapper",
              children=[
              html.Div(className='row',
                    children=[
                    html.Div(className="col-lg-9 main-chart",
                             children="gnagna"),
                    html.Div(className="col-lg-3 ds",
                             children="gnagnagna")

            ])
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug = True)

