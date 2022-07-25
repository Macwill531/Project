import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Stock Price Visualization')
st.header('Stock Prices 2022')
st.subheader('It is working')

### --- LOAD DATAFRAME
excel_file = 'value_strategy.xls'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:N',
                   header=0)

st.dataframe(df)

# --- PLOT PIE CHART
pie_chart = px.pie(df,
                   title='STOCKS',
                   values='Price',
                   names='Ticker')

st.plotly_chart(pie_chart)

#mask = df 

# --- PLOT BAR CHART
bar_chart = px.bar(df,
                   x='Ticker',
                   y='Price',
                   text='Price',
                   color_discrete_sequence = ['#F63366']*len(df),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

## ---- SIDEBAR ----
#st.sidebar.header("Please Filter Here:")
#ticker = st.sidebar.multiselect(
#    "Select the Ticker:",
#    options=df["Ticker"].unique(),
#    default=df["Ticker"].unique()
#)
##
##number_of_shares_to_buy = st.sidebar.multiselect(
##    "Select the Customer Type:",
##    options=df["Number of Shares to Buy"].unique(),
##    default=df["Number of Shares to Buy"].unique(),
##)
#
#rv_score = st.sidebar.multiselect(
#    "Select the RV Score:",
#    options=df["RV Score"].unique(),
#    default=df["RV Score"].unique()
#)
#
## SALES BY PRODUCT LINE
#df_selection = df.query(
#    "Ticker == @ticker & Number of Shares to Buy ==@number_of_shares_to_buy & RV Score == @rv_score"
#)
#
## SALES BY PRODUCT LINE [BAR CHART]
#sales_by_product_line = (
#    df_selection.groupby(by=["Ticker"]).sum()[["RV Score"]].sort_values(by="RV Score")
#)
#fig_product_sales = px.bar(
#    sales_by_product_line,
#    x="RV Score",
#    y=sales_by_product_line.index,
#    orientation="h",
#    title="<b>Sales by Product Line</b>",
#    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#    template="plotly_white",
#)
#fig_product_sales.update_layout(
#    plot_bgcolor="rgba(0,0,0,0)",
#    xaxis=(dict(showgrid=False))
#)

# --- PLOT BAR CHART
bar_chart = px.bar(df,
                   y='Ticker',
                   x='Number of Shares to Buy',
				   orientation="h",
                   text='Number of Shares to Buy',
                   color_discrete_sequence = ['#F63366']*len(df),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- PLOT PIE CHART
pie_chart = px.pie(df,
                   title='RV SCORE',
                   values='RV Score',
                   names='Ticker')
st.plotly_chart(pie_chart)

















