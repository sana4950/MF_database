import streamlit as st
import pandas as pd

family=['ピクシー','ミント','スエコ']

st.title('モンスター情報DB')
st.subheader('種族一覧')

df=pd.read_csv('MF_database.csv',index_col='モンスター名')

#ピクシー種ボタン作成していく
family_select=st.button(label='ピクシー種')
if family_select:
    if 'push_1' not in st.session_state:
        st.session_state.push_1=False
    #select作成
    stock=st.session_state.selectbox(label='ピクシー種一覧',options=family)
    if stock:
        st.session_state.push_1=True
    #Trueなら以下処理に入る
    if st.session_state.push_1=True:
        #列でデータ分割表示
        cols=st.columns(2)
        #左列表示
        with cols[0].container():
            #status_1
            st.write(df.loc[stock].filter(items=['レア','メイン','サブ']))
            #status_2
            st.write(df.loc[stock].filter(items=['ライフ','ちから','かしこさ','命中','回避','丈夫さ']))
        #右列表示
        with cols[1].container():
            #status_3
            st.write(df.loc[stock].filter(items=['初期技1','初期技2']))
            #status_4
            st.write(df.loc[stock].filter(items=['登録可能技1','登録可能技2']))
