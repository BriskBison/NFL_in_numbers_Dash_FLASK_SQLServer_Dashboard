import pandas as pd
import statsmodels.api as sm
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output


class Regression:
    def __init__(self, app):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)

        self.df_numeric = self.df.select_dtypes(include=["number"]).dropna()

        self.dependent_vars = ['UNI', 'STX', 'SLP', 'BNG', 'BWG', 'FUT', 'FRL', 'TRD', 'OWN', 'AFF', 'CCH']

        self.teams = self.df['TEAM'].unique()

        self.results = {}
        self._run_regressions()

        self.register_callbacks(app)

    def _run_regressions(self):
        for var in self.dependent_vars:
            y = self.df_numeric[var]
            X = self.df_numeric.drop(columns=self.dependent_vars)
            X = sm.add_constant(X)

            model = sm.OLS(y, X).fit()
            self.results[var] = model

    def update_plot(self, selected_var):
        selected_model = self.results[selected_var]

        self.df_numeric["Fitted Values"] = selected_model.fittedvalues
        self.df_numeric["Residuals"] = selected_model.resid

        self.df_numeric["TEAM"] = self.df['TEAM']

        fig = px.scatter(
            self.df_numeric,
            x="Fitted Values",
            y="Residuals",
            color="TEAM",
            title=f"Residuals plot of the regression model for '{selected_var}'",
            labels={"Fitted Values": "Predicted values", "Residuals": "Residuals"},
            width=1000,
            height=600
        )

        fig.update_layout(
            xaxis=dict(
                title='Predicted values',
                title_font=dict(size=18, family='Arial', color='black', weight='bold'),
                tickfont=dict(size=14, family='Arial', color='black')
            ),
            yaxis=dict(
                title='Residuals',
                title_font=dict(size=18, family='Arial', color='black', weight='bold'),
                tickfont=dict(size=14, family='Arial', color='black')
            )
        )

        return fig

    def get_layout(self):
        return html.Div([
    html.H1("Regression model residuals plot", style={'textAlign': 'center', 'marginBottom': '30px'}),

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='dependent-variable-dropdown',
                options=[{'label': var, 'value': var} for var in self.dependent_vars],
                value='UNI',
                style={'width': '70%', 'margin-left': '20px'}
            ),
            dcc.Graph(
                id='residuals-plot',
                style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px', 'margin-top': '20px'}
            ),
        ], style={'width': '60%', 'padding': '20px'}),

        html.Div([
            dcc.Markdown(self.regression_text, style={'textAlign': 'left', 'color': '#503D36', 'font-size': '21px'})
        ], style={'width': '35%', 'padding': '20px', 'margin-right': '10px', 'margin-top': '-20px'}),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'gap': '20px'}),

], style={'width': '100%', 'margin': '30px'})

    def register_callbacks(self, app):
        @app.callback(
            Output('residuals-plot', 'figure'),
            Input('dependent-variable-dropdown', 'value')
        )
        def update_graph(selected_var):
            return self.update_plot(selected_var)

        self.regression_text = (
            " I started by checking if the values that are assigned to each category in "
            " Table B are well prepared, what is their mean and standard deviation, which has already shown in advance what "
            " categories can be removed. \n\n Then I checked what the correlation is between variables to have "
            " additional look at the variables and find the initial relationships and have information that "
            " variables are not related to each other. Because of this I could already discard some variables that "
            " had little impact on the data or even disturbed its structure. \n\n"
            " Later, by performing PCA analysis on the 'trimmed' data, we made sure that further reduction "
            " is not needed and could destroy the analysis. "
            " Then I divided the entire team table into clusters to get a picture of how the teams group together. "
            " I have confirmed with several methods that this division is the best. \n\n"
            " This allows us to better search for specific results, which I present in the SQL tab. "
            " Because of all these actions we can get the most important graph, "
            " that will allow us to predict the values of category data for specific teams.\n\n"
            " On the left side I set the 'regression model residuals plot', "
            " Each category is assigned to a team, so choosing the appropriate category "
            " the graph will update and the dots assigned to each team will indicate  "
            " the main information I'm looking for: **what are the expected values for a given category.** \n\n"
            " If the points are randomly scattered around line 0, it means that the model fits the data well. "
            " If a pattern appears on the graph (e.g. curvature), it may suggest that the model is not good enough, "
            " to capture the complexity of the data, and it may be worth trying a different model.\n\n"
            " Additionally, you can click on the team in the TEAM column on the right side of the chart,"
            " then the dot corresponding to that team will disappear from the graph.")
