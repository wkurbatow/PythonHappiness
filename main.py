
import plotly.express as px
import streamlit as st
import pandas as pd


# import plotly.figure_factory as ff
st.title('В пошуках щастя')

df = pd.read_csv("happy.csv")
choise_item = df.columns[1:].to_list()
df['Колір'] = 'Інші'
df['Корупція'] = 600 - df['Корупція']
df.loc[df['country']== "Ukraine",'Колір'] = 'Україна'


col1, col2 = st.columns(2)

with col1:
    user_choise_x = st.radio('Що по горизонталі ?:', choise_item)
with col2:    
    user_choise_y = st.radio('Що по вертикалі:', choise_item)

# data_x = df[user_choise_x]
# data_y = df[user_choise_y]


st.subheader('А чи варто шукати щастя там де його не може бути взагалі? ')



figure = px.scatter(df, x=user_choise_x, y=user_choise_y, hover_name='country',
                     color ='Колір', size = 'Щастя', labels={"x" : user_choise_x, "y": user_choise_y })

st.plotly_chart(figure)

st.write('by Kurbatov VV')