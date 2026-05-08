import streamlit as st

# 網頁標題與風格
st.set_page_config(page_title="NMIXX 韓文字典", page_icon="🎤")
st.title("🎤 NSWER 專屬：NMIXX 韓文語境字典")
st.markdown("輸入你想學的詞彙，聽聽成員們怎麼說！")

# 建立一個簡單的資料庫（暫時用手動模擬）
# 實際營運時，這裡會連動到你用 AI 跑出來的資料庫
data = {
    "안녕하세요": {"member": "Haewon", "url": "https://www.youtube.com/watch?v=5vT899m5_n8", "start": 10},
    "대박": {"member": "Lily", "url": "https://www.youtube.com/watch?v=5vT899m5_n8", "start": 45},
    "감사합니다": {"member": "Sullyoon", "url": "https://www.youtube.com/watch?v=5vT899m5_n8", "start": 120},
}

# 介面設計
col1, col2 = st.columns([2, 1])

with col1:
    search_word = st.text_input("輸入韓文單字 (例如: 안녕하세요, 대박):", "")

with col2:
    member_filter = st.selectbox("指定成員:", ["全部", "Lily", "Haewon", "Sullyoon", "BAE", "Jiwoo", "Kyujin"])

# 搜尋邏輯
if search_word in data:
    result = data[search_word]
    
    # 如果有過濾成員，檢查是否符合
    if member_filter == "全部" or member_filter == result["member"]:
        st.success(f"找到了！這是 {result['member']} 說的 '{search_word}'")
        # 顯示影片並自動跳轉秒數
        st.video(result["url"], start_time=result["start"])
    else:
        st.warning(f"抱歉，在 {member_filter} 的片段中沒找到這個詞。")
elif search_word:
    st.error("目前資料庫還沒收錄這個詞，快去叫作者更新！")

# 側邊欄資訊
st.sidebar.info("這是一個粉絲開發的教育專案，旨在透過 NMIXX 的影片學習韓文。")