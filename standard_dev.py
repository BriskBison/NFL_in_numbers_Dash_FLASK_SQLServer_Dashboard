import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
import dash

class StandardDeviationAnalysis:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)
        self.df_numeric = self.df.select_dtypes(include=["number"])
        self.std_dev = self.df_numeric.std()
        self.fig = self.create_std_dev_figure()
        self.stand_dev_text = self.create_stand_dev_text()

    def create_std_dev_figure(self):
        fig = go.Figure(data=[go.Bar(
            x=self.std_dev.index,
            y=self.std_dev.values,
            marker=dict(color='rgb(158,202,225)', line=dict(color='rgb(8,48,107)', width=1.5))
        )])

        fig.update_layout(
            title="Standard deviation for each variable in Table A",
            xaxis_title="Variables",
            yaxis_title="Standard deviation",
            xaxis_title_font=dict(size=16, family='Arial', weight='bold'),
            yaxis_title_font=dict(size=16, family='Arial', weight='bold'),
            template="plotly_dark",
            yaxis=dict(range=[30, self.std_dev.max() + 1]),
            margin=dict(l=40, r=40, t=40, b=40),
            width=800,
            height=530,
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            xaxis_tickangle=-45,
            plot_bgcolor="cornsilk",
            paper_bgcolor="cornsilk",
            font=dict(color="black")
        )

        return fig

    def create_stand_dev_text(self):
        return [
            "The NYP variable has the largest standard deviation. This means that the values of this variable "
            "are the most dispersed around the mean.",
            "The BEH variable has the smallest standard deviation, which suggests that the values of this variable are more stable.",
            "The other variables have relatively similar values of the standard deviation (around 30.2-30.4).",
            "The NYP variable may require additional analysis because its values are the most variable.",
            "The BEH variable is the least variable, suggesting stability.",
            "It is worth checking what importance these variables have in the model and whether the high variability "
            "is a problem or a natural feature of the data.",
            "In the following pages - 'Mean' , 'Correlation' we will try to look more closely at the variables to find additional clues for the full analysis."
        ]

    def get_layout(self):
        stand_dev_text_component = html.Ul([html.Li(point) for point in self.stand_dev_text])

        return html.Div([

            html.H1("Standard Deviation", style={'textAlign': 'center'}),

            html.Div([
                dcc.Graph(
                    id='standard-dev',
                    figure=self.fig,
                    style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px', 'display': 'inline-block',
                           'gap': '170px', 'margin-bottom': '-10px'}
                ),
                html.P(stand_dev_text_component,
                       style={'textAlign': 'left', 'color': '#503D36', 'font-size': '22px',
                              'display': 'inline-block', 'margin-right': '95px', 'margin-top': '-10px'}),
            ], style={'display': 'flex', 'width': '100%', 'justify-content': 'space-between', 'margin': '30px', 'gap': '20px'})

        ])

app = dash.Dash(__name__)
dev_analysis = StandardDeviationAnalysis()
app.layout = dev_analysis.get_layout()
