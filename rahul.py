import cv2
import numpy as np
from matplotlib import pyplot as plt
img_original= cv2.imread('nature.jpg')
img= cv2.cvtColor(img_original,cv2.COLOR_BGR2RGB)
x,y,z=np.shape(img)
mirror_img=np.zeros((x,y,z),dtype=int)
for i in range(0,x):
    k=0
    for j in range(y-1,0,-1):
        mirror_img[i][j][0]=img[i][j][0]
        mirror_img[i][j][1]=img[i][j][1]
        mirror_img[i][j][2]=img[i][j][2]

        k=k+1


    cv2.imwrite('nature.jpg',mirror_img)
    plt.subplot(1,2,1)
    plt.title('orginial Image')
    plt.imshow(img)
    plt.subplot(1,2,2)
    plt.title('mirror image')
    plt.imshow(mirror_img) 









