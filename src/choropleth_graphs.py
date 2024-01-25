from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from dataframes import (
    df, df_with_iso
)

ladder_choropleth = px.choropleth(df_with_iso, locations='Code', color='Ladder score',
             hover_name='Country', color_continuous_scale=px.colors.sequential.Plasma,
             width=800, height=600)

life_choropleth = px.choropleth(df_with_iso, locations='Code', color='Life expectancy',
             hover_name='Country', color_continuous_scale=px.colors.sequential.Plasma,
             width=800, height=600)

gdp_choropleth = px.choropleth(df_with_iso, locations='Code', color='Logged GDP per capita',
             hover_name='Country', color_continuous_scale=px.colors.sequential.Plasma,
             width=800, height=600)

life_bubble_map = px.scatter_geo(df_with_iso, locations='Code', color='Regional Indicator',
                                hover_name='Country', size='Life expectancy',
                                projection='natural earth')