from multiprocessing import Pool
import os, sys
import Image

size = 128, 128
def shrink_image(img):
	try:
		im = Image.open("inria-horses-v103/neg/"+img)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save("not_horses/" + img, "JPEG")
	except IOError:
		print "cannot create thumbnail for %s" % img

p = Pool(20)
files = filter( lambda x: x[-3:]=='jpg',os.listdir("inria-horses-v103/neg/"))
p.map(shrink_image, files)