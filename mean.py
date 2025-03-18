import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash


class MeanValuesAnalysis:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)

        self.df_numeric = self.df.select_dtypes(include=["number"])

        self.mean_values = self.df_numeric.mean().reset_index()
        self.mean_values.columns = ["Category", "Mean"]

        self.fig = self.create_mean_values_figure()

        self.mean_text = self.create_mean_text()

    def create_mean_values_figure(self):
        fig = px.line(
            self.mean_values,
            x="Category",
            y="Mean",
            markers=True,
            title="Mean values for each variable in Table A",
            line_shape="spline",
            template="plotly_white"
        )

        fig.update_layout(
            xaxis_title="Variables",
            yaxis_title="Mean values",
            xaxis_title_font=dict(size=16, family='Arial', weight='bold'),
            yaxis_title_font=dict(size=16, family='Arial', weight='bold'),
            yaxis=dict(gridcolor="grey"),
            xaxis=dict(tickangle=-45, gridcolor="grey"),
            font=dict(size=12, color="black"),
            width=800,
            height=530,
            plot_bgcolor="cornsilk",
            paper_bgcolor="cornsilk"
        )

        return fig

    def create_mean_text(self):
        return (
            "Most values oscillate around 50 – Most categories have very similar average values in the range of 49.9 - 50.1.",
            "Clear peak for the NYP category – The average value of this category is noticeably higher than the others. "
            "This may indicate unique features of this category or the presence of anomalies in the data.",
            "As in the case of standard deviation, you can see a decrease for the BEH category – This is the only category that has a significantly lower average than the others. "
            "This may mean that the values of this variable are lower than in other categories.",
            "The remaining variables have stable values  Apart from NYP and BEH, there are no significant deviations from the value of 50.",
            "Let me recall that NYP denotes the distance of the team to New York, and BEH denotes the behavior of the players, "
            "measured based on the number of their 'suspensions' since 2007.",
            "Apart from NYP and BEH, the values are very similar, which means that most variables have a similar impact on the analyzed case."
        )

    def get_layout(self):
        mean_text_component = html.Ul([html.Li(point) for point in self.mean_text])

        return html.Div([

            html.H1("Mean", style={'textAlign': 'center'}),

            html.Div([
                dcc.Graph(
                    id='mean',
                    figure=self.fig,
                    style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px', 'display': 'inline-block',
                           'gap': '170px', 'margin-bottom': '-10px'}
                ),
                html.P(mean_text_component,
                       style={'textAlign': 'left', 'color': '#503D36', 'font-size': '22px',
                              'display': 'inline-block', 'margin-right': '95px', 'margin-top': '-10px'}),
            ], style={'display': 'flex', 'width': '100%', 'justify-content': 'space-between', 'margin': '30px', 'gap': '20px'})

        ])

app = dash.Dash(__name__)
mean_analysis = MeanValuesAnalysis()
app.layout = mean_analysis.get_layout()
