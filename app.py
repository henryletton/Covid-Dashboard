'''
    File name: app.py
    Author: Henry Letton
    Date created: 2020-11-29
    Python Version: 3.8.3
    Desciption: Streamlit app to show uk covid cases
'''

import pandas as pd
import streamlit as st
import plotly.express as px

# Webpage def
def main():

    # Get main data
    df = load_data().sort_values('Specimen date')
    
    # User input
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Cases", "Data"])
    area = st.sidebar.selectbox("Choose area type", ["All", "Lower-Tier Local Authority"], index=1)
    
    # Filter according to user input
    if area == 'Nation':
        area_in_df = 'nation'
    elif area == 'Region':
        area_in_df = 'region'
    elif area == 'Upper-Tier Local Authority':
        area_in_df = 'utla'
    elif area == 'Lower-Tier Local Authority':
        area_in_df = 'ltla'
    
    if area == 'All':
        df_area_fil = df.copy()
    else:
        df_area_fil = df[df['Area type'] == area_in_df].copy()

    # Define different pages
    if page == "Homepage":
        st.header("About")
        st.write("This a dashboard to display data on covid.")
        st.write("Please select a page on the left.")
    
    elif page == "Cases":
        st.title("Covid Cases in UK Areas")
        area_list = list(df_area_fil['Area name'].unique())
        area_list.sort()
        chosen_area = st.selectbox("Choose an area to view", area_list, index=0)
        chosen_metric = st.selectbox("Daily or cumulative cases", ['Daily', 'Cumulative'], index=0)
        visualize_data(df_area_fil, chosen_area, chosen_metric)
    
    elif page == "Data":
        st.dataframe(df)

# Cache data, to save on running time
@st.cache
def load_data():
    url = "https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv"
    df = pd.read_csv(url)
    #df = df_all[df_all['Area name'] == 'Elmbridge']
    return df

# Function to plat chart based on user selection
def visualize_data(df, chosen_area, chosen_metric, chosen_period="Specimen date"):
    
    df_filter = df[df['Area name'] == chosen_area]
    
    if chosen_metric == 'Daily':
        chosen_metric2 = 'Daily lab-confirmed cases'
    else:
        chosen_metric2 = 'Cumulative lab-confirmed cases'
    
    
    graph = px.line(df_filter, x=chosen_period, 
              y=chosen_metric2, 
              title=f'Covid in {chosen_area}')

    st.write(graph)

if __name__ == "__main__":
    main()

