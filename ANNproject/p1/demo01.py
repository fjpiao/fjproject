from tensorflow.examples.tutorials.mnist import input_data
import scipy.misc
import os
from PIL import Image
import matplotlib.pyplot as mp
mnist = input_data.read_data_sets('mnist_data', one_hot=True)

save_dir = 'mnist_data/raw/'
if os.path.exists(save_dir) is False:
    os.makedirs(save_dir)


image_array = mnist.train.images[1, :]
print(image_array.shape)
image_array = image_array.reshape(28, 28)
print(image_array)
filename=save_dir

# im=Image.fromarray(image_array,'L')
# im.show()

# mp.gray()
mp.imshow(image_array)
mp.show()
# print(mnist.train.labels[0,:])
