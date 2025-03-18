import requests
import pandas as pd
from bs4 import BeautifulSoup


class Winners():

        page = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

        my_html = requests.get(page)

        soup = BeautifulSoup(my_html.content, 'html.parser')

        tables = soup.find_all('table', {'class': 'wikitable'})

        for table in tables:
            if "Championships table key and summary" in table.get_text():
                continue

            if "Super Bowl championships" in table.get_text():

                headers = []
                rows = []

                header_row = table.find_all('th')
                for header in header_row:
                    headers.append(header.get_text(strip=True))

                data_rows = table.find_all('tr')[1:]
                for row in data_rows:
                    cols = row.find_all('td')
                    cols = [col.get_text(strip=True) for col in cols]

                    rows.append(cols)

                df = pd.DataFrame(rows, columns=headers)

                df = df.replace('I[sb 1]', 'I', regex=False)
                df = df.replace('II[sb 1]', 'II', regex=False)
                df = df.replace('III[sb 1]', 'III', regex=False)
                df = df.replace('IV[sb 1]', 'IV', regex=False)
                df = df.replace('50[sb 17]', 'L', regex=False)

                break
