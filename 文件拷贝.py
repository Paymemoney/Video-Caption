import os
import shutil


for i in range(0,10000):
    if i%100==0:
        print(i)
    if not os.path.exists(".\\data\\feats\\c3d_feats\\video"+str(i)+".npy"):
        shutil.copy(".\\data\\feats\\c3d_feats_first\\video"+str(i)+".npy",".\\data\\feats\\c3d_feats")

