My web application called "NFL in numbers" is my own project to showcase my data analysis skills

The application is based on Dash and uses Flask as a backend. On each subpage it describes different issues related to data analysis, everything is based on American football teams.

- Interactive dashboard divided into tabs and pages
- Statistical analysis of NFL teams
- Data visualizations: PCA, regression, correlation
- Tables, queries in SQL Server

![enef1](https://github.com/user-attachments/assets/8a043ecf-6cff-48b3-badd-a90170fdb818)
![enef2](https://github.com/user-attachments/assets/1859be51-4ef7-4523-8235-7e3382852e46)
![enef4](https://github.com/user-attachments/assets/6908e06a-40cc-4be6-aaf2-265749e3833a)
![enef3](https://github.com/user-attachments/assets/9820b302-3d80-40f6-8069-70811ae6658c)


Based on data found on the internet, I use a table that defines specific categories based on which I evaluate each team, e.g. CCH = which evaluates the value of the coach. The values ​​are in the form of numbers from 0 to 100.

1. The main.py file = is the main file of the entire application, which contains all the mechanics of the code, it also contains a table containing the teams and their assigned categories and points, as well as a table explaining which category means what

2. In the database folder there is a table describing the categories and a table from Wikipedia, which is downloaded using Web Scraping. Both of these works are placed in the winners_table.py and legend_text.py files, respectively. In the database folder there is also a file from SQL Server with all the executed commands

3. The assets folder contains the screenshots that I use in the application.

4. The standard_dev.py file contains the calculation of the standard deviation and a graph built on this basis, as well as a description of the results

5. The mean.py file contains the calculation of the mean and also a graph built on this basis, as well as a description of the results

6. In the correlation.py file, I placed the code with which I created the correlation matrix and a description of the results

7. The pca.py file contains the code with which I created the principal component analysis, a graph describing the results, as well as text in which I explain specific actions

8. The clustering.py file contains the code with which I divided the data into clusters, graphs describing the research methods and an explanation of the process.

9. The regression.py file contains the code that creates an interactive graph of the regression model residuals, thanks to which you can try to calculate the future value for a given category for each team.

10. The file contains a text description of the results of the actions in SQL and screenshots from the 'assets' folder, which show the code I made in SQL Server.

11. At the very end, results.py contains a few sentences in which it mainly describes the conclusions resulting from my analysis.

As I mentioned, the project is entirely my own, and the data I used is publicly available. I will gladly share what was most difficult during the creation process:
- undoubtedly creating an interactive graph of the regression residual model, in such a way that each value was assigned to a team and establishing the correct @callback function to update it all

- in second place I would consider the clustering graph, although it is not too complicated, it took me a lot of time to create the correct code

- logic, as this is my first fully independent, large analytical work, creating the entire process of data analysis, conclusions, dependencies and their appropriate presentation was difficult, but at the same time very developmental :)

© 2025 Karol B. Krawczyk, All Rights Reserved
