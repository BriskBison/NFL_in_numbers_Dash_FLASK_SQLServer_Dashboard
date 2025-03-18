from statistics import correlation

import pandas as pd
from dash import dcc, html
import plotly.graph_objects as go
import dash

class CorrelationMatrixAnalysis:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)
        self.df_numeric = self.df.select_dtypes(include=["number"]).dropna()
        self.df_numeric = self.df_numeric.loc[:, self.df_numeric.std() > 0]


        self.corr_matrix = self.df_numeric.corr()
        self.fig = self.create_correlation_matrix_figure()

        self.correlation_text = self.create_correlation_text()

        self.vif_text = self.vif_text()

    def create_correlation_matrix_figure(self):
        fig = go.Figure(data=go.Heatmap(
            z=self.corr_matrix.values,
            x=self.corr_matrix.columns,
            y=self.corr_matrix.columns,
            colorscale='Plasma',
            zmin=-1,
            zmax=1,
            colorbar=dict(title="Correlation", ticks="outside", tickvals=[-1, 0, 1], ticktext=["-1", "0", "1"]),
            text=self.corr_matrix.values,
            texttemplate="%{text:.2f}",
            showscale=True
        ))

        fig.update_layout(
            title="Variable Correlation Matrix",
            title_font=dict(size=20, family="Arial", color='black', weight="bold"),
            xaxis_title="Variables",
            yaxis_title="Variables",
            xaxis=dict(
                tickangle=45,
                title_font=dict(size=16, family="Arial", color="black", weight="bold"),
                tickfont=dict(size=14, color="black")
            ),
            yaxis=dict(
                tickangle=0,
                title_font=dict(size=16, family="Arial", color="black", weight="bold"),
                tickfont=dict(size=14, color="black")
            ),
            plot_bgcolor="black",
            paper_bgcolor="cornsilk",
            template="plotly_dark",
            margin=dict(l=40, r=40, t=40, b=40),
            width=800,
            height=530,
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            xaxis_tickangle=-45,
            font=dict(color="black")
        )

        return fig

    def create_correlation_text(self):
        return [
            "BMK and SMK have a perfect negative correlation (-1.00), which means that these variables are strongly negatively correlated, suggesting that an increase in one leads to a decrease in the other.",
            "OWN and PLA have a high positive correlation (0.85-0.92), indicating that these variables may be very similar.",
            "FRL and PLA also show a strong correlation (0.85), suggesting a strong relationship between these variables.",
            "Variables such as NYP, SLP, and BEH have weak correlations with most other variables, suggesting they are not strongly related to each other.",
            "BMK and SMK are exactly opposite, so one of these variables may be redundant in the model.",
            "OWN, PLA, and FRL are strongly correlated, which may indicate some redundancy in the data.",
            "TRD shows a medium positive correlation with UNI (0.66), which may suggest some relationship between these variables.",
            "BWG has a negative correlation with several variables, such as PLA (-0.58) and FRL (-0.40), indicating possible negative relationships."
        ]

    def vif_text(self):
        return [
            "The 'BMK' and 'SMK' variable have a VIF of 'inf', which suggests that they are highly correlated with other variables in the model, indicating a potential multicollinearity issue.",
            "The 'UNI' variable has a VIF of 4.68, indicating a moderate correlation with other variables.",
            "The 'CCH' variable has a VIF of 6.89, which also suggests a moderate correlation with other variables.",
            "The 'STX' variable has a VIF of 7.51, indicating a higher correlation with other variables.",
            "The 'AFF' variable has a VIF of 4.86, suggesting a moderate dependence on other variables.",
            "The 'SLP' variable has a VIF of 1.66, indicating a low correlation with other variables.",
            "The 'NYP' variable has a VIF of 1.55, suggesting that it is relatively independent from other variables.",
            "The 'FRL' variable has a VIF of 13.05, suggesting that it may be highly correlated with other variables in the model.",
            "The 'BNG' variable has a VIF of 4.55, indicating a moderate correlation with other variables.",
            "The 'TRD' variable has a VIF of 3.03, suggesting a moderate relationship with other variables.",
            "The 'BWG' variable has a VIF of 3.64, indicating a moderate correlation with other variables.",
            "The 'FUT' variable has a VIF of 3.33, which also suggests a moderate correlation with other variables.",
            "The 'PLA' variable has a VIF of 21.57, indicating a very high correlation with other variables, which may point to a multicollinearity problem.",
            "The 'OWN' variable has a VIF of 6.30, suggesting a moderate correlation with other variables.",
            "The 'BEH' variable has a VIF of 1.82, indicating a low correlation with other variables."
        ]

    def get_layout(self):
        correlation_text_component = html.Ul([html.Li(point) for point in self.correlation_text])
        vif_text_component = html.Ul([html.Li(point) for point in self.vif_text])

        return html.Div([

            html.H1("Variable Correlation Matrix", style={'textAlign': 'center'}),

            html.Div([
                dcc.Graph(
                    id='correlation-heatmap',
                    figure=self.fig,
                    style={'textAlign': 'left', 'color': '#503D36', 'font-size': '18px', 'display': 'inline-block', 'gap': '170px'}
                ),
                html.P(correlation_text_component,
                       style={'textAlign': 'left', 'color': '#503D36', 'font-size': '22px',
                              'display': 'inline-block', 'margin-right': '95px', 'margin-top': '-10px'}),
            ], style={'display': 'flex', 'width': '100%', 'justify-content': 'space-between', 'margin': '30px', 'gap': '20px'}),

            html.P("VIF coefficient for each variable",
                   style={'textAlign': 'left', 'color': '#503D36', 'font-size': '24px', 'margin-bottom': '-10px',
                          'fontWeight': 'bold', 'margin-left': '95px'}),

            html.Div([
                html.P(vif_text_component,
                       style={'textAlign': 'left', 'color': '#503D36', 'font-size': '22px',
                              'margin-right': '95px', 'margin-top': '-10px', 'width': '50%'}),
                html.Img(src='/assets/VIF.png', style={'width': '50%', 'height': 'auto', 'margin-right': '95px'}),
            ], style={'display': 'flex', 'width': '100%', 'justify-content': 'space-between', 'margin': '30px', 'gap': '20px'}),
        ])

app = dash.Dash(__name__)
correlation_analysis = CorrelationMatrixAnalysis()
app.layout = correlation_analysis.get_layout()

