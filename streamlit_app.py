from PIL import ImageGrab, Image
import time

im1 = ImageGrab.grab() 
# im1 = ImageGrab.grab(300,100,1400,600)
TimeName = time.strftime("%Y%m%d%H%M%S", time.localtime())
path = '.\\'+str(TimeName)+'.jpg'
im1.save(path)
im1.show()  # 展示


im2 = ImageGrab.grabclipboard() 
# 判断粘贴板是否为空
if isinstance(im2, Image.Image):
    im2.save('.\\a.jpg')
else:
    print("no no no ")

