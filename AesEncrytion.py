from PIL import Image
import cv2
import numpy as np
import csv
from aes import AES
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import unittest
from Crypto.Cipher import AES



#from Crypto.Cipher import AES

#Webcam'den görüntü alıyoruz.

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cv2.imshow('frame',frame)

#Webcam'den aldığımız görüntüyü kaydediyoruz.

cv2.imwrite('webcam.jpg',frame)

cv2.waitKey(0)
img = Image.open('webcam.jpg')

#Sistemin daha hızlı çalışabilmesi için resmi yeniden şekillendiriyoruz.

new_img = img.resize((200,150), Image.ANTIALIAS)
quality_val = 90 
new_img.save("img_new.jpg", "JPEG", quality=quality_val)


#Kaydettiğimiz görüntüyü diziye aktarıyoruz.


arr = np.array(img) 

#Diziyi binary diziye çeviriyoruz.
        

binary_repr_v = np.vectorize(np.binary_repr)
print()
print(binary_repr_v(arr, 8))
 
binaryDizi=binary_repr_v(arr, 8)

img = cv2.imread('img_new.jpg',1)


yenidizi=np.zeros((len(binaryDizi),len(binaryDizi[0]),len(binaryDizi[0][0])),'U8')

t=np.random.randint(2, size=(len(binaryDizi),len(binaryDizi[0]),len(binaryDizi[0][0]),8))

#Dizimizi daha iyi görebilmek adına dosyaya kaydediyoruz.



with open('bitlerimiz.txt', 'w') as f:
    csv.writer(f, delimiter=' ').writerows(binary_repr_v(arr, 8))


#Güvenliği sağlamak adına random key oluşturuyoruz.
    
    
key = str(np.random.randint(2,size=(16)))
key=str(key).strip('[]')
key=key.replace("'","")
key=key.replace(" ","")



intdizinonxor=np.zeros((len(binaryDizi),len(binaryDizi[0]),len(binaryDizi[0][0])),'int')

#AES ile şifreleme kısmını burada yapıyoruz.


cipher = AES.new(key)

ciphertext = cipher.encrypt(binaryDizi)

#Şifreli metni binary diziye dönüştürüyoruz.


int_values = [x for x in ciphertext]

a=np.asarray(int_values)

#Reshape işlemi yapıyoruz.
                      
                      
a=a.reshape(int(a.size/(800*3)),int(a.size/(a.size/(800*3)*3)),3)

plt.imsave('sifrelenmis.png', np.asarray(a), cmap=cm.gray)

