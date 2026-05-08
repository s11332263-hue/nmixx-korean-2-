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
                video_url = f"https://www.youtube.com/watch?v=fg9Z4-Dnukk&t={sec}s"
                
                with st.expander(f"⏰ {sec//60}分{sec%60}秒 | {row['內容']}"):
                    st.video(video_url)
        else:
            st.error("AI 好像沒聽清楚這個詞，換個簡單的字試試？")
except Exception as e:
    st.warning("資料庫讀取中，或是 CSV 格式不對喔！")
