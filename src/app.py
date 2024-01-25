from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

from scatter_graphs import (
    metric_vs_ladder_container, get_metric_vs_ladder_callbacks,
    metric_vs_life_container, get_metric_vs_life_callbacks,
    region_xy_container, get_region_xy_callbacks
)

from static_graphs import (
    static_figures_container,
    static_figures_size_container,
    corr_container
)

from histogram_graphs import (
    metric_hist_container, get_metric_hist_callbacks
)

from spine_graphs import (
    median_vs_ladder_container
)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# ---------------------------------------------------------------------------- #
#                                   callbacks                                  #
# ---------------------------------------------------------------------------- #

get_metric_vs_ladder_callbacks(app)
get_metric_vs_life_callbacks(app)
get_region_xy_callbacks(app)

get_metric_hist_callbacks(app)

# ---------------------------------------------------------------------------- #
#                                  app layout                                  #
# ---------------------------------------------------------------------------- #

app.layout = dbc.Container([
    metric_vs_ladder_container, html.Hr(),
    metric_vs_life_container, html.Hr(),
    region_xy_container, html.Hr(),

    static_figures_container, html.Hr(),
    static_figures_size_container, html.Hr(),
    corr_container, html.Hr(),

    metric_hist_container, html.Hr(),

    median_vs_ladder_container, html.Hr()
], fluid=True)


# ---------------------------------------------------------------------------- #
#                                      run                                     #
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run_server(debug=False)