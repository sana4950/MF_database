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

    cols=st.columns(2)
    #status_1
    cols[1].container():
        st.dataframe(tgt.filter(items=['レア','メイン','サブ']).filter(items=[stock],axis=0))
    #status_2
    cols[2].container():
        st.dataframe(tgt.filter(items=['ライフ','ちから','かしこさ']).filter(items=[stock],axis=0))

