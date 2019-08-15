from PIL import Image
#打开图片
image=Image.open('image/cat.jpg')
print(help(Image.open('image/cat.jpg')))
print('format:',image.format)
print('mode:',image.mode)
print('size:',image.size)

#rotate: 图片旋转
image.rotate(45).show()
#图片缩放
image.thumbnail([128,128],Image.ANTIALIAS)
image.save('image/cat3' + ".jpg", "JPEG")
image.resize([128,128],Image.ANTIALIAS)
image.save('image/cat4' + ".jpg", "JPEG")
print()