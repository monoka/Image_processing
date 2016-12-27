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
		for a in range(-2,3):
			for b in range(-2,3):
				if x+a<0 or y+b<0 or x+a>size[0]-1 or y+b>size[1]-1:
					continue
				if a == 0 and b == 0:
					g.append(px[x+a,y+b][0]*36)
				elif a == 0 or b == 0:
					if a ==-1 or a==1 or b==1 or b==-1:
						g.append(px[x+a,y+b][0]*24)
					else:
						g.append(px[x+a,y+b][0]*6)
				elif a==-1 or a==1 or b==-1 or b==1:
					if a ==-2 or a==2 or b==-2 or b==2:
						g.append(px[x+a,y+b][0]*4)
					else:
						g.append(px[x+a,y+b][0]*16)
				else:
					g.append(px[x+a,y+b][0])
		for c in range(len(g)):
			n = n + g[c]
		n = n // 256
		im.putpixel((x,y),(n,n,n))
		n = 0
		m = len(g)
		for l in range(m):
			del g[0]

im.save('5*5g.jpg')