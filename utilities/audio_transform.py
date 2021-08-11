import glob

from pydub import AudioSegment


def audioTrans(pathname):
    base_path = 'DB/External SSD for Data/Elderly Speech Recognition/contents/'
    subdir_wav = "/data/**/**.wav"
    pathlist = glob.glob(base_path + pathname + subdir_wav)
    filenames = [filename.split('/')[-1] for filename in pathlist]
    for idx, subdir in enumerate(pathlist):
        try:
            sound = AudioSegment.from_wav(subdir)
            sound = sound.set_channels(1)
            tmp = base_path + pathname + '/data_new/' + filenames[idx]
            sound.export(tmp, format='wav')
            print(f"WAV file {filenames[idx]} in {pathname} has converted into mono-data.")
        except FileNotFoundError:
            print(f"file {subdir} not found.")
        
def main():
    #audioTrans('Train_young')
    audioTrans('vali_young')
    audioTrans('Train_old')
    audioTrans('vali_old')

if __name__ == "__main__":
    main()
