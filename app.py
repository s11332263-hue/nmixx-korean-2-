import streamlit as st
import pandas as pd

st.title("🌟 NMIXX 韓文語境字典")

import streamlit as st
import pandas as pd

st.title("🌟 NMIXX 韓文語境字典")

# 讀取大腦
@st.cache_data
def load_data():
    # 這裡會讀取你上傳的那個 nmixx_data.csv
    df = pd.read_csv("nmixx_data.csv")
    return df

try:
    data = load_data()
    search_word = st.text_input("輸入韓文單字 (例如: 촬영, 앞머리)")

    if search_word:
        # 只要內容包含搜尋的字，就把它抓出來
        results = data[data['內容'].str.contains(search_word, na=False)]
        
        if not results.empty:
            st.success(f"找到了 {len(results)} 個片段！")
            for _, row in results.iterrows():
                # 自動幫你計算分秒，方便你看影片
                sec = int(float(row['秒數']))
                # 換成你那支 15 分鐘影片的網址
                # 這是新的，請貼上
                video_id = "fg9Z4-Dnukk"
                # 注意：嵌入式連結要用 /embed/，參數要用 ?start=
                embed_url = f"https://www.youtube.com/embed/{video_id}?start={sec}&autoplay=1"

                    with st.expander(f"⏰ {sec//60}分{sec%60}秒 | {row['內容']}"):
                    # 我們改用 HTML 模式，這能強制 YouTube 從特定秒數開始播
                    st.components.v1.html(
                        f'<iframe width="100%" height="315" src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                        height=350,
    )
        else:
            st.error("AI 好像沒聽清楚這個詞，換個簡單的字試試？")
except Exception as e:
    st.warning("資料庫讀取中，或是 CSV 格式不對喔！")
