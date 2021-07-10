# ***Enhancing Korean Elderly Speech Recognition using Transfer Learning, CNN***

## 문제의식
1. 노인들의 디지털 소외는 이동권과 같은 기본권에도 영향을 미칠 수 있음.
2. 노인들의 디지털 소외 원인 중 하나는 기기 이용방법에 대한 심리적 부담감.
3. 음성인식이라는 쉬운 조작법을 통해 기기 이용에 대한 심리적 부담을 줄여 노인의 이동권과 같은 기본권을 보장할 수 있음.
4. 그러나 노인들의 음성 데이터는 부족하고, 현재 대부분의 모델이 청년 남녀에 맞춰줌.
5. 노인 음성인식률은 평균 연령대의 성인남녀 음성인식률에 비해 약 20%정도 낮음

## Problem awareness
1. Digital alienation of elders would critically violate fundamental rights such as violation of the right to mobility
2. One of the causes of this alienation is the psychological uncomfortableness of how to use cutting-edge devices such as mobile phones.
3. Service providers can secure these rights by providing voice recognition services that are much easier to use.
4. However, most Auto Speech Recognition models fit only youth adults' voice data since elders' voice data is scarce.
5. For these reasons, the recognition rate of elders' voices on the existing model is 20 percent lower than youth adults' voice recognition rate.

## Stack
1. Python 3
2. Tensorflow.Keras
3. Scikit-learn
4. matplotlib
5. seaborn
6. pandas
7. numpy

## Prior research review
<a href="https://drive.google.com/file/d/17soL9L7CqMF4sI-pPxCOhN2IqwyoxrhG/view?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a> - Korean

1. Due to the reduced range, persistence, and thickness of tongue movements, the speaking style of older people is characterized by slower speech speed, increased speech intensity, increased silence, and higher pronunciation inaccuracies.
2. Also, its voice characterized as higher harmonic-to-noise ratio(HNR)

## Algorithm
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcUS1cn%2Fbtq8wKuDKQd%2FvyMTirbz1pN94R7kOhwtbk%2Fimg.png">

1. Transfer learning and fine-tuning is used in this project to utilize scarce target data
2. Convolutional Neural Network(CNN) is also used to reduce HNR, which is one of the elder voice's characteristic.
3. Softmax will be used as hidden unit k, j, m's activation function.
4. CTC/attention hybrid Loss function will be used as loss function.

## Dataset
1. BASELINE: 한국 음성 데이터셋(Korean Voice Dataset) built by 한국전자통신연구원(ETRI): Consist of youth male data of 923 people, youth female data of 1077 people. total 1000 hours.
2. Elder Dataset: 자유대화 음성(노인남녀) built by NHN Diquest: Consists of elder male data of 500 people, elder female data of 500 people. total 3000 hours of Gyeonggi/Chungcheong/Gangwon/Jeolla/Jeju/Etc.
