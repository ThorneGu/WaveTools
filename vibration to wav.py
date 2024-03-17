
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.io import wavfile
# 加载音频文件
data = pd.read_csv("D:/vibration-3classes/Inner race/data15.csv",encoding='utf-8')
signal = data['0']
signal = np.array(signal)


# 生成一个示例信号
sr = 5000  # 采样率
duration = 10  # 时长（秒）
amp = 0.5 * 32767  # 振幅（16位整数的最大值的一半）

# 将数据输出为 WAV 文件
wavfile.write('C:/Users/dell/Desktop/output.wav', sr, signal * amp)
