'''
    File name: data to chart.py
    Author: Henry Letton
    Date created: 2020-11-29
    Python Version: 3.8.3
    Desciption: From gov site to chart
'''

#%% Import modules
import pandas as pd
from collections import Counter

#%% Download data
#https://coronavirus.data.gov.uk/details/download

url = "https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv"
cases_df = pd.read_csv(url)

#%% 

print(list(cases_df.columns))

areas = Counter(cases_df['Area type'])

#%% Filter to specific area

cases_area_df = cases_df[cases_df['Area name'] == 'Elmbridge']

#%% Plot data

import plotly.express as px
from plotly.offline import plot

#df = px.data.gapminder().query("country=='Canada'")
fig = px.line(cases_area_df, x="Specimen date", 
              y="Daily lab-confirmed cases", 
              title='Covid in Elmbridge')
#fig.show()

plot(fig)

#%% 

import plotly.express as px
from plotly.offline import plot

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
plot(fig)