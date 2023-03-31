import streamlit as st
import pandas as pd

#リスト作成
種族名一覧=['ピクシー種','スエゾー種','ゴーレム種']
ピクシー種=['ピクシー','ミント','スエコ']

st.title('モンスター情報DB')
st.subheader('種族一覧')

#データ抽出
df=pd.read_csv('MF_database.csv',index_col='モンスター名')

#ピクシー種ボタン作成していく
def page_p():
    st.title(ピクシー種)
    stock=st.radio(options=ピクシー種)
    ###データ表示
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

#
selected_family=st.sidebar.radio('種族選択',種族名一覧)

#
if selected_family=='ピクシー種':
    page_p()
else:
    pass#何もしない処理
