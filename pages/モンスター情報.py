import streamlit as st
import pandas as pd

st.title('モンスター情報DB')
st.subheader('種族一覧')

df=pd.read_csv('MF_database.csv',encoding="utf-8",index_col='モンスター名')

#ピクシー種ボタン作成していく
if st.button('ピクシー種'):
    tgt=(df['メイン']=='ピクシー')
    stocks=st.selectbox(label='ピクシー種',options=tgt.index)
    data_set=tgt.loc(stocks)

    #status_1
    st.write(data_set.filter[items=stocks,axis=0].filter(items=['レア','メイン','サブ'])
             
             
