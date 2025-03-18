import pandas as pd
import scipy.cluster.hierarchy as sch
import plotly.graph_objects as go
from dash import dcc, html
from scipy.cluster.hierarchy import fcluster
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import dash


class ClusteringAnalysis:
    def __init__(self, num_clusters=2):
        self.url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/team-picking-categories.csv"
        self.df = pd.read_csv(self.url)
        self.df_numeric = self.df.select_dtypes(include=["number"]).dropna()
        self.scaler = StandardScaler()
        self.df_scaled = self.scaler.fit_transform(self.df_numeric)

        self.Z = sch.linkage(self.df_scaled, method='ward')
        self.num_clusters = num_clusters
        self.df["Cluster"] = self.get_clusters()


        self.scatter_fig = self.create_cluster_plot()
        self.silhouette_fig = self.create_silhouette_plot()
        self.quality_fig = self.create_quality_plot()

        self.clustering_text = self.create_clustering_text()

    def get_clusters(self):
        return fcluster(self.Z, self.num_clusters, criterion='maxclust')

    def create_cluster_plot(self):
        fig = go.Figure()
        cluster_colors = ['red', 'green', 'blue', 'purple', 'orange']

        for i in range(1, self.num_clusters + 1):
            cluster_data = self.df[self.df["Cluster"] == i]
            fig.add_trace(go.Scatter(
                x=cluster_data.index,
                y=cluster_data["Cluster"],
                mode='markers',
                marker=dict(color=cluster_colors[i - 1], size=10),
                name=f'Cluster {i}'
            ))

        fig.update_layout(title="Scatter Plot of Clusters")
        return fig

    def create_silhouette_plot(self):
        k_range = range(2, 10)
        silhouette_scores = []

        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(self.df_scaled)
            silhouette_scores.append(silhouette_score(self.df_scaled, labels))

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(k_range),
            y=silhouette_scores,
            mode='lines+markers',
            marker=dict(color='blue', size=8),
            line=dict(dash='dash')
        ))
        fig.update_layout(title="Silhouette Score for Different k")
        return fig

    def create_quality_plot(self):
        k_range = range(2, 10)
        ch_scores = []
        db_scores = []

        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(self.df_scaled)
            ch_scores.append(calinski_harabasz_score(self.df_scaled, labels))
            db_scores.append(davies_bouldin_score(self.df_scaled, labels))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(k_range), y=ch_scores, mode='lines+markers', name='Calinski-Harabasz'))
        fig.add_trace(go.Scatter(x=list(k_range), y=db_scores, mode='lines+markers', name='Davies-Bouldin', line=dict(color='red')))
        fig.update_layout(title="Clustering Quality Indicators")
        return fig

    def create_clustering_text(self):
        return (" Division into clusters is another important element of proper analysis.\n"
                " Because of the appropriate model, I made a selection into two clusters, which will make it easier\n"
                " finding differences between individual teams, finding relationships\n"
                " and above all, it will further strengthen our belief that which variables are\n"
                " most important in predicting outcomes.\n\n"

                " The silhouette method I used suggests dividing it into two clusters, similar information"
                " gives the elbow method.\n\n"

                " The red cluster (1) contains the most points, which means that many observations had similar characteristics.\n\n"
                " The green cluster (2) has fewer points, suggesting they are more unique in the dataset.\n\n"

                " **Teams in cluster 1:** Green Bay Packers, Pittsburgh Steelers, Kansas City Chiefs, New England Patriots, "
                " Buffalo Bills, Carolina Panthers, Seattle Seahawks, Indianapolis Colts, Arizona Cardinals, Houston Texans, "
                " Philadelphia Eagles, Detroit Lions\n\n"

                " **Teams in cluster 2:** Baltimore Ravens, New Orleans Saints, Denver Broncons, Minnesota Vikings, "
                " New York Giants, Atlanta Falcons, Dallas Cowboys, Jacksonville Jaguars, Miami Dolphins, "
                " Cincinnati Bengals, Oakland Raiders, Tampa Bay Buccaneers, Los Angeles Rams, Chicago Bears, Cleveland Browns, "
                "San Diego Chargers, San Francisco 49ers, New York Jets, Washington Redskins, Tennessee Titans\n\n"

                " I will use this data in the SQL tab where using the database, \n"
                " I try to find relationships between teams.\n\n"

                " The high Calinski-Barabasz index and the low Davies-Bouldin index confirm "
                " that this number of clusters is appropriate.")

    def get_layout(self):
        return html.Div([
            html.Div([
                html.H1("Scatter plot", style={'textAlign': 'center'}),
                dcc.Graph(
                    id='scatter-plot',
                    figure=self.scatter_fig,
                    style={'margin-top': '-20px', 'margin-right': '95px'}
                )
            ], style={'width': '100%', 'margin-bottom': '30px'}),

            html.Div([
                html.Div([
                    dcc.Graph(id='clusters', figure=self.silhouette_fig),
                    dcc.Graph(id='quality', figure=self.quality_fig)
                ], style={'display': 'flex', 'flex-direction': 'column', 'width': '60%', 'gap': '30px'}),

                html.Div([
                    dcc.Markdown(self.clustering_text,
                                 style={'textAlign': 'left', 'color': '#503D36', 'font-size': '20px', 'margin-right': '95px'}
                                 )
                ], style={'width': '35%', 'padding-left': '30px'})
            ], style={'display': 'flex', 'justify-content': 'space-between', 'width': '100%'})
        ], style={'width': '100%', 'padding': '20px'})


app = dash.Dash(__name__)
clustering = ClusteringAnalysis()
app.layout = clustering.get_layout()

