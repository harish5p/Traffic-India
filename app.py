import pandas as pd
import streamlit as st


def get_data():
    df_tomtom = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/tomtom_reports/tomtom_trafic_index.csv")
    df_tomtom_india = df_tomtom[df_tomtom['country']=="India"]    
    df_tomtom_india['date'] = pd.to_datetime(df_tomtom_india['date'])   
    df_tomtom_india_average = df_tomtom_india.groupby("date").mean()
    return df_tomtom_india, df_tomtom_india_average



def main():
    #Some title and descriptive text
    st.title("Daily TomTom traffic congestion data of major cities in India")

    #Getting the data and displaying the dataframe in the dashboard
    data, df_tomtom_india_average = get_data()
    
    df_tomtom_india_bengaluru = data[data['city']=="Bengaluru"]
    df_tomtom_india_mumbai = data[data['city']=="Mumbai"]
    df_tomtom_india_newdelhi = data[data['city']=="New Delhi"]
    df_tomtom_india_pune = data[data['city']=="Pune"]
    

    df_tomtom_india_bengaluru["congestion_ma"] = df_tomtom_india_bengaluru['congestion'].rolling(7,center=False).mean() 
    df_tomtom_india_bengaluru["diffRatio_ma"] = df_tomtom_india_bengaluru['diffRatio'].rolling(7,center=False).mean() 

    df_tomtom_india_mumbai["congestion_ma"] = df_tomtom_india_mumbai['congestion'].rolling(7,center=False).mean() 
    df_tomtom_india_mumbai["diffRatio_ma"] = df_tomtom_india_mumbai['diffRatio'].rolling(7,center=False).mean() 

    df_tomtom_india_newdelhi["congestion_ma"] = df_tomtom_india_newdelhi['congestion'].rolling(7,center=False).mean() 
    df_tomtom_india_newdelhi["diffRatio_ma"] = df_tomtom_india_newdelhi['diffRatio'].rolling(7,center=False).mean() 

    df_tomtom_india_pune["congestion_ma"] = df_tomtom_india_pune['congestion'].rolling(7,center=False).mean() 
    df_tomtom_india_pune["diffRatio_ma"] = df_tomtom_india_pune['diffRatio'].rolling(7,center=False).mean() 

    df_tomtom_india_average["congestion_ma"] = df_tomtom_india_average['congestion'].rolling(7,center=False).mean() 
    df_tomtom_india_average["diffRatio_ma"] = df_tomtom_india_average['diffRatio'].rolling(7,center=False).mean()   
    
    # Change the index to date
    df_tomtom_india_bengaluru.set_index('date', inplace=True)
    df_tomtom_india_mumbai.set_index('date', inplace=True)
    df_tomtom_india_newdelhi.set_index('date', inplace=True)
    df_tomtom_india_pune.set_index('date', inplace=True)
    
    #Sidebar    
    st.sidebar.header("Traffic Congestions")
    st.sidebar.caption("This dashboard showcases the daily number of traffic congestions recorded in major cities of India. The data is taken from https://github.com/ActiveConclusion/COVID19_mobility")    
    st.sidebar.caption("This dashboard is created by Harish Pentapalli https://github.com/harish5p/Traffic-India")    
              
    st.title("Bengaluru Traffic Congestion")
    st.line_chart(df_tomtom_india_bengaluru[['congestion','congestion_ma']])
    
    
    st.title("Mumbai Traffic Congestion")
    st.line_chart(df_tomtom_india_mumbai[['congestion','congestion_ma']])
    
    
    st.title("New Delhi Traffic Congestion")
    st.line_chart(df_tomtom_india_newdelhi[['congestion','congestion_ma']])
    
    
    st.title("Pune Traffic Congestion")
    st.line_chart(df_tomtom_india_pune[['congestion','congestion_ma']])
    
    
    st.title("India Average Traffic Congestion")
    st.line_chart(df_tomtom_india_average[['congestion','congestion_ma']])
    
    
    
     #Creating Bengaluru Traffic Congestion Diff plot
    st.title("Bengaluru Traffic Congestion DiffRatio")
    st.line_chart(df_tomtom_india_bengaluru[['diffRatio', 'diffRatio_ma']])
    
    
    st.title("Mumbai Traffic Congestion DiffRatio")
    st.line_chart(df_tomtom_india_mumbai[['diffRatio', 'diffRatio_ma']])
    
    
    st.title("New Delhi Traffic Congestion DiffRatio")
    st.line_chart(df_tomtom_india_newdelhi[['diffRatio', 'diffRatio_ma']])
    
    
    st.title("Pune Traffic Congestion DiffRatio")
    st.line_chart(df_tomtom_india_pune[['diffRatio', 'diffRatio_ma']])
    
    
    st.title("India Average Traffic Congestion DiffRatio")
    st.line_chart(df_tomtom_india_average[['diffRatio', 'diffRatio_ma']])

if __name__ == "__main__":

    #Here we are setting the page configuration setting
    st.set_page_config(
        page_title="India Traffic Congestions",
        page_icon="🇮🇳",
        layout="wide",
        initial_sidebar_state="auto"
    )

    main()
