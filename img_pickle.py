from multiprocessing import Pool
import cPickle as pickle
import os, sys
import Image

def process_image(img):
	try:
		im = Image.open("horses/"+img)
		# convert list of tuples into flat list
		return list(sum(list(im.getdata()), ()))
	except Exception as e:
		print str(e)
		print "cannot export data for %s" % img


p = Pool(20)
files = os.listdir("horses/")
pixels = p.map(process_image, files)
print len(pixels)
pickle.dump(pixels, open("horses.p", "wb"))