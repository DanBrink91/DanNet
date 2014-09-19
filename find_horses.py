import cPickle as pickle
from net import *
neg_pixels = pickle.load(open('not_horses.p', "rb"))
pos_pixels = pickle.load(open('horses.p', "rb"))

hidden_layers = (128*128) / 2
horse_net = Net(128*128, hidden_layers, 1)

print len(pos_pixels)