from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from dataframes import (
    df,
    metric_graph_columns
)

# ---------------------------------------------------------------------------- #
#                            Histogram multi-figure                            #
# ---------------------------------------------------------------------------- #
metric_hist_controls = dbc.Card(
    [
        html.Div(
            [
            dbc.Label("Metric"),
            dcc.Dropdown(
                id='hist-metric-selection',
                value = 'Social support',
                options = [col for col in metric_graph_columns if col != 'Ladder score']
            )
            ]),
    ],
    body=True,
)

metric_hist_container = dbc.Container([
    html.H1(children = 'Metric histogram', style={'textAlign': 'center'}),
    html.P(id='hist-metric-test'),
    dbc.Row(
        [
            dbc.Col(metric_hist_controls, md=4),
            dbc.Col(dcc.Graph(id='hist-metric-graph'), md=8),
        ],
        align="center",
    ),
], fluid=True)

def get_metric_hist_callbacks(app):
    @app.callback(
        [
            Output('hist-metric-graph', 'figure'),
            Output('hist-metric-test', 'children')
        ],
        [
            Input('hist-metric-selection', 'value'),
        ]
    )
    def update_hist_metric_graph(metric):
        # fig = px.scatter(df, y='Ladder score', x=metric, hover_data='Country', color='Regional Indicator',)
        fig = px.histogram(df, x=metric, color='Regional Indicator')
        return fig, f'metric: {metric}'
        # return fig
    

# ---------------------------------------------------------------------------- #
#                              Other hist / donuts                             #
# ---------------------------------------------------------------------------- #
forest_vs_agriculture_hist_fig = go.Figure()

forest_vs_agriculture_hist_fig.add_trace(
    # px.histogram(df, x='Forested Area (%)', nbins=10).data[0]
    go.Histogram(x=df['Forested Area (%)'], nbinsx = 10, name='Forested Area (%)')
)
forest_vs_agriculture_hist_fig.add_trace(
    # px.histogram(df, x='Agriculture', nbins=10).data[0]
    go.Histogram(x=df['Agriculture']*100, nbinsx = 10, name='Agriculture')
)

forest_vs_agriculture_hist_fig.update_layout(barmode='overlay')
forest_vs_agriculture_hist_fig.update_traces(opacity=0.75)


forest_vs_industry_hist_fig = go.Figure()
forest_vs_industry_hist_fig.add_trace(
    # px.histogram(df, x='Forested Area (%)', nbins=10).data[0]
    go.Histogram(x=df['Forested Area (%)'], nbinsx = 10, name='Forested Area (%)')
)
forest_vs_industry_hist_fig.add_trace(
    # px.histogram(df, x='Agriculture', nbins=10).data[0]
    go.Histogram(x=df['Industry']*100, nbinsx = 10, name='Industry')
)

forest_vs_industry_hist_fig.update_layout(barmode='overlay')
forest_vs_industry_hist_fig.update_traces(opacity=0.75)

hist_with_boxes = px.histogram(df, x='Ladder score', color='Regional Indicator',
             marginal='violin', height=800)