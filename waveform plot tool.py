import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 从CSV文件加载数据
data = pd.read_csv('D:/vibration-inner/1/data15.csv')

# 提取信号列的数据
signal = data['0']

# 创建时间序列
time = range(1024)

signal = np.array(signal)
sr = np.shape(signal)[0]


f = np.fft.fft(signal)
print(np.shape(f))
x = np.fft.fftfreq(len(signal),1/sr)
plt.plot(x,np.abs(f))
plt.xlim(-6000, 6000)
plt.ylim(0, 100)
plt.show()

# 绘制信号波形
plt.plot(time, signal)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Vibration Signal')
plt.show()