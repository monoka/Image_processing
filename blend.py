#coding:utf-8
from  PIL import Image
import numpy as np

im = Image.open("kirin.jpg")
im2 = Image.open("tora.jpg")
Image.blend(im,im2, 0.3).show()