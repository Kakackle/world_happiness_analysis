from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as graph_objects

from dataframes import (
    df,
    metric_graph_columns
)

# ---------------------------------------------------------------------------- #
#               Metric vs ladder score for every country scatter               #
# ---------------------------------------------------------------------------- #

metric_vs_ladder_controls = dbc.Card(
    [
        html.Div(
            [
            dbc.Label("Metric"),
            dcc.Dropdown(
                id='metric-vs-ladder-selection',
                value = 'Social support',
                options = [col for col in metric_graph_columns if col != 'Ladder score']
            )
            ]),
    ],
    body=True,
)

metric_vs_ladder_container = dbc.Container([
    html.H1(children = 'Chosen metric vs ladder score', style={'textAlign': 'center'}),
    html.P(id='metric-vs-ladder-test'),
    dbc.Row(
        [
            dbc.Col(metric_vs_ladder_controls, md=4),
            dbc.Col(dcc.Graph(id='metric-vs-ladder-graph'), md=8),
        ],
        align="center",
    ),
], fluid=True)

def get_metric_vs_ladder_callbacks(app):
    @app.callback(
        [
            Output('metric-vs-ladder-graph', 'figure'),
            Output('metric-vs-ladder-test', 'children')
        ],
        [
            Input('metric-vs-ladder-selection', 'value'),
        ]
    )
    def update_metric_vs_ladder_graph(metric):
        fig = px.scatter(df, y='Ladder score', x=metric, hover_data='Country', color='Regional Indicator',)
        return fig, f'metric: {metric}'
        # return fig
    

# ---------------------------------------------------------------------------- #
#              Metric vs life expectancy for every country scatter             #
# ---------------------------------------------------------------------------- #
metric_vs_life_controls = dbc.Card(
    [
        html.Div(
            [
            dbc.Label("Metric"),
            dcc.Dropdown(
                id='metric-vs-life-selection',
                value = 'Social support',
                options = [col for col in metric_graph_columns if col != 'Life expectancy']
            )
            ]),
    ],
    body=True,
)

metric_vs_life_container = dbc.Container([
    html.H1(children = 'Chosen metric vs life expectancy', style={'textAlign': 'center'}),
    html.P(id='metric-vs-life-test'),
    dbc.Row(
        [
            dbc.Col(metric_vs_life_controls, md=4),
            dbc.Col(dcc.Graph(id='metric-vs-life-graph'), md=8),
        ],
        align="center",
    ),
], fluid=True)

def get_metric_vs_life_callbacks(app):
    @app.callback(
        [
            Output('metric-vs-life-graph', 'figure')
            ,Output('metric-vs-life-test', 'children')
        ],
        [
            Input('metric-vs-life-selection', 'value'),
        ]
    )
    def update_metric_vs_life_graph(metric):
        fig = px.scatter(df, y='Life expectancy', x=metric, hover_data='Country', color='Regional Indicator')
        return fig, f'metric: {metric}'
        # return fig


# ---------------------------------------------------------------------------- #
#           Within region two metric choosable scatter for countries           #
#           within chosen region           #
# ---------------------------------------------------------------------------- #
region_xy_controls = dbc.Card(
    [
        html.Div(
            [
            dbc.Label("Regional Indicator"),
            dcc.Dropdown(
                id='region-region-selection',
                value = 'Western Europe',
                options = list(df['Regional Indicator'].unique())
            )
            ]),
        html.Div(
            [
            dbc.Label("Metric x"),
            dcc.Dropdown(
                id='region-x-selection',
                value = 'Social support',
                options = metric_graph_columns
            )
            ]),
        html.Div(
            [
            dbc.Label("Metric y"),
            dcc.Dropdown(
                id='region-y-selection',
                value = 'Freedom',
                options = metric_graph_columns
            )
            ]),
    ],
    body=True,
)

region_xy_container = dbc.Container([
    html.H1(children = 'Within region two metric choosable scatter for countries within chosen region', style={'textAlign': 'center'}),
    html.P(id='region-xy-test'),
    dbc.Row(
        [
            dbc.Col(region_xy_controls, md=4),
            dbc.Col(dcc.Graph(id='region-xy-graph'), md=8),
        ],
        align="center",
    ),
], fluid=True)

def get_region_xy_callbacks(app):
    @app.callback(
        [
            Output('region-xy-graph', 'figure'),
            Output('region-xy-test', 'children'),
        ],
        [
            Input('region-region-selection', 'value'),
            Input('region-x-selection', 'value'),
            Input('region-y-selection', 'value'),
        ]
    )
    def update_region_xy_graph(region, metric_x, metric_y):
        region_df = df[df['Regional Indicator'] == region]
        fig = px.scatter(region_df, y=metric_y, x=metric_x, hover_data='Country', color='Regional Indicator',
                        trendline = 'ols')
        return fig, f'region df shape: {region_df.shape}'
        # return fig