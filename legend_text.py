import requests
import pandas as pd

class Legend():

        url3 = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-favorite-team/README.md"
        response = requests.get(url3)

        legend_text = response.text

        lines = legend_text.split('\n')

        table_lines = [line for line in lines if line.startswith('|')]

        header = table_lines[0].split('|')[1:-1]

        rows = []
        for line in table_lines[2:]:
            row = line.split('|')[1:-1]
            rows.append(row)

        df_legend_table = pd.DataFrame(rows, columns=header)
