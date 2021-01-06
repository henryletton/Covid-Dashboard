import pandas as pd
import streamlit as st
import plotly.express as px

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Cases"])

    if page == "Homepage":
        st.header("About")
        st.write("This a dashboard to display data on covid.")
        st.write("Please select a page on the left.")
        #st.write(df)
    elif page == "Cases":
        st.title("Covid Cases in UK Areas")
        chosen_area = st.selectbox("Choose an area to view", list(df['Area name'].unique()), index=0)
        chosen_metric = st.selectbox("Daily or cumulative cases", ['Daily', 'Cumulative'], index=0)
        #y_axis = st.selectbox("Choose a var for the y-axis", df.columns, index=4)
        visualize_data(df, chosen_area, chosen_metric)


@st.cache
def load_data():
    url = "https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv"
    df = pd.read_csv(url)
    #df = df_all[df_all['Area name'] == 'Elmbridge']
    return df

def visualize_data(df, chosen_area, chosen_metric):
    
    df_filter = df[df['Area name'] == chosen_area]
    
    if chosen_metric == 'Daily':
        chosen_metric2 = 'Daily lab-confirmed cases'
    else:
        chosen_metric2 = 'Cumulative lab-confirmed cases'
    
    
    graph = px.line(df_filter, x="Specimen date", 
              y=chosen_metric2, 
              title='Covid in Elmbridge')

    st.write(graph)

if __name__ == "__main__":
    main()

