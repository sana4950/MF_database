import streamlit as st
import pandas as pd

st.title('モンスター情報DB')
st.subheader('種族一覧')

df=pd.read_csv('MF_database.csv',index_col='モンスター名')

#ピクシー種ボタン作成していく
if st.button(label='ピクシー種'):
    family=['ピクシー','ミント','スエコ']
    stock=st.selectbox(label='ピクシー種一覧',options=family)
    tgt=df.loc[stock]

#status_1
st.write(tgt.filter(items=stock,axis=0).filter(items=['レア','メイン','サブ']))
