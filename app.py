# -*- coding: utf-8 -*-
from dash import html, dcc, Output, Input, State, dash_table
import dash_bootstrap_components as dbc
import dash
import dash_auth
import Dashauth
import pandas as pd
import plotly.express as px
import base64
import io
from dash_extensions import Lottie

# Urls
url1 = "https://assets4.lottiefiles.com/packages/lf20_zlrpnoxz.json"
url2 = "https://assets3.lottiefiles.com/packages/lf20_ezkqui33.json"
url3 = "https://assets7.lottiefiles.com/packages/lf20_ic37y4kv.json"
url4 = "https://assets3.lottiefiles.com/packages/lf20_m4wmgweb.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

df1 = pd.read_csv('mtak.csv')

# Uplines /Agents
bestUplinegraph = df1['Agents'].value_counts()

fig = px.bar(bestUplinegraph, y=bestUplinegraph.values, x=bestUplinegraph.keys(), text_auto='.2s',
             title="Agents Performance", width=600, height=600,
             labels={
                 "y": "Total registered traders"})

bestUplineName = list(bestUplinegraph.items())[0][0]
bestUplinevalue = list(bestUplinegraph.items())[0][1]

# Markets
bestMarketsgraph = df1['Markets'].value_counts()

bestMarketsName = list(bestMarketsgraph.items())[0][0]
bestMarketsValue = list(bestMarketsgraph.items())[0][1]

fig1 = px.bar(bestMarketsgraph, y=bestMarketsgraph.values, x=bestMarketsgraph.keys(),
              text=bestMarketsgraph.values, text_auto='.2s',
              title="Markets Performance", width=600, height=600,
              labels={
                  "y": "Total registered traders"})

# Total Income
totalIncome = df1['Transamount'].sum()

bestSubCounties = df1['Sub-counties'].value_counts()

fig3 = px.bar(bestSubCounties, y=df1['Sub-counties'].value_counts().values, x=df1['Sub-counties'].value_counts().keys(),
              labels={
                  "y": "Total registered traders",
                  "x": "Sub county"}
              )

# Members per Counties
bestCounties = df1['Counties'].value_counts()

fig6 = px.bar(bestCounties, y=bestCounties.values, x=bestCounties.keys(),
              labels={
                  "y": "Total registered traders",
                  "x": "Counties"}
              )

# Amount Transacted per Sub-Counties
bestAmounts = df1['Transamount'].value_counts()

fig4 = px.bar(df1, y=df1['Transamount'], x=df1['Sub-counties'], color=df1['Counties'],
              labels={
                  "Sub-counties": "Sub counties",
                  "Transamount": "Money Transacted (kshs)"},
              title="Amount transacted per month")
fig4.update_layout(
    bargap=0.1,
    plot_bgcolor="#fafafa",
    paper_bgcolor="#fafafa",
    # font_color="#097733"
)

app = dash.Dash(external_stylesheets=[dbc.themes.VAPOR], title='Dash App 1 Analytics')

server = app.server

auth = dash_auth.BasicAuth(
    app,
    Dashauth.VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=url2)),
                            html.H5("Best Markets", className="card1", style={'color': 'white', 'font-size': '28',
                                                                              'textAlign': 'center'}),
                            dbc.Row([
                                dbc.Col([
                                    html.H3(bestMarketsName)
                                ], style={'color': 'white', 'font-size': '28',
                                          'textAlign': 'left'}
                                ),
                                dbc.Col([
                                    html.Div([html.H3([bestMarketsValue], style={'color': 'white', 'font-size': '28',
                                                                                 'textAlign': 'right'}),
                                              html.P("traders")], style={'color': 'white', 'font-size': '28',
                                                                         'textAlign': 'right'})
                                ])
                            ]),
                            html.P(
                                "Best performing Market", style={'color': 'info', 'font-size': '20',
                                                                 'textAlign': 'center'},
                                className="card-text1"
                            ),
                            dbc.Button("More Info", color="info", className="me-1", id="tooltip-target"),
                            dbc.Tooltip([dcc.Graph(figure=fig1)], target="tooltip-target", trigger="click",
                                        delay={'show': 0, 'hide': 200},
                                        style={'max-width': '700px', 'padding': '.25rem .5rem',
                                               'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                               'border-radius': '.25rem'}
                                        )
                        ]
                    )
                ]
            )
        ]),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=url4)),
                            html.H5("Total Income", className="card1", style={'color': 'white', 'font-size': '28',
                                                                              'textAlign': 'center'}),
                            dbc.Row([
                                dbc.Col([
                                    html.H3([str(totalIncome)],
                                            style={'font-size': '22', 'textAlign': 'center'}
                                            ),
                                    html.P(["Kshs"], style={'font-size': '12', 'textAlign': 'center'})
                                ])
                            ]),
                            html.P(
                                "Total amount deposited",
                                className="card-text1", style={'color': 'info', 'font-size': '20',
                                                               'textAlign': 'center'}
                            )
                        ]
                    )
                ]
            )
        ]),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=url3)),
                            html.H5("Best Agents", className="card1", style={'color': 'white', 'font-size': '28',
                                                                             'textAlign': 'center'}),
                            dbc.Row([
                                dbc.Col([
                                    html.Div(
                                        html.H3(bestUplineName, style={'font-size': '22', 'textAlign': 'left'})
                                    )
                                ]),
                                dbc.Col([
                                    html.Div([
                                        html.H3([bestUplinevalue], style={'font-size': '22', 'textAlign': 'right'}),
                                        html.P(["traders"], style={'font-size': '12', 'textAlign': 'right'})
                                    ])
                                ])
                            ]),
                            html.P(
                                "Best performing Agent",
                                className="card-text1", style={'color': 'info', 'font-size': '20',
                                                               'textAlign': 'center'}
                            ),
                            dbc.Button("More Info", color="info", className="me-1", id="tooltip-target2"),
                            dbc.Tooltip([dcc.Graph(figure=fig)], target="tooltip-target2", placement="bottom",
                                        delay={'show': 0, 'hide': 200}, trigger="click",
                                        style={'max-width': '700px', 'padding': '.25rem .5rem',
                                               'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                               'border-radius': '.25rem'}
                                        )
                        ]
                    )
                ]
            )
        ])
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                dcc.Upload(
                    id='datatable-upload',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%', 'height': '60px', 'lineHeight': '60px',
                        'borderWidth': '1px', 'borderStyle': 'dashed',
                        'borderRadius': '1px', 'textAlign': 'center', 'margin': '1px'
                    },
                )]),
            dbc.CardBody([
                dash_table.DataTable(
                    id='datatable-upload-container',
                    sort_action='native',
                    style_table={'height': '500px', 'overflowY': 'auto', 'overflowX': 'auto', 'color': 'black'},
                    style_data_conditional=[
                        {
                            'if': {
                                'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                                'column_id': 'Humidity'
                            },
                            'color': 'green',
                            'fontWeight': 'bold'
                        },
                        {
                            'if': {
                                'filter_query': '{Pressure} > 19',
                                'column_id': 'Pressure'
                            },
                            'textDecoration': 'underline'
                        },
                        {
                            'if': {
                                'filter_query': '{Region} = "San Francisco"'
                            },
                            'backgroundColor': '#0074D9',
                            'color': 'black'
                        }
                    ],
                    style_data={
                        'color': 'black'
                    },
                    editable=True,
                    filter_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=50,
                    export_format='xlsx',
                    export_headers='display',
                    merge_duplicate_headers=True
                ),
                dbc.Alert(id='tbl_out')]),
            dbc.CardBody([
                dbc.Label(['Market Analysis'], style={'font-size': '22', 'textAlign': 'center',
                                                      'font-family': 'Arial'}),
                dcc.Graph(id='datatable-upload-graph')
            ]),
        ], className="card3"),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody("Amount Transacted per county", style={'font-size': '22', 'textAlign': 'center',
                                                                    'font-family': 'Arial'}),
                className="card4",
            ),
            dcc.Graph(figure=fig6)
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody("Sub-county Analysis", style={'font-size': '22', 'textAlign': 'center',
                                                           'font-family': 'Arial'}),
                className="card5",
            ),
            dcc.Graph(figure=fig3)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody("Amount per sub-counties vs counties",
                             style={'font-size': '22', 'textAlign': 'center', 'font-family': 'Arial'}),
                className="card6",
            ),
            dcc.Graph(figure=fig4)
        ])
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Button('Change', id='btn-nclicks-1', style={'font-size': '20', 'color': 'white'}),
            html.Br(),
            html.Br(),
            dbc.Card([
                html.H6("Agents", style={'color': 'white', 'font-size': 14}),
                dcc.Dropdown(df1['Agents'].unique(), 'Bob', id='dropdown-1'),
            ], className="card7", style={'color': 'black', 'font-size': 14}),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Card([
                html.H6("Markets", style={'color': 'white', 'font-size': 14}),
                dcc.Dropdown(df1['Markets'].unique(), id='dropdown-2'),
            ], className="card7", style={'color': 'black', 'font-size': 14}),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Card([
                html.H6("Counties", style={'color': 'white', 'font-size': 14}),
                dcc.Dropdown(df1['Counties'].unique(), id='dropdown-3'),
            ], className="card7", style={'color': 'black', 'font-size': 14})
        ]),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(dcc.Graph(id='marketTrends'
                                       ))
            )
        ], width=8)
    ])
], style={'marginTop': '10px', "color": "#3cf281", 'marginRight': '10px', 'marginBottom': '10px',
          'marginLeft': '100px', "border": "2px LightGreen"})


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an Excel file
        return pd.read_excel(io.BytesIO(decoded))


@app.callback(Output('datatable-upload-container', 'data'),
              Output('datatable-upload-container', 'columns'),
              Input('datatable-upload', 'contents'),
              State('datatable-upload', 'filename'))
def update_output(contents, filename):
    if contents is None:
        return [{}], []
    df = parse_contents(contents, filename)
    return df.to_dict('records'), [
        {"name": i, "id": i, "clearable": True, "renamable": True, "hideable": True, "deletable": True} for i in
        df.columns]


@app.callback(Output('datatable-upload-graph', 'figure'),
              Input('datatable-upload-container', 'data'))
def display_graph(rows):
    df = pd.DataFrame(rows)
    if df.empty or len(df.columns) < 1:
        return {
            'data': [{
                'x': [],
                'y': [],
                'type': 'bar'
            }]
        }
    return {
        'data': [{
            'x': df[df.columns[0]],
            'y': df[df.columns[1]],
            'type': 'bar'
        }]
    }


@app.callback(
    Output("marketTrends", "figure"),
    Input("dropdown-1", "value"),
    Input("dropdown-2", "value"),
    Input("dropdown-3", "value"),
    Input("btn-nclicks-1", "n_clicks")
)
def create_dashboard4(value, value1, value2, value3):
    df2 = pd.read_csv('mtak.csv', parse_dates=["TransTime"])

    df2 = df2[(df2.Agents == value) | (df2.Markets == value1) | (df2.Counties == value2)]

    if value3 is None or value3 == 2 or value3 == 4 or value3 == 6 or value3 == 8 or value3 == 10 or value3 == 12 \
            or value3 == 14 or value3 == 16 or value3 == 18 or value3 == 20 or value3 == 22:
        fig7 = px.histogram(df2, x='TransTime', y='Transamount', histfunc="avg", nbins=10, text_auto=True,
                            labels={
                                "TransTime": "Months",
                                "Transamount": "transacted money (kshs)"},
                            title="Amount of money transacted per month",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl
                            )
        fig7.update_layout(
            bargap=0.1,
            # plot_bgcolor="#3cf281",
            # paper_bgcolor="#3cf281",
            font_color="#097733"
        )

        return fig7

    else:
        fig7 = px.pie(df2, values='Transamount', names='Counties',
                      title='Total amount transacted per county',
                      hole=.3, color_discrete_sequence=px.colors.sequential.Aggrnyl,
                      hover_data=['Agents'])

        return fig7


if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, port=5000)
