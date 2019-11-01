import numpy as np

def cut(data):
    #a = np.zeros((40,512))
    data = data.reshape((1,-1))
    if data.shape[1] > 20480:
        data = np.delete(data,np.s_[20479:-1],axis=1)
    if data.shape[1] < 20480:
        a = np.zeros((1,20480-data.shape[1]))
        data = np.c_[data,a]
    #print(data.shape[1])
    data = data.reshape((40,512))
    return data




srcname1 = "../c3d_feats_first/video"
destname1 = "../c3d_new/video"

for i in range(0,13000):
    if i%100==0:
        print(i)
    srcname = srcname1 + str(i) + ".npy"
    destname = destname1 + str(i) + ".npy"
    file = np.load(srcname)
    file = cut(file)
    np.save(destname,file)
