import numpy as np

voice1 = np.load("E:/video-caption2/video-caption/data/voice_normalize/voice1.npy")
feats_3d = np.load("data/feats/c3d_feats/video10.npy")
feats_2d = np.load("data/train-video/video10.npy")
print("voice:"
      ,voice1.shape)
print(voice1)
print("feats_3d:",
      feats_3d.shape)
print("feats_2d:",
      feats_2d.shape)
'''
print("voice1",voice1)
print("feats_3d",feats_3d)
print("feats_2d",feats_2d)
'''