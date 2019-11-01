'''
import os
filename = "./data/voice/video1.wav"
path, ext = os.path.splitext(filename)
print(path)
print(ext)
filename = os.path.abspath(os.path.expanduser(filename))
path, ext = os.path.splitext(filename)
print(path)
print(ext)
'''
import numpy as np
a = np.load("data\\feats\\resnet152\\resnet101\\video1.npy")
print(a.shape)