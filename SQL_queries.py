from dash import html
from dash import dcc
import dash


class SQLqueries():
    def get_layout(self):
        return html.Div([
    dcc.Tabs([
        dcc.Tab(label='Database and TOP 10', children=[
            html.Div([
                html.Div([
                    dcc.Markdown("In this tab I will present queries executed in SQL Server, which will allow even more "
                           "verify which variables are most important.\n\n"
                           " At the beginning we can check if the teams with the most wins are in greater numbers in cluster 1 or cluster 2. \n\n "
                           " **Cluster 1** = Green Bay Packers, Pittsburgh Steelers, Kansas City Chiefs, New England Patriots, Buffalo Bills, "
                           "Carolina Panthers, Seattle Seahawks, Indianapolis Colts, Arizona Cardinals, "
                           "Houston Texans, Philadelphia Eagles, Detroit Lions\n\n"
                           " **Cluster 2** = Baltimore Ravens, New Orleans Saints, Denver Broncons, Minnesota Vikings, "
                           "New York Giants, Atlanta Falcons, Dallas Cowboys, Jacksonville Jaguars, Miami Dolphins, "
                           "Cincinnati Bengals, Oakland Raiders, Tampa Bay Buccaneers, Los Angeles Rams, Chicago Bears, Cleveland Browns, "
                           "San Diego Chargers, San Francisco 49ers, New York Jets, Washington Redskins, Tennessee Titans\n\n"
                           " As you can see, the TOP 10 teams are almost evenly distributed across two clusters, which is"
                           " very good information because it shows that there is no error in the data and it is additional"
                           " confirmation of the actions taken in the previous stages.\n\n"
                           "In the second photo I present the reliability and truthfulness of the database. \n\n")
                ], style={'width': '50%', 'textAlign': 'left','font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query1(Top_Winners).png',
                             style={'width': '100%', 'height': 'auto', 'margin-bottom': '20px'}),
                    html.Img(src='/assets/Query0(Showing_database).png',
                             style={'width': '100%', 'height': 'auto'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ]),
        dcc.Tab(label='SUM of points and AVG(subqueries)', children=[
            html.Div([
                html.Div([
                    dcc.Markdown(
                        "In this tab we can see very important data. Is presented the total of "
                        "all points from all categories that the team obtained and the average value of points "
                        "which the teams will obtain.\n\n"
                        "As a result of the search, I marked the teams that achieved the most in blue "
                        "victories presented in the previous tab. We can see that "
                        "in fact the first 3 teams have the most points and also "
                        "these teams have a lot of Superbowl wins, so only in 15th place"
                        "we see the 'New York Giants' and right below them the 'Denver Broncos', the teams, "
                        "which can also boast of many winnings.\n\n"
                        "So what's most important is how many teams that haven't achieved much "
                        "Superbowl victories, they also have a large number of points. "
                        "These are basically all teams from 7 to 14 excluding 'Philadelphia Eagles', "
                        "who got two wins. \n\n"
                        "This information tells us first of all that the sum of points may actually indicate that "
                        "how good a team is, however, it absolutely cannot be the only indicator.\n\n"
                        "It is important in which categories the teams have the most points, "
                        "which was also confirmed by the previous mathematical calculations that were made on the previous pages of this application.\n\n"
                        "In the following pages of this page, I will try to find the answer to what these categories are.")
                ], style={'width': '50%', 'textAlign': 'left', 'font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query2(Sum_and_avg).png',
                             style={'width': '100%', 'height': '110%'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ]),
        dcc.Tab(label='LEFT JOIN to catch every final', children=[
            html.Div([
                html.Div([
                    dcc.Markdown(
                        " The search results that I would like to present in this tab"
                        " is to find how many times teams were selected as TOP 10 in the first tab,"
                        " were the 'losing teams' in the Winners table. \n\n "
                        " This is very important information because it further distinguishes the teams that "
                        " are significantly better than others. Just getting to the Superbowl finals is a huge accomplishment,"
                        " which only confirms that the team was not there by accident, especially when "
                        " this happened several times. \n\n"
                        " So to single out the best teams and based on them "
                        " analyze which categories from Table A indicate this, these would be "
                        " 'New England Patriots, 'Denver Broncos', 'Dallas Cowboys', 'San Francisco 49ers' and 'Kansas City Chiefs' "
                        " because these teams not only had a lot of Superbowl wins but also finished second many times"
                        " - as they were the losers in the final. \n"
                        " This means that the 'New England Patriots' have been to the finals a total of 11 times, "
                        " which is 3 more than the teams that come second after him, having a total of 8 finals.\n\n"
                        " Without a doubt, it is worth checking out the 'New England Patriots' and the entire top teams in this table to see "
                        " in which categories they have the most points, which I will present in the following tables.")
                ], style={'width': '50%', 'textAlign': 'left', 'font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query3(Final_Losing_Count).png',
                             style={'width': '100%', 'height': '110%'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ]),
        dcc.Tab(label='Final answer', children=[
            html.Div([
                html.Div([
                    dcc.Markdown(
                        " In this search we find the answer to the main question, which is"
                        " what variables and their values are most typical for winning teams"
                        " So if someone wanted to predict the future Super Bowl winners,  "
                        " which categories should be followed. \n\n"
                        " The teams marked in blue in the table are those that were number 3 in the previous tab "
                        " were chosen as particularly strong due to their large number of Superbowl wins and 2nd place finishes. \n\n"
                        " I created two searches to make the favorite - 'New England Patriots',"
                        " was in a separate table to make it easier to compare results. For searching "
                        " I didn't use all the features from Table A, only those that I reduced during the previous stages "
                        " of the application, which is described in detail on the 'Correlation' and 'PCA' pages.\n\n"
                        " When it comes to the analysis of the 'New England Patriots', it is undoubtedly a special element"
                        " is the value of CCH = coaching, up to 100 points. And also FUT = point estimate of winnings in "
                        " next 5 seasons at 97 points and FRL = Fan Power Rating at 90 points."
                        " Other categories with high indicators are TRD = what is the historical number of wins at 81 points."
                        " and BNG = ratio of dollar spent by fans to number of wins equal to 84 points. \n\n"
                        " When we look at these values in other teams, we can see that they are high everywhere, but"
                        " they almost never all occur at a high level as is the case."
                        " 'New England Patriots'. For example, 'New York Giants', has only high CCH and TRD from this list."
                        " 'Kansas City Chiefs' have high CCH, high FUT, but low TRD and BNG. 'Pittsburgh Steelers'"
                        " has high TRD, high FUT and FRL but CCH and BNG have low.\n\n"
                        " So this is the final answer I was looking for and which I wanted to present to you: "
                        " **The most important features for estimating a team's future wins are:CCH, FUT, TRD, FRL and BNG. "
                        " The most important thing is that all these values are high, and not selectively at the maximum value."
                        " It is better for a team to have 80 points in 5 of these features than 100 points in two and 60 points in the remaining ones.**\n\n"
                        " For the full picture, we need to check out the second-place teams: 'Dallas Cowboys', 'Pittsburgh Steelers'"
                        " and 'Denver Broncos', which have different values. However, it can be concluded that each of these three "
                        " teams have a total points in this range of 600+ and have either FUT, TRD or FRL at a high level. "
                        " The closer the better. This is perfectly confirmed by the 'Pittsburgh Steelers', who have the same number of wins "
                        " as the New England Patriots, but he participated in significantly fewer finals. It has low CCH, but"
                        " FUT, FRL and TRD are at a high level.\n\n"
                        " As it turns out, the sum of the remaining points does not have a big impact, as evidenced by the 'Green Bay Packers'"
                        " with the most points, but not in the categories that matter.\n\n."
                        " Finally, it is worth taking a look at the 'Washington Redskins' and 'San Francisco 49ers', who have very little"
                        " points in all categories, but there are two categories that distinguish them from others. And there "
                        " is the relationship between BNG and AFF points. These two teams indicate that if a given team "
                        " does not have many points in other categories, the higher the BNG and the lower the AFF, the better. "
                        " Especially when the sum is closer to the value = 100. This is precisely presented in the second table. "
                        " However, this only applies when CCH, TRD, FUT and FRL are low. ")
                ], style={'width': '50%', 'textAlign': 'left', 'font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query4(Best_Variables).png',
                             style={'width': '100%', 'height': '110%'}),
                    html.Img(src='/assets/Query4.1(BNG + AFF).png',
                             style={'width': '100%', 'height': '110%'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ]),
        dcc.Tab(label='Additional Stadium info - DENSE RANK, PARTITION BY', children=[
            html.Div([
                html.Div([
                    dcc.Markdown(
                        " In this tab I present additional data about stadiums and matches."
                        " The first information that remains the same is that all Superbowl finals,"
                        " without exception took place on Sunday. \n\n"
                        " Additionally, we can see that even though it is a huge event,"
                        " The stands weren't always full. There are quite a few matches where attendance was below average."
                        " or equal to. (Then 'below average' is also returned.\n\n"
                        " Without a doubt, the 'Pittsburgh Steelers' games always attract the most fans, which makes"
                        " result above average.\n\n"
                        " The Rose Bowl definitely hosts the most matches, but there are still finals,"
                        " where the number of guests is below average.")
                ], style={'width': '50%', 'textAlign': 'left', 'font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query5(Game_attendance, dense_rank).png',
                             style={'width': '100%', 'height': '110%'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ]),
        dcc.Tab(label='Additional stadium info - LEAD,LAG, attendance changes', children=[
            html.Div([
                html.Div([
                    dcc.Markdown(
                        " In this tab I present additional data regarding the growth or decline of fans "
                        " at a specific stadium, compared to the previous match of a specific stadium.\n\n"
                        " It is clear that it is difficult to find an increase or decrease in fans in the stands based only on teams. "
                        " Especially when matches are played in such different places. "
                        " The increased and decreased values are very different for each team. "
                        " Therefore, the specific reason for the attendance should be sought in other factors, "
                        " such as ticket prices, location, distance of the stadium from the city the team comes from, etc.\n\n ")
                ], style={'width': '50%', 'textAlign': 'left', 'font-size': '23px'}),

                html.Div([
                    html.Img(src='/assets/Query6(Lead, lag, attendance_changes).png',
                             style={'width': '100%', 'height': '110%'})
                ], style={'width': '50%', 'display': 'flex', 'flex-direction': 'column'})

            ], style={'display': 'flex', 'width': '100%', 'align-items': 'flex-start', 'gap': '20px', 'margin': '30px'})
        ])
    ])
        ])

app = dash.Dash(__name__)
query = SQLqueries()
app.layout = query.get_layout()

