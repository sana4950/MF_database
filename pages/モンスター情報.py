import streamlit as st
import pandas as pd

st.title('モンスター情報DB')
st.subheader('種族一覧')

df=pd.read_csv('MF_database.csv',index_col='モンスター名')

if st.button('ピクシー種'):
    ピクシー種=['ピクシー','ミント','スエコ','エンジェル','リリム']
    stock=st.selectbox(label='ピクシー種一覧',
                       options=ピクシー種
                       default=['ピクシー'])
    df_tgt=df.loc[stock]
    st.dataframe(df_tgt)
