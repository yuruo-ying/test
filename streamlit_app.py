import streamlit as st
from PIL import ImageGrab

def save_image():
    # 從剪貼簿擷取圖片
    image = ImageGrab.grabclipboard()
    if image:
        # 開啟檔案儲存對話框
        file_path = st.text_input("請輸入檔案名稱（包含路徑）", "image.png")
        if st.button("儲存"):
            # 儲存圖片
            image.save(file_path)
            st.success(f"圖片已儲存至 {file_path}")
        else:
            st.warning("儲存取消")
    else:
        st.error("剪貼簿中沒有圖片")

st.title("從剪貼簿擷取圖片並儲存")
if st.button("擷取並儲存圖片"):
    save_image()
