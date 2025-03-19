import dash
import pandas as pd
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import SQL_queries
from legend_text import Legend
from winners_table import Winners
import standard_dev
import mean
import pca
import clustering
import regression
import correlation


app = dash.Dash(__name__, suppress_callback_exceptions=True)

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
df = pd.read_csv(url)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),

    html.Div([
        dcc.Link("Main", href="/"),
        " | ",
        dcc.Link("Winners", href="/winners"),
        " | ",
        dcc.Link("Standard Deviation", href="/standard-deviation"),
        " | ",
        dcc.Link("Mean", href="/mean"),
        " | ",
        dcc.Link("Correlation", href="/correlation"),
        " | ",
        dcc.Link("PCA", href="/pca"),
        " | ",
        dcc.Link("Clustering", href="/clustering"),
        " | ",
        dcc.Link("Regression", href="/regression"),
        " | ",
        dcc.Link("SQL", href="/sql"),
        " | ",
        dcc.Link("Results", href="/results"),
        " | ",
    ], style={"textAlign": "center", "padding": "10px", "fontSize": "20px"}),

    html.Div(id="page-content")
])

@app.callback(
    Output('residuals-plot', 'figure'),
    Input('dependent-variable-dropdown', 'value')
)

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/":
        return html.Div([
    html.H1("NFL in numbers", style={'textAlign': 'center', 'color': '#503D36', 'font-size': '28px'}),
    html.H2("by Karol Bohdan Krawczyk", style={'textAlign': 'center', 'color': '#503D36', 'font-size': '12px', 'font-family': 'Verdana'}),

    dcc.Markdown(
        "Welcome to my app. Its purpose is to examine the value of NFL teams in great detail. "
        "Table A contains the names of the teams on the left side, while on the right side are the points awarded for each category. "
        "The names of the categories are listed on the top bar of Table A. \n\n"
        "On the right is Table B, which explains what the points are awarded for in each category. "
        "For example, the PLA category - determines the effort of the players on the field, their motivation, commitment, teamwork, etc. "
        "The CCH category - determines how good the coach of a given team is, based on his history, opinions, experience, etc.\n\n"
        "Above are the tabs related to typical data analysis. "
        "Their purpose is to check what the values from Table A have to do with the results, whether there are any relationships between them, "
        "and whether it is possible to predict future events.\n\n"
        "The whole process is arranged in order, so I encourage you to browse the tabs from left to right, "
        "then the whole analysis process will be clearest. Additionally, the 'Winners' tab contains data on the Superbowl since 1967.\n\n",
        style={'margin': '20px 30px', 'font-size': '20px'}
    ),

    html.Div([
        html.Div([
            html.H3("Table A - Team scores in each category", style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px',
                                                                     'margin-bottom': '10px'}),
            dash_table.DataTable(
                id='table',
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records'),
                style_table={'overflowX': 'auto', 'width': '100%', 'height': '400px'},
                style_data={'whiteSpace': 'normal', 'height': 'auto', 'backgroundColor': 'darkcyan', 'color': 'white'},
                style_data_conditional=[{'if': {'column_id': 'TEAM'},
                                         'backgroundColor': 'cornsilk', 'color': 'black', 'fontWeight': 'bold'}],
                style_header={'backgroundColor': 'navy', 'color': 'white', 'fontWeight': 'bold', 'font-size': '15px'},
                style_cell={'textAlign': 'left', 'minWidth': '30px', 'width': 'auto', 'maxWidth': '300px'},
                fixed_rows={'headers': True}
            )
        ], style={'width': '50%'}),

        html.Div([
            html.H3("Table B - Criteria for awarding points", style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px',
                                                                     'margin-bottom': '10px'}),
            dash_table.DataTable(
                id='table2',
                columns=[{'name': col, 'id': col} for col in Legend.df_legend_table.columns],
                data=Legend.df_legend_table.to_dict('records'),
                style_table={'overflowX': 'auto', 'width': '100%', 'height': '400px'},
                style_data={'whiteSpace': 'normal', 'height': 'auto', 'backgroundColor': 'lightslategrey', 'color': 'white'},
                style_data_conditional=[{'if': {'column_id': ' abbrev '},
                                         'backgroundColor': 'cornsilk', 'color': 'black', 'fontweight': 'bold'}],
                style_header={'backgroundColor': 'darkblue', 'color': 'white', 'fontWeight': 'bold', 'font-size': '15px'},
                style_cell={'textAlign': 'left'},
                style_cell_conditional=[{'if': {'column_id': 'abbrev'}, 'minWidth': '60px'}],
                fixed_rows={'headers': True}
            )
        ], style={'width': '45%'})
    ], style={'display': 'flex', 'justify-content': 'flex-start', 'gap': '20px', 'width': '100%', 'margin': '10px', 'margin-left': '30px'})
])

    elif pathname == "/winners":
        return html.Div([
            html.H1("Super Bowl Champions", style={'textAlign': 'center'}),
            html.P("This is a list of Super Bowl championships since 1967.",
            style={'color': '#503D36', 'font-size': '20px', 'font-family': 'Verdana'}),
            dash_table.DataTable(
                id='superbowl-table',
                columns=[{'name': col, 'id': col} for col in Winners.df.columns if col != 'Ref.' and col != 'Venue' and col != 'City'],
                data=Winners.df.to_dict('records'),
                style_table={'overflowX': 'auto', 'width': '100%', 'height': '900px'},
                style_data={'whiteSpace': 'normal', 'height': 'auto', 'backgroundColor': 'cornsilk', 'color': 'black', 'font-size': '14px'},
                style_header={'backgroundColor': 'navy', 'color': 'white', 'fontWeight': 'bold', 'font-size': '18px'},
                style_cell={
                    'textAlign': 'left',
                    'minWidth': '150px',
                    'width': 'auto',
                    'maxWidth': '300px',
                },
                fixed_rows={'headers': True}
            ),
        ])

    elif pathname == "/standard-deviation":
        return standard_dev.StandardDeviationAnalysis().get_layout()

    elif pathname == "/mean":
        return mean.MeanValuesAnalysis().get_layout()

    elif pathname == "/correlation":
        return correlation.CorrelationMatrixAnalysis().get_layout()

    elif pathname == "/pca":
        return pca.PCAAnalysis().get_layout()

    elif pathname == "/clustering":
        return clustering.ClusteringAnalysis().get_layout()

    elif pathname == "/regression":
        return regression.Regression(app).get_layout()

    elif pathname == "/sql":
        return SQL_queries.SQLqueries().get_layout()

    elif pathname == "/results":
        return html.Div([
        html.H1("Summary", style={'textAlign': 'center'}),
            dcc.Markdown("Thank you very much for reviewing my application, I hope that the process of analyzing "
                        " data for the NFL was understandable and pleasant for you. Below I will present the most important. "
                        " information from the entire analysis. \n\n"
                        " **The most important features for estimating a team's future wins are:** CCH, FUT, TRD, FRL and BNG. "
                        " The key is that all of these values are high, and not that they are selectively at the maximum value."
                        " It is better for a team to have 80 points in 5 of these characteristics than 100 points in two and 60 points "
                        " in the remaining ones.\n\n"
                        " If a team does not have many points in other categories, the more points they will have"
                        " BNG value and lower AFF, aiming at 100 points, the better. \n\n"
                        " **Categories such as** 'BMK', 'SMK', 'BEH', 'NYP', 'PLA' they don't have a major impact on winnings"
                        " there is no need to put significant effort into analyzing them. \n\n"
                        " The division of the team into clusters did not return a clear result in the form of only winning teams "
                        " or very weak teams, these are teams of different categories, but the best ones"
                        " have the features listed above, it doesn't matter which cluster they are in.\n\n "
                        " The data in Table A describing the points awarded to individual teams is well awarded, "
                        " Apart from the BEH and NYP categories, I did not detect any anomalies, disturbed relationships, "
                        " or significantly higher standard deviations or mean values.. \n\n"
                        " **Using the residuals of the regression model, we can try to predict the future values of the teams with great accuracy**. \n\n"
                        " Total points scored by teams in each category **has no significance in predicting winnings**, "
                        " what matters is what values the points are awarded for "
                        " a team and how they are distributed relative to other relevant categories.\n\n"
                        " I wish you all the best, best regards, Karol Bohdan Krawczyk")
        ], style={'width': '100%', 'textAlign': 'center',  'fontSize': '23px', 'marginLeft': 'auto',  'marginRight': 'auto',  'padding': '5px' })

if __name__ == '__main__':
    app.run(debug=True)

