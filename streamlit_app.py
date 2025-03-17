from PIL import ImageGrab, Image
import time



m1 = ImageGrab.grabclipboard()
if st.button("save"):
    m1.save('test_image.png')

