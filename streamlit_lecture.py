import streamlit as st
import pandas as pd
import plotly.express as px 
import os

st.title("My Dashboard")

file = st.file_uploader("Upload file",type=({"csv","xlsx"}))
dir = os.chdir(r"C:\Users\lenovo\Desktop\Data set")
if file is not None:
    st.write("Selected file Name: " + file.name)
    df=pd.read_csv(file.name,encoding="ISO-8859-1")
    st.write(df)
else:
    df = pd.read_csv(r"C:\Users\lenovo\Desktop\Data set\Superstore.csv",encoding="ISO-8859-1")
    st.write(df)

# col1,col2 = st.columns((2))

# df["Order Date"] = pd.to_datetime(df["Order Date"],format='mixed')

# date1 = pd.to_datetime(df["Order Date"]).min()
# date2 = pd.to_datetime(df["Order Date"]).min()
# st.write(date1)
# st.write(date2)


# with col1:
#     startTime =pd.to_datetime(st.date_input("Start date"),date1)
    

# with col2:
#     endTime = pd.to_datetime(st.date_input("end date"),date2)
    

## Sort values
df.sort_values(['Profit','Sales'],axis=0,ascending=[False,False],inplace=True)

### graph b/w Region and Sales with Category
fig = px.bar(df.head(20),x='Region',y='Sales',color='Category',width=600,title='Graph b/w Region and Sales with Category')
st.plotly_chart(fig)


### Graph  b/w region and Sales with Profit
fig = px.bar(df.head(20),x='Region',y='Sales',color='Profit',hover_data=['Category'],width=1000,title='Graph  b/w region and Sales with Profit')
st.plotly_chart(fig)


### graph order count v/s Sub Category
fig = px.bar(df.head(100),x='Sub-Category',color='Category',width=700,title='Graph b/w order count and Sub-Category')
st.plotly_chart(fig)



### graph b/w Customer Name and Quantity with Profit
fig = px.bar(df.head(20),x='Customer Name',y='Quantity',color='Profit',hover_data=['Discount','Category']
             ,width=700,height=600,title='Graph b/w Customer Name and Quantity with Profit')
st.plotly_chart(fig)



### Graph b/w Sub Category and Profit
fig = px.pie(df,names='Sub-Category',values='Profit',title='Graph b/w Sub Category and Profit')
st.plotly_chart(fig)