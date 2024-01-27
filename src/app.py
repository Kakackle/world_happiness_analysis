from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc

from dataframes import (
    ladder_sorted_df, df_with_iso, iso_df, df
)

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

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
# eg. margin-left is 2rem bigger than sidebar width
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links for same page", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="#start", external_link=True),
                dbc.NavLink("metric-vs-ladder-test", href="#metric-vs-ladder-test", external_link=True),
                dbc.NavLink("metric-vs-life-test", href="#metric-vs-life-test",external_link=True),
                dbc.NavLink("region-xy-graph", href="#region-xy-graph",external_link=True),
                dbc.NavLink("static-figures", href="#static-figures",external_link=True),
                dbc.NavLink("corr-graph-content", href="#corr-graph-content",external_link=True),
                dbc.NavLink("hist-metric-graph", href="#hist-metric-graph",external_link=True),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


## table
df_table = dash_table.DataTable(
    df.to_dict('records'),
    columns=[{"name": c, "id": c} for c in df.columns],

    filter_action="native",
    sort_action="native",
    # sort_mode="multi",

    page_action="native",
    page_current= 0,
    page_size= 10,

    # tooltip_data=[
    #     {
    #         column: {'value': str(value), 'type': 'markdown'}
    #         for column, value in row.items()
    #     } for row in df.to_dict('records')
    # ],
    # tooltip_data = [column for column in df.columns],
    # Overflow into ellipsis
    # style_cell={
    #     'overflow': 'hidden',
    #     'textOverflow': 'ellipsis',
    #     'maxWidth': 10,
    # },
    # tooltip_delay=0,
    # tooltip_duration=None,

    style_as_list_view=True,
    style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    },
    style_table={"overflowX": "auto"},
)

md_intro = dcc.Markdown(
'''
    # World happiness index / ladder score, life expectancy and other data

    ## Some simple explaratory charts, looking for some correlations
    (although obiously - correlation =/= causation)

    The columns / metrics include:
    * country - self-exlanatory
    * Ladder score - subjective well-being - The English wording
    of the question is “Please imagine a ladder, with steps numbered from 0 at the
    bottom to 10 at the top. The top of the ladder represents the best possible life
    for you and the bottom of the ladder represents the worst possible life for you.
    On which step of the ladder would you say you personally feel you stand at this
    time
    * Logged GDP per capita - self-explanatory
    * Life expectancy - healthy life expectancy at birth
    * Social support - (or having someone to count on in times of trouble) is the national
    average of the binary responses (either 0 or 1) to the GWP question “If you
    were in trouble, do you have relatives or friends you can count on to help you
    whenever you need them, or not?
    * Freedom to make life choices - average of binary responses
    * Generosity - the residual of regressing national average of response to the GWP
    question “Have you donated money to a charity in the past month?” on GDP
    per capita
    * Perceptions of corruption -  the national average of the survey responses to two questions in the GWP: “Is corruption widespread throughout
    the government or not” and “Is corruption widespread within businesses or
    not?” The overall perception is just the average of the two 0-or-1 responses. In
    case the perception of government corruption is missing, we use the perception
    of business corruption as the overall perception.

    * Density - density (P/Km2): Population density measured in persons per square kilometer
    * Abbreviation - abbreviation or code
    * Agricultural Land (%)- Percentage of land area used for agricultural purposes
    * Land Area - (Km2)
    * Armed Forces Size
    * Birth Rate - Number of births per 1,000 population per year
    * CO2 Emission - Carbon dioxide emissions in tons
    * CPI - Consumer Price Index, a measure of inflation and purchasing power
    * CPI Change (%) - Percentage change in the Consumer Price Index compared to the previous year
    * Fertility Rate - Average number of children born to a woman during her lifetime
    * Forested Area (%) - Percentage of land area covered by forests
    * GDP
    * Gross Primary Education Enrollment (%)
    * Gross Tertiary Education Enrollment (%)
    * Infant Mortality - Number of deaths per 1,000 live births before reaching one year of age
    * Out of Pocket Health Expenditure (%) - Percentage of total health expenditure paid out-of-pocket by individuals
    * Physicians per Thousand
    * Population
    * Labor Force Participation (%)
    * Tax Revenue (%) - Tax revenue as a percentage of GDP
    * Unemployment Rate (%)
    * Urban Population (%)
    * Latitude
    * Longitude

    * Business starting score - These scores are calculated using the simple average of all the indicators’ scores
    * Time - (days) The median number of days needed to get the business up and running for each country/region, split for men and women

    * agriculture - portion of population employed in sectors
    * industry
    * service

    * Political regime - 0 = closed autocracy, 1 = electoral autocracy, 2 = electoral democracy, 3 = liberal democracy

    maybe some table etc...
''')

content = html.Div([
    html.H1(children='World happiness etc analysis', id='start'), html.Hr(),
    md_intro,
    df_table,
    metric_vs_ladder_container, html.Hr(),
    metric_vs_life_container, html.Hr(),
    region_xy_container, html.Hr(),

    static_figures_container, html.Hr(),
    static_figures_size_container, html.Hr(),
    corr_container, html.Hr(),

    metric_hist_container, html.Hr(),

    median_vs_ladder_container, html.Hr()
], id='page-content', style=CONTENT_STYLE)


app.layout = html.Div([sidebar, content])
# ---------------------------------------------------------------------------- #
#                                      run                                     #
# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run_server(debug=True)