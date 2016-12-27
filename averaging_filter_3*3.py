#coding:utf-8
from  PIL import Image

im = Image.open('monochrome.jpg')
#get size
size = im.size
#get pixel
px = im.load()
n = 0
g = []

for x in range(size[0]):
	for y in range(size[1]):
		for a in range(-1,2):
			for b in range(-1,2):
				if x+a<0 or y+b<0 or x+a>size[0]-1 or y+b>size[1]-1:
					continue
				g.append(px[x+a,y+b][0])
		for c in range(len(g)):
			n = n + g[c]
		n = n // len(g)
		im.putpixel((x,y),(n,n,n))
		n = 0
		m = len(g)
		for l in range(m):
			del g[0]
im.save('3*3.jpg')