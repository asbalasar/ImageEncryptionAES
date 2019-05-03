from PIL import Image
import cv2
import numpy as np
import pickle
import csv
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.cm as cm



cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cv2.imshow('frame',frame)
cv2.imwrite('webcam.jpg',frame)

cv2.waitKey(0)
img = Image.open('webcam.jpg')
new_img = img.resize((50,50), Image.ANTIALIAS)
quality_val = 90 ##you can vary it considering the tradeoff for quality vs performance
new_img.save("img_new.jpg", "JPEG", quality=quality_val)
arr = np.array(img) # 640x480x4 array
 # 4-vector, just like above
#print (arr)
        
binary_repr_v = np.vectorize(np.binary_repr)
print()
print(binary_repr_v(arr, 8)) 
asd=binary_repr_v(arr, 8)
img = cv2.imread('img_new.jpg',1)
#cv2.imshow("Sifrelenmemis Resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
    
with open("img_new.jpg", "r+b") as image:
  x = image.read()
  #for b in f:
  print("piksel no:" ,x[0])   

print ("dizinin uzunlugu : ",len(x))

with open('tmp_file.txt', 'w') as f:
    csv.writer(f, delimiter=' ').writerows(binary_repr_v(arr, 8))

yenidizi=np.zeros((len(asd),len(asd[0]),len(asd[0][0])),'U8')

t=np.random.randint(2, size=(len(asd),len(asd[0]),len(asd[0][0]),8))

for i in range(len(asd)):
    for k in range(len(asd[0])):
        for l in range(len(asd[0][0])):
            for m in range(8):
                if bool(t[i][k][l][m]) != bool(int(asd[i][k][l][m])):
                   yenidizi[i][k][l]=yenidizi[i][k][l]+'1'
                else:
                   yenidizi[i][k][l]=yenidizi[i][k][l]+'0'


eskidizi=np.zeros((len(asd),len(asd[0]),len(asd[0][0])),'U8')
for i in range(len(asd)):
    for k in range(len(asd[0])):
        for l in range(len(asd[0][0])):
            for m in range(8):
                if bool(t[i][k][l][m]) != bool(int(yenidizi[i][k][l][m])):
                   eskidizi[i][k][l]=eskidizi[i][k][l]+'1'
                else:
                   eskidizi[i][k][l]=eskidizi[i][k][l]+'0'

intdizixor=np.zeros((len(asd),len(asd[0]),len(asd[0][0])),'int')
intdizinonxor=np.zeros((len(asd),len(asd[0]),len(asd[0][0])),'int')

for i in range(len(asd)):
    for k in range(len(asd[0])):
        for l in range(len(asd[0][0])):
                intdizixor[i][k][l]=int(yenidizi[i][k][l],2)                 
for i in range(len(asd)):
    for k in range(len(asd[0])):
        for l in range(len(asd[0][0])):
                intdizinonxor[i][k][l]=int(eskidizi[i][k][l],2) 
plt.imsave('sifreli.png', np.array(intdizixor), cmap=cm.gray)
plt.imsave('sifresiz.png', np.array(intdizinonxor), cmap=cm.gray)

# =============================================================================
# img = cv2.imread('img_new.jpg',2)
# ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# cv2.imshow("Binary Image",bw_img)
# cv2.imwrite('img_new.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()   
# =============================================================================

# =============================================================================
# 
# def sifreleme():
#     for b in x:
#         b=b+1;
# sifreleme();
#        
# =============================================================================
        
        
        
        
        
 