import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.graph_objs as go
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class PCAAnalysis:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)
        self.df_numeric = self.df.select_dtypes(include=["number"])

        self.columns = ['UNI', 'STX', 'SLP', 'BNG', 'BWG', 'FUT', 'FRL', 'TRD', 'OWN', 'AFF', 'CCH']

        self.data_dict = {col: self.df_numeric[col].tolist() for col in self.columns if col in self.df_numeric.columns}

        self.scaler = StandardScaler()
        self.df_scaled = self.scaler.fit_transform(self.df_numeric)

        self.pca = PCA(n_components=2)
        self.df_pca = self.pca.fit_transform(self.df_scaled)

        self.df_pca = pd.DataFrame(self.df_pca, columns=['PC1', 'PC2'])

        self.explained_variance = self.pca.explained_variance_ratio_

        self.fig_variance = go.Figure(data=[go.Bar(
            x=[f'PC{i + 1}' for i in range(len(self.explained_variance))],
            y=self.explained_variance,
            marker=dict(color='blue', opacity=0.7)
        )])

        self.fig_variance.update_layout(
            title='Variance explained by individual PCA components',
            xaxis_title='Main Components',
            yaxis_title='Percentage of explained variance',
            height=700,
            plot_bgcolor='cornsilk',
            xaxis=dict(
                title='Main Components',
                title_font=dict(size=20, family='Arial', color='black', weight='bold')
            ),
            yaxis=dict(
                title='Percentage of explained variance',
                title_font=dict(size=20, family='Arial', color='black', weight='bold')
            )
        )

        self.fig_pca = go.Figure(data=go.Scatter(
            x=self.df_pca['PC1'],
            y=self.df_pca['PC2'],
            mode='markers',
            marker=dict(color='blue', size=10, opacity=0.7)
        ))

        self.fig_pca.update_layout(
            title='PCA plot - dimension reduction',
            xaxis_title='Principal Component 1 (PC1)',
            yaxis_title='Principal Component 2 (PC2)',
            plot_bgcolor='cornsilk',
            yaxis=dict(
                showgrid=True,
                gridcolor='grey',
                gridwidth=0.5,
                title='Principal Component 2 (PC2)',
                title_font=dict(size=20, family='Arial', color='black', weight='bold')
            ),
            xaxis=dict(
                showgrid=True,
                gridcolor='grey',
                gridwidth=0.5,
                title='Principal Component 1 (PC1)',
                title_font=dict(size=20, family='Arial', color='black', weight='bold')
            )
        )

        self.pca_combined_text = (
            " The results of the mean, standard deviation and correlation matrix allowed us to indicate, "
            " which variables are worth further analysis. The removed variables are: 'BMK', 'SMK', 'BEH', 'NYP', 'PLA'.\n\n"
            " For this purpose, I created a PCA model using the following variables: "
            "'UNI', 'STX', 'SLP', 'BNG', 'BWG', 'FUT', 'FRL', 'TRD', 'OWN', 'AFF', 'CCH'. "
            "The results are shown on the left.\n\n"
            "#### PCA Results:\n\n"
            "PC1: 36.31%\n\n"
            "PC2: 15.90%\n\n"
            "PC3: 11.21%\n\n"
            "PC4: 10.11%\n\n"
            "PC5: 7.34%\n\n"
            "PC6: 4.90%\n\n"
            "PC7: 4.41%\n\n"
            "PC8: 3.48%\n\n"
            "PC9: 1.91%\n\n"
            "PC10: 1.29%\n\n"
            "**Sum of variance explained by PC1 and PC2: 52.21%**\n\n"
            "The distribution of scores suggests that the first component (PC1) explains a significant part of the variability in the data. "
            "PC1 explains 36.31%, a PC2 15.90% variance, which gives a total of 52.21%. "
            "Other components (PC3–PC10) are having less and less impact, suggesting that further reduction "
            "may result in the loss of important information.\n\n"
            "Top chart (scatter plot PCA) shows that the distribution of points along PC1 suggests, "
            "that the main variability in the data comes from this component. "
            "PC2 adds some additional information, but it is less important than PC1.\n\n"
            "Because of this, I finally reduced the list of features to only those that actually matter."
            "If even PC3 + PC4 add little, it means that the data is difficult to reduce to a small number of dimensions."
            "Therefore, further reduction would be detrimental to the quality of the analysis."
            "This is a very important step, it will make future analyses easier and faster.\n\n"
            "**Final list of features to analyze:**\n"
            "'UNI', 'STX', 'SLP', 'BNG', 'BWG', 'FUT', 'FRL', 'TRD', 'OWN', 'AFF', 'CCH'."
        )

    def get_layout(self):
        return html.Div([

            html.Div([
                html.H1("Principal Component Analysis", style={'textAlign': 'center', 'marginBottom': '30px'}),

                html.Div([
                    dcc.Graph(id='pca', figure=self.fig_pca)
                ], style={'display': 'inline-block', 'flex-direction': 'column', 'align-items': 'left',
                          'width': '100%'}),

                html.Div([
                    dcc.Graph(id='variance', figure=self.fig_variance)
                ], style={'display': 'inline-block', 'flex-direction': 'column', 'align-items': 'left',
                          'width': '100%'})
            ], style={'display': 'inline-block', 'flex-direction': 'column', 'align-items': 'left', 'width': '60%',
                      'gap': '170px'}),

            dcc.Markdown(self.pca_combined_text, style={
                'textAlign': 'left',
                'color': '#503D36',
                'font-size': '20px',
                'display': 'inline-block',
                'margin-right': '95px',
                'margin-top': '-15px',
                'width': '50%'
            }),

        ], style={'display': 'flex', 'width': '100%', 'justify-content': 'space-between', 'margin': '30px',
                  'gap': '20px'})

app = dash.Dash(__name__)
pca_analysis = PCAAnalysis()
app.layout = pca_analysis.get_layout()
