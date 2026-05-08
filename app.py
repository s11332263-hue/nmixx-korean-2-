import streamlit as st
import pandas as pd

st.set_page_config(page_title="NMIXX 韓文字典", page_icon="🎤")
st.title("🌟 NMIXX 韓文語境字典")

# 1. 讀取 AI 產出的 CSV
@st.cache_data
def load_data():
    try:
        # 讀取你上傳的 nmixx_data.csv
        df = pd.read_csv("nmixx_data.csv")
        # 簡單過濾掉 AI 亂碼 (太短的字)
        df = df[df['內容'].str.len() > 1]
        return df
    except:
        return None

df = load_data()

if df is not None:
    word = st.text_input("輸入想搜尋的韓文：", placeholder="例如：촬영 (拍攝)")

    if word:
        # 在資料中尋找包含關鍵字的片段
        results = df[df['內容'].str.contains(word, na=False)]
        
        if not results.empty:
            st.success(f"找到 {len(results)} 個片段！")
            for index, row in results.iterrows():
                sec = int(float(row['秒數']))
                # 這是你那支 15 分鐘影片的 ID
                video_id = "fg9Z4-Dnukk"
                # 強制跳轉關鍵：使用 embed 格式並加上 start 參數
                embed_url = f"https://www.youtube.com/embed/{video_id}?start={sec}"
                
                # --- 注意：這裡的縮排必須整齊 ---
                with st.expander(f"⏰ {sec//60}分{sec%60}秒 | {row['內容']}"):
                    # 這行必須比 with 往右縮進 (通常是 4 個空格)
                    st.components.v1.html(
                        f'<iframe width="100%" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe>',
                        height=350,
                    )
        else:
            st.error("目前資料庫沒聽到這個詞，換個字試試？")
else:
    st.warning("找不到 nmixx_data.csv，請確認檔案有上傳到 GitHub 喔！")
