import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa.display

# 读取csv文件并转换为numpy数组格式
df = pd.read_csv('C:/Users/dell/Desktop/HSB1/12.13/2023-12-13 05_32_31.csv')
data = np.array(df.iloc[:, 0])

# 计算stft矩阵
D = librosa.stft(data,n_fft=2046, hop_length=512, win_length=None, window='hann', center=True, pad_mode='reflect')

# 计算lofar时频谱图
lofar = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# 绘制lofar时频谱图
plt.figure(figsize=(8, 4))
librosa.display.specshow(lofar, y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Lofar spectrogram')
plt.ylim(0, 500)
plt.tight_layout()
plt.show()