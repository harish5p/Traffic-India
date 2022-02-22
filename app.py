from collections import namedtuple
import plost
import math
import pandas as pd
import streamlit as st


df_tomtom = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/tomtom_reports/tomtom_trafic_index.csv")
df_tomtom_india = df_tomtom[df_tomtom['country']=="India"]
df_tomtom_india['date'] = pd.to_datetime(df_tomtom_india['date'])

df_tomtom_india_bengaluru = df_tomtom[df_tomtom['city']=="Bengaluru"]
df_tomtom_india_mumbai = df_tomtom[df_tomtom['city']=="Mumbai"]
df_tomtom_india_newdelhi = df_tomtom[df_tomtom['city']=="New Delhi"]
df_tomtom_india_pune = df_tomtom[df_tomtom['city']=="Pune"]
df_tomtom_india_average = df_tomtom_india.groupby("date").mean()


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

plost.line_chart(
  df_tomtom_india_bengaluru,
  x='date',
  y=('congestion', 'congestion_ma'),  
)
