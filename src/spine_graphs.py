from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from dataframes import (
    df
)

spine_columns = ['Social support', 'Life expectancy', 'Freedom', 'Urban_population']

social_median = df['Social support'].median()
life_median = df['Life expectancy'].median()
freedom_median = df['Freedom'].median()
urban_median = df['Urban_population'].median()

medians = [social_median, life_median, freedom_median, urban_median]
median_columns = [f'{col} above median' for col in spine_columns]

for col_index, col in enumerate(median_columns):
    df[col] = df.apply(
    lambda row: True if row[spine_columns[col_index]] > medians[col_index] else False,
    axis = 1
    )

median_col_True_means = []
for col in median_columns:
    median_mean = df[df[col] == True]['Ladder score'].mean()
    median_col_True_means.append(median_mean)

median_col_False_means = []
for col in median_columns:
    median_mean = df[df[col] == False]['Ladder score'].mean()
    median_col_False_means.append(median_mean)

# reverse values for spine visualization
median_col_False_means = [col * -1 for col in median_col_False_means]

# ---------------------------------------------------------------------------- #
#                 Spine graphs by spreads / relation to median                 #
# ---------------------------------------------------------------------------- #
ladder_vs_medians_fig = go.Figure(
    data = [
        go.Bar(name = 'above median',
               y = spine_columns,
               x = median_col_True_means,
               orientation='h',
                marker=dict(color='#DD5555',
                line=dict(
                color='rgba(0,0,0,1.0)', width=0.5)),
                hoverinfo='none'
              ),
        go.Bar(name = 'below median',
               y = spine_columns,
               x = median_col_False_means,
               orientation='h',
                marker=dict(color='#5555DD',
                line=dict(
                color='rgba(0,0,0,1.0)', width=0.5)),
                hoverinfo='none'
              ),
    ],
)
ladder_vs_medians_fig.update_layout(barmode='relative')

# reverse again for vertical bar visualization
median_col_False_means = [col * -1 for col in median_col_False_means]

median_vs_ladder_vertical_fig = go.Figure(
    data = [
        go.Bar(name = 'above median', x = spine_columns, y = median_col_True_means),
        go.Bar(name = 'below median', x = spine_columns, y = median_col_False_means),
    ],
)
median_vs_ladder_vertical_fig.update_layout(barmode='group',
                                           yaxis_title="Ladder score",
                                           xaxis_title="Metric")

median_vs_ladder_container = dbc.Container([
    html.H1(children = 'Spine graphs by spreads', style={'textAlign': 'center'}),
    dcc.Graph(id='median-vs-ladder-graph-content',
             figure = median_vs_ladder_vertical_fig)
], fluid=True)