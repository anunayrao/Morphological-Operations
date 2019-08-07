import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)

image = cv2.imread('noise.jpg',0)
height,width = image.shape

se = [[255,255,255],[255,255,255],[255,255,255]]
se = np.asarray(se)

def dilation(image, se):
	heigth ,width = image.shape
	pimg = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
	pimg = np.asarray(pimg)
	dimg = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
	dimg = np.asarray(dimg)
	img = [[ 0 for x in range(width)] for w in range(height)]
	img = np.asarray(img)
	for i in range(height):
		for j in range(width):
			dimg[i+1][j+1] = image[i][j]
			pimg[i+1][j+1] = image[i][j]
	for i in range(height):
		for j in range(width):
			if((pimg[i][j]== se[0][0]) or (pimg[i][j+1]==se[0][1]) or (pimg[i][j+2]==se[0][2]) or (pimg[i+1][j]==se[1][0]) or (pimg[i+1][j+1]==se[1][1]) or (pimg[i+1][j+2]==se[1][2]) or (pimg[i+2][j]==se[2][0]) or (pimg[i+2][j+1]==se[2][1]) or (pimg[i+2][j+2]==se[2][2])):
				dimg[i+1][j+1] = 255
			else:
				dimg[i+1][j+1] = 0
	for i in range(height):
		for j in range(width):
			img[i][j]= dimg[i+1][j+1]
			
	return img

def erosion(image, se):
	height,width = image.shape
	pimg = [[ 255 for x in range(width + 2)] for w in range(height + 2)]
	pimg = np.asarray(pimg)
	dimg = [[ 255 for x in range(width + 2)] for w in range(height + 2)]
	dimg = np.asarray(dimg)
	img = [[ 255 for x in range(width)] for w in range(height)]
	img = np.asarray(img)
	for i in range(height):
		for j in range(width):
			dimg[i+1][j+1] = image[i][j]
			pimg[i+1][j+1] = image[i][j]
	for i in range(height):
		for j in range(width):
			if((pimg[i][j]== se[0][0]) and (pimg[i][j+1]==se[0][1]) and (pimg[i][j+2]==se[0][2]) and (pimg[i+1][j]==se[1][0]) and (pimg[i+1][j+1]==se[1][1]) and (pimg[i+1][j+2]==se[1][2]) and (pimg[i+2][j]==se[2][0]) and (pimg[i+2][j+1]==se[2][1]) and (pimg[i+2][j+2]==se[2][2])):
				dimg[i+1][j+1] = 255
			else:
				dimg[i+1][j+1] = 0
	for i in range(height):
		for j in range(width):
			img[i][j]= dimg[i+1][j+1]
			
	return img


a = dilation(image,se)
b = erosion(a,se)
c = erosion(b,se)
d = dilation(c,se)
cv2.imwrite("res_noise1.jpg",d) 

e = erosion(d,se)
i = [[ 0 for x in range(width)] for w in range(height)]
i = np.asarray(i)

for p in range(height):
	for q in range(width):
		i[p][q] = d[p][q] - e[p][q]
cv2.imwrite("res_bound1.jpg",i) 


a1 = erosion(image,se)
b1 = dilation(a1,se)
c1 = dilation(b1,se)
d1 = erosion(c1,se)
cv2.imwrite("res_noise2.jpg",d1) 

e1 = erosion(d1,se)

for p in range(height):
	for q in range(width):
		i[p][q] = d1[p][q] - e1[p][q]
cv2.imwrite("res_bound2.jpg",i)