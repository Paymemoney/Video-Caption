from pydub import AudioSegment
import os
import sys

path = os.getcwd()

def file_exists(file_path):
    if os.path.isfile(os.path.join(path,file_path)):
        return os.path.join(path,file_path)
    elif os.path.isfile(file_path):
        return file_path
    else:
        return False

def convert_video(file_path):
    wav_filename = os.path.splitext(os.path.basename(file_path))[0] + '.wav'
    AudioSegment.from_file(file_path).export(".\\data\\voice\\"+wav_filename, format='wav')

if __name__ == '__main__':
    #file_path = file_exists(sys.argv[1])
    for i in range(0,10000):
        file_path = ".\data\\videos\\video{0}.mp4".format(i)
        try:
            convert_video(file_path)
        except:
            print(i)
        if(i%100==0):
            print(i)
