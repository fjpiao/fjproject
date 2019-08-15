from PIL import Image
import numpy as np
#打开图片
image=Image.open('image/cat.jpg')
print(help(Image.open('image/cat.jpg')))
print('format:',image.format)
print('mode:',image.mode)
print('size:',image.size)

a=np.asarray(image)
print(a)
im=Image.fromarray(a)
help(im)
im.show()