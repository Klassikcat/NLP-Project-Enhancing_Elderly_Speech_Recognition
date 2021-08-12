import json
import glob
import random

from tqdm.notebook import tqdm

from jamo import j2hcj, h2j
from krUtils.unicodeUtil import join_jamos

import pandas as pd
import numpy as np

import scipy.signal as signal

import tensorflow as tf
import tensorflow_io as tfio

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

class Extract_files:
    def __init__(self, dataframe, data_path, label_path):
        self.dataframe = dataframe
        self.data_path = data_path
        self.label_path = label_path

    def decode_audio(self, audio_file):
        self.audio_file = audio_file
        audio = tfio.audio.AudioIOTensor(audio_file)
        return tf.squeeze(audio[100:], axis=-1)

    def get_json(self, json_path):
        self.json_path = json_path
        with open(json_path) as json_file:
            json_data = json.load(json_file)
            data = json_data['발화정보']
            data['gender'] = json_data['녹음자정보']['gender']
            data['age'] = json_data['녹음자정보']['age']
            data['personId'] = json_data['녹음자정보']['recorderId']
            data['region'] = json_data['대화정보']['cityCode']
            data['theme'] = json_data['대화정보']['convrsThema']
        return data

    def match_json_audio(self, json_paths=None, data_size=int, gender='all', region='all', validation_set=None,
                         processed=False):
        self.json_paths = json_paths
        self.data_size = data_size
        self.gender = gender
        self.region = region
        self.validation_set = validation_set
        self.processed == processed

        dataframe = pd.DataFrame()

        if processed == False:  # json 파일 경로 수집
            json_paths = glob.glob(json_paths + subdir_json)
            json_paths = [path for path in tqdm(json_paths) if path in validation_set]  # Validation set(오디오 파일 경로)
            json_paths = [join_jamos(j2hcj(h2j(path))) for path in tqdm(json_paths)]  # 가 있는지 확인하고 추가

        elif processed == True:
            json_paths = json_paths

        else:
            raise TypeError

        random.shuffle(json_paths)

        paths = []
        for
        if region == '수도권':  # 지역별 수집
            paths = [match for match in json_paths if "수도권" in match]
        elif region == '경상':
            paths = [match for match in json_paths if "경상" in match]
        elif region == '전라':
            paths = [match for match in json_paths if "전라" in match]
        elif region == '충청':
            paths = [match for match in json_paths if "충청" in match]
        elif region == '강원':
            paths = [match for match in json_paths if "강원" in match]

        if gender == 'male':  # 성별별 수집
            matching = [match for match in paths if "_M_" in match]
        elif gender == 'female':
            matching = [match for match in paths if "_F_" in match]

        json_paths = matching[:data_size]  # 최종 수집 데이터에서 절삭

        for json_path in tqdm(json_paths):
            ax = self.get_json(json_path)
            dataframe = dataframe.append(ax, ignore_index=True)  # json file 읽은 뒤
        return dataframe

    def audio_vec(self, dataframe, types='train', age='young'):
        self.dataframe = dataframe
        self.age = age
        self.types = types
        self.age = age
        array = []
        label = []
        if types == 'train':
            if age == 'young':
                PATH = TRAIN_YOUNG
            elif age == 'old':
                PATH = TRAIN_OLD
        elif types == 'test':
            if age == 'young':
                PATH = TEST_YOUNG
            elif age == 'old':
                PATH = TEST_OLD
        for length in tqdm(range(len(dataframe))):
            try:
                array += self.files.decode_audio(PATH + DATA_PATH + '/' + dataframe['fileNm'][length].replace(
                    dataframe['scriptId'][length].split('-')[-1] + '.wav', '') + '/' + dataframe['fileNm'][length])
                label += dataframe['stt'][length]
            except:
                pass
        return array, label

    def extract_json(self, processed=False, processed_data=None, num=int, types='train', age='young',
                     validation_set=list):
        self.num = num
        self.types = types
        self.age = age
        self.processed = processed
        self.validation_set = validation_set
        self.processed_data = processed_data

        regions = ['수도권', '경상', '전라', '충청', '강원']
        genders = ['남', '여']

        target_num = int(num / len(regions) / len(genders))

        dataframe = pd.DataFrame()

        if processed == False:

            validation_set = self.MakeValiSet(validation_set)

            if types == 'train':
                if age == 'young':
                    path = self.train_young + self.label_path
                elif age == 'old':
                    path = self.train_old + self.label_path
            elif types == 'test':
                if age == 'young':
                    path = self.test_young + self.label_path
                elif age == 'old':
                    path = self.test_old + self.label_path

        else:
            path = processed_data

        for i in regions:
            print(f"age: {age}, gender=Male, region = {i} Begins")
            dfMale = self.match_json_audio(path, data_size=target_num, gender='male', region=i,
                                           validation_set=validation_set, processed=processed)
            print(f"\nSame but gender=Female")
            dfFemale = self.match_json_audio(path, data_size=target_num, gender='female', region=i,
                                             validation_set=validation_set, processed=processed)
            dataframe = dataframe.append(dfMale)
            dataframe = dataframe.append(dfFemale)

        return dataframe.sample(frac=1).reset_index(drop=True)

    def get_all_paths(self):
        Y_all_train_data = glob.glob(self.train_young + self.data_path + subdir_WAV)
        Y_all_test_data = glob.glob(self.test_young + self.data_path + subdir_WAV)
        O_all_train_data = glob.glob(self.train_old + self.data_path + subdir_WAV)
        O_all_test_data = glob.glob(self.test_old + self.data_path + subdir_WAV)
        return Y_all_train_data, Y_all_test_data, O_all_train_data, O_all_test_data

    def processed_paths(self, vali1, vali2, vali3, vali4):
        self.vali1 = vali1
        self.vali2 = vali2
        self.vali3 = vali3
        self.vali4 = vali4

        young_train_label = glob.glob(TRAIN_YOUNG + LABEL_PATH + subdir_json)
        young_vali_label = glob.glob(TEST_YOUNG + LABEL_PATH + subdir_json)
        old_train_label = glob.glob(TRAIN_OLD + LABEL_PATH + subdir_json)
        old_vali_label = glob.glob(TEST_OLD + LABEL_PATH + subdir_json)

        validation_set = self.MakeValiSet(vali1)
        young_train_label = [path for path in tqdm(young_train_label) if path in validation_set]
        young_train_label = [join_jamos(j2hcj(h2j(path))) for path in tqdm(young_train_label)]

        validation_set = self.MakeValiSet(vali2)
        young_vali_label = [path for path in tqdm(young_vali_label) if path in validation_set]
        young_vali_label = [join_jamos(j2hcj(h2j(path))) for path in tqdm(young_vali_label)]

        validation_set = self.MakeValiSet(vali3)
        old_train_label = [path for path in tqdm(old_train_label) if path in validation_set]
        old_train_label = [join_jamos(j2hcj(h2j(path))) for path in tqdm(old_train_label)]

        validation_set = self.MakeValiSet(vali4)
        old_vali_label = [path for path in tqdm(old_vali_label) if path in validation_set]
        old_vali_label = [join_jamos(j2hcj(h2j(path))) for path in tqdm(old_vali_label)]

        return young_train_label, young_vali_label, old_train_label, old_vali_label

    def MakeValiSet(self, dataframe_wav):
        return [path.replace(self.data_path, self.label_path).replace('wav', 'json') for path in tqdm(dataframe_wav)]


    def export_file(self, dataframe, path):  # Export json-dataframe to google drive
        self.dataframe = dataframe
        self.path = path
        return dataframe.to_csv(path_or_buf=path)


    def import_file(type=str, path=str):
        if type == 'colab':
            # Import json-dataframe from google drive(to re-use json dataframe when the colab disconnected)
            assert type in ['colab', 'local']
            return pd.read_csv('/content/drive/MyDrive/')
        elif type == 'local':
            return pd.read_csv(path)

        def get_path(self, types, age, filename):
            self.types = types
            self.age = age
            self.filename = filename

            if types == 'train':
                if age == 'young':
                    PATH = TRAIN_YOUNG
                elif age == 'old':
                    PATH = TRAIN_OLD
            elif types == 'test':
                if age == 'young':
                    PATH = TEST_YOUNG
                elif age == 'old':
                    PATH = TEST_OLD

            return PATH + DATA_PATH + '/' + '_'.join(filename.split('_')[:-1]) + '/' + filename


class EDA(Extract_files):
    def __init__(self):
        self.dataframe = dataframe

    def eda(self, dataframe,
            type_name, age_num,
            rate=160000):  # Extract jitter, shimmer, formants, f0-stastics, and HNR(Harmonic-to-Noise Ratio)
        self.dataframe = dataframe
        self.type_name = type_name
        self.age_num = age_num
        self.rate = rate

        tmp = pd.DataFrame()
        for audio in tqdm(dataframe['fileNm']):
            try:
                file = waves(self.get_path(filename=audio, types=type_name, age=age_num), sample_rate=rate)
                jitters = file.jitters()
                shimmers = file.shimmers()
                formants = file.formants()
                mfccs = file.f0_statistics()
                harmonicsToNoise = file.hnr()  # Calculate jitter, shimmer, formants-n and formants zero, and mfccs

                df_tmp1 = pd.DataFrame(data=jitters, index=[0])
                df_tmp2 = pd.DataFrame(data=shimmers, index=[0])
                df_tmp3 = pd.DataFrame(data=formants, index=[0])
                df_tmp4 = pd.DataFrame(data=mfccs, index=[0])
                df_tmp5 = pd.DataFrame(data=harmonicsToNoise, index=[0], columns=['Harmonic-to-noise Ratio'])

                df_tmp = pd.concat([df_tmp1, df_tmp2, df_tmp3, df_tmp4, df_tmp5], axis=1)
                tmp = pd.concat([tmp, df_tmp])
            except:
                df_tmp = pd.DataFrame(index=[0], columns=list(tmp.columns), data=[[None] * len(list(tmp.columns))])
                tmp = pd.concat([tmp, df_tmp])

        tmp = tmp.sample(frac=1).reset_index(drop=True)
        tmp_new = pd.concat([dataframe, tmp], axis=1).sample(frac=1).reset_index(drop=True)
        return tmp_new


