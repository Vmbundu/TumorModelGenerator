import pyopenvdb as vdb
import numpy as np 
from PIL import Image
import PIL.ImageOps
img_1 = Image.open('test/tumor0000.jpg').convert('L')
img_1 = PIL.ImageOps.invert(img_1)
img_1 = img_1.convert('1')
#img_2 = Image.open('Tumor_Renderings/tumor_2.jpg').convert('L')
np_img_1 = np.array(img_1).astype(float)
#np_img_2 = np.array(img_2).astype(float)
#img = np.stack((np_img_1, np_img_2), axis = -1)
img = [np_img_1]
#print()
for x in range(1,201):
    num = '{:0>4}'.format(x) 
    link = 'test/tumor'+str(num)+'.jpg'
    img_ = Image.open(link).convert('L')
    img_ = PIL.ImageOps.invert(img_)
    img_ = img_.convert('1')
    np_img = np.array(img_).astype(float)
    img.append(np_img)
img = np.array(img)
print(img.shape)
grid = vdb.FloatGrid()
grid.copyFromArray(img)
vdb.write('tumor.vdb', grids=grid,metadata=None)
