from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from dataframes import df

overall_fig = px.scatter(df, y='Life expectancy', x='Agriculture', hover_data='Country', color='Regional Indicator',
                        trendline='ols', trendline_scope='overall')
overall_fig.show()