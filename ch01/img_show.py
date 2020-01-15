# coding: utf-8
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread


img = imread(os.getcwd()+'/dataset/lena.png')  # 画像の読み込み
plt.imshow(img)

plt.show()
