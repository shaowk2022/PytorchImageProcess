import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# 读取网络图像
url = "https://www.manongbook.com/d/file/python/e17c6518b44b6591781903c81d6590f14.jpg"
response = requests.get(url)
img_pil = Image.open(BytesIO(response.content))

print(img_pil.width, img_pil.height, img_pil.mode, img_pil.format, type(img_pil))
# 453 340 RGB PNG <class 'PIL.PngImagePlugin.PngImageFile'>

#从PIL Image转为numpy
img_np = np.array(img_pil)
plt.imshow(img_np) # 将图片放入图片显示窗口里
plt.axis("off") # 关闭显示图片的坐标轴
plt.show() # 弹出显示窗口
