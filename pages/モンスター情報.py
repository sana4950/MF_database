import streamlit as st
import pandas as pd

st.title('モンスター情報DB')
st.subheader('種族一覧')

df=pd.read_csv('MF_database.csv',index_col='モンスター名')

#ピクシー種ボタン作成していく
if st.button(label='ピクシー種'):
    family=['ピクシー','ミント','スエコ']
    stock=st.selectbox(label='ピクシー種一覧',options=family)

    #列でデータ分割表示
    cols=st.columns(2)
    
    with cols[0].container():
    #status_1
        st.dataframe(df.loc[stock].filter(items=['レア','メイン','サブ']))
    #status_2
        st.dataframe(df.loc[stock].filter(items=['ライフ','ちから','かしこさ','命中','回避','丈夫さ']))
    #status_3
    with cols[1].container():
        st.dataframe(df.loc[stock].filter(items=['初期技1','初期技2']))
    #status_4
