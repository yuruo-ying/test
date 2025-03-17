from PIL import ImageGrab, Image
import time
import streamlit.components.v1 as components
import streamlit as st

st.title("從剪貼簿擷取圖片")

# JavaScript 讀取剪貼簿圖片並傳給 Streamlit
clipboard_js = """
<button id="pasteBtn">貼上圖片</button>
<canvas id="imageCanvas" style="border:1px solid black; width:100%;"></canvas>

<script>
document.getElementById("pasteBtn").addEventListener("click", async function() {
    try {
        const clipboardItems = await navigator.clipboard.read();
        for (const item of clipboardItems) {
            for (const type of item.types) {
                if (type.startsWith("image/")) {
                    const blob = await item.getType(type);
                    const imgURL = URL.createObjectURL(blob);
                    
                    // 顯示在 canvas
                    const img = new Image();
                    img.onload = function() {
                        const canvas = document.getElementById("imageCanvas");
                        const ctx = canvas.getContext("2d");
                        canvas.width = img.width;
                        canvas.height = img.height;
                        ctx.drawImage(img, 0, 0);
                    };
                    img.src = imgURL;

                    return; // 只處理第一張圖片
                }
            }
        }
    } catch (err) {
        console.error("無法存取剪貼簿", err);
    }
});
</script>
"""

components.html(clipboard_js, height=300)

