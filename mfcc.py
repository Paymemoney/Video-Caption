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
    name = "E:/video-caption2/video-caption/data/voice_test_mfcc/video"+str(i)+".npy"
    numpy.save(name, mfccs)


def decode2wav(filename, outname):
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
    return [[(float(data[i][j]) - m) / (mx - mn) for i in range(data.shape[0])]for j in range(data.shape[1])]

def reps(data):
    length = numpy.size(data)
    #print(length)
    if length%2048!=0:
        a = numpy.zeros((1,2048-length % 2048))
        #print(numpy.shape(data), numpy.shape(a))
        data = numpy.concatenate((data,a),axis=1)
    return data

if __name__ == '__main__':
    for i in range(12000,13000):
        if i%100 ==0:
            print(i)
        '''
        #mfcc提取
        file_path = ".\data\\voice_test\\video{0}.wav".format(i)
        showmfcc(file_path,i)
        '''
        filename = "./data/voice_test_mfcc/video"+str(i)+".npy"
        c3d_feats = "./data/feats/c3d_feats_first/video"+str(i)+".npy"
        if os.path.exists(filename):
            voice = numpy.load(filename)
            voice = Normalize(voice)
            voice = numpy.array(voice)
            video = numpy.load(c3d_feats)
            #print(numpy.shape(voice),numpy.shape(video))
            voice = voice.reshape(1, -1)
            voice = reps(voice)
            voice = voice.reshape(-1, 2048)
            #print(numpy.shape(voice),numpy.shape(video))
            voice = numpy.concatenate((voice,video))
            #print(numpy.shape(voice))
            numpy.save("E:/video-caption2/video-caption/data/feats/c3d_feats/video"+str(i)+".npy",voice)
        