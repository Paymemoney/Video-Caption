import matplotlib
from sklearn import preprocessing
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy, scipy, librosa, audioread, wave
import librosa.display
import sys, os


def showmfcc(wavpath,i):
    t, spe = librosa.load(wavpath)
    mfccs = librosa.feature.mfcc(t, sr=spe)
    name = "E:/video-caption2/video-caption/data/voice_mfcc/video"+str(i)+".npy"
    numpy.save(name, mfccs)


def decode2wav(srcname, outname):
    f = audioread.audio_open(filename)
    nsample = 0
    for buf in f:
        nsample += 1
    f.close()
    with audioread.audio_open(filename) as f:
        print("input file: channels=%d, samplerate=%d, duration=%d" % (f.channels, f.samplerate, f.duration))
        channels = f.channels
        samplewidth = 2
        samplerate = f.samplerate
        compresstype = "NONE"
        compressname = "not compressed"
        outwav = wave.open(outname, 'wb')
        outwav.setparams((channels, samplewidth, samplerate, nsample, compresstype, compressname))
        for buf in f:
            outwav.writeframes(buf)
        outwav.close()


def pcm2wav(srcname, outname, channels, samplewidth, samplerate):
    fs = os.path.getsize(srcname)
    nsample = fs / samplewidth
    outwav = wave.open(outname, 'wb')
    outwav.setparams((channels, samplewidth, samplerate, nsample, "NONE", "not cmopressed"))
    fsrc = open(srcname, 'rb')
    outwav.writeframes(fsrc.read())
    fsrc.close()
    outwav.close()

def Normalize(data):
    m = numpy.mean(data)
    mx = numpy.max(data)
    mn = numpy.min(data)
    return [(float(i) - m) / (mx - mn) for i in data]

if __name__ == '__main__':
    for i in range(0,10000):
        if i%100 ==0:
            print(i)
        filename = "E:/video-caption2/video-caption/data/voice_normalize/voice"+str(i)+".npy"
        c3d_feats = "E:/video-caption2/video-caption/data/feats/c3d_feats/video"+str(i)+".npy"
        if os.path.exists(filename):
            voice = numpy.load(filename)
            video = numpy.load(c3d_feats)
            #print(numpy.shape(voice),numpy.shape(video))
            voice = numpy.concatenate((voice,video))
            #print(numpy.shape(voice))
            numpy.save("E:/video-caption2/video-caption/data/feats/c3d_feats_voice/video"+str(i)+".npy",voice)