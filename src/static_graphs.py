from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from dataframes import (
    df,
    numeric_cols
)

# ---------------------------------------------------------------------------- #
#                                scatter graphs                                #
# ---------------------------------------------------------------------------- #

physicians_vs_mortality_fig = px.scatter(df, x='Physicians per thousand', y='Infant mortality',
                                          color='Regional Indicator', trendline='ols')
urbanpop_vs_primary_enrollment_fig = px.scatter(df, x='Urban_population', y='Gross primary education enrollment (%)',
                                                color='Regional Indicator', trendline='ols')
urbanpop_vs_tertiary_enrollment_fig = px.scatter(df, x='Urban_population', y='Gross tertiary education enrollment (%)',
                                                color='Regional Indicator', trendline='ols')

forestation_vs_co2_fig = px.scatter(df, x='Forested Area (%)', y='Co2-Emissions', color='Regional Indicator', trendline='ols')
gasoline_vs_co2_fig = px.scatter(df, x='Gasoline Price', y='Co2-Emissions', color='Regional Indicator', trendline='ols')
armed_vs_co2_fig = px.scatter(df, x='Armed Forces size', y='Co2-Emissions', color='Regional Indicator', trendline='ols')
density_vs_co2_fig = px.scatter(df, x='Density (P/Km2)', y='Co2-Emissions', color='Regional Indicator', trendline='ols')

# density_vs_co2_fig = px.scatter(df, x='Density (P/Km2)', y='Co2-Emissions', color='Regional Indicator', trendline='ols')
gdp_vs_businessrank_fig = px.scatter(df, x='Logged GDP per capita', y='Starting a Business rank',
                                      color='Regional Indicator', trendline='ols')

# ========== the same graphs but with bubble size ===========

physicians_vs_mortality_fig_size = px.scatter(df, x='Physicians per thousand', y='Infant mortality', color='Regional Indicator', trendline='ols',
                                             size='Ladder score')
urbanpop_vs_primary_enrollment_fig_size = px.scatter(df, x='Urban_population', y='Gross primary education enrollment (%)',
                                                color='Regional Indicator', trendline='ols', size='Ladder score')
urbanpop_vs_tertiary_enrollment_fig_size = px.scatter(df, x='Urban_population', y='Gross tertiary education enrollment (%)',
                                                color='Regional Indicator', trendline='ols', size='Ladder score')

forestation_vs_co2_fig_size = px.scatter(df, x='Forested Area (%)', y='Co2-Emissions', color='Regional Indicator', trendline='ols',
                                        size='Ladder score')
gasoline_vs_co2_fig_size = px.scatter(df, x='Gasoline Price', y='Co2-Emissions', color='Regional Indicator', trendline='ols', size='Ladder score')
armed_vs_co2_fig_size = px.scatter(df, x='Armed Forces size', y='Co2-Emissions', color='Regional Indicator', trendline='ols', size='Ladder score')
density_vs_co2_fig_size = px.scatter(df, x='Density (P/Km2)', y='Co2-Emissions', color='Regional Indicator', trendline='ols', size='Ladder score')

gdp_vs_businessrank_fig_size = px.scatter(df, x='Logged GDP per capita', y='Starting a Business rank',
                                           color='Regional Indicator', trendline='ols', size='Ladder score')

static_figures = [
    physicians_vs_mortality_fig,
    urbanpop_vs_primary_enrollment_fig,
    urbanpop_vs_tertiary_enrollment_fig,
    forestation_vs_co2_fig,
    gasoline_vs_co2_fig,
    armed_vs_co2_fig,
    density_vs_co2_fig,
    gdp_vs_businessrank_fig
]

static_figures_size = [
    physicians_vs_mortality_fig_size,
    urbanpop_vs_primary_enrollment_fig_size,
    urbanpop_vs_tertiary_enrollment_fig_size,
    forestation_vs_co2_fig_size,
    gasoline_vs_co2_fig_size,
    armed_vs_co2_fig_size,
    density_vs_co2_fig_size,
    gdp_vs_businessrank_fig_size
]

# ---------------------------------------------------------------------------- #
#                          scatter containers                                  #
# ---------------------------------------------------------------------------- #
# ========= no size =========

static_figures_rows = []

len_static = len(static_figures)

for fig_index in range(len_static//2):
    static_figures_row = dbc.Row(
        [
            dbc.Col(dcc.Graph(id=f'static-graph-{fig_index*2}', figure=static_figures[fig_index*2])),
            dbc.Col(dcc.Graph(id=f'static-graph-{fig_index*2 + 1}', figure=static_figures[fig_index*2 + 1])),
        ],
        align="center",
    )
    static_figures_rows.append(static_figures_row)

static_figures_container = dbc.Container([
    html.H1(children = 'Static figures', style={'textAlign': 'center'}),
    # html.P(id='region-xy-test'),
    *static_figures_rows,
], fluid=True)


# ======== with size ========

static_figures_rows_size = []

len_static = len(static_figures_size)

for fig_index in range(len_static//2):
    static_figures_row = dbc.Row(
        [
            dbc.Col(dcc.Graph(id=f'static-graph-{fig_index*2}', figure=static_figures_size[fig_index*2])),
            dbc.Col(dcc.Graph(id=f'static-graph-{fig_index*2 + 1}', figure=static_figures_size[fig_index*2 + 1])),
        ],
        align="center",
    )
    static_figures_rows_size.append(static_figures_row)

static_figures_size_container = dbc.Container([
    html.H1(children = 'Static figures', style={'textAlign': 'center'}),
    # html.P(id='region-xy-test'),
    *static_figures_rows_size,
], fluid=True)


# ---------------------------------------------------------------------------- #
#                                  corr matrix                                 #
# ---------------------------------------------------------------------------- #

corr_except = ['Ladder score lower whisker', 'Ladder score upper whisker', 'Ladder score stanard error']
corr_columns = [col for col in numeric_cols if col not in corr_except]
df_corr = df[numeric_cols].corr()

corr_map = go.Heatmap(x=df_corr.columns, y=df_corr.columns, z=df_corr,
                     colorscale=px.colors.diverging.RdBu)

corr_title = 'Correlation Matrix'

corr_layout = go.Layout(
    title_text=corr_title,  
    width=900, 
    height=900,
    xaxis_showgrid=False,
    yaxis_showgrid=False,
    # yaxis_autorange='reversed'
)
corr_fig=go.Figure(data=[corr_map], layout=corr_layout)

corr_container = dbc.Container([
    html.H1(children = 'Correlation matrix', style={'textAlign': 'center'}),
    dcc.Graph(id='corr-graph-content',
             figure = corr_fig)
], fluid=True)