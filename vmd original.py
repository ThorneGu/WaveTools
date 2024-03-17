import numpy as np
import matplotlib.pyplot as plt
from vmdpy import VMD
import pandas as pd
# -----测试信号及其参数--start-------------
Fs=1024 # 采样频率
N=1024 # 采样点数
t=np.arange(1,N+1)/N
fre_axis=np.linspace(0,Fs/2,int(N/2))

data = pd.read_csv("D:/vibration/1/data2.csv") # 测试信号
f = data['0']
# -----测试信号及其参数--end----------
# alpha 惩罚系数；带宽限制经验取值为抽样点长度1.5-2.0倍.
# 惩罚系数越小，各IMF分量的带宽越大，过大的带宽会使得某些分量包含其他分量言号;
# a值越大，各IMF分量的带宽越小，过小的带宽是使得被分解的信号中某些信号丢失该系数常见取值范围为1000~3000
alpha=2000
tau=0 # tau 噪声容限，即允许重构后的信号与原始信号有差别。
K=3 # K 分解模态（IMF）个数
DC=0 # DC 若为0则让第一个IMF为直流分量/趋势向量
init=1 # init 指每个IMF的中心频率进行初始化。当初始化为1时，进行均匀初始化。
tol=1e-7 # 控制误差大小常量，决定精度与迭代次数
u, u_hat, omega = VMD(f, alpha, tau, K, DC, init, tol) # 输出U是各个IMF分量，u_hat是各IMF的频谱，omega为各IMF的中心频率

# 1 画原始信号和它的各成分
plt.figure(figsize=(10,7));plt.subplot(K+1, 1, 1);plt.plot(t,f)
plt.suptitle('Original input signal and its components');plt.show()

# 2 分解出来的各IMF分量
plt.figure(figsize=(10,7))
plt.plot(t,u.T);plt.title('all Decomposed modes');plt.show()  # u.T是对u的转置
for imf in u:
    plt.plot(imf)
    plt.show()

# 3 各IMF分量的fft幅频图
plt.figure(figsize=(10, 7), dpi=80)
for i in range(K):
    plt.subplot(K, 1, i + 1)
    fft_res=np.fft.fft(u[i, :])
    plt.plot(fre_axis,abs(fft_res[:int(N/2)])/(N/2))
    plt.title('(FFT) amplitude frequency of IMF {}'.format(i + 1))
plt.show()

# 4 分解出来的各IMF分量的频谱
# print(u_hat.shape,t.shape,omega.shape)
plt.figure(figsize=(10, 7), dpi=80)
for i in range(K):
    plt.subplot(K, 1, i + 1)
    plt.plot(fre_axis,abs(u_hat[:, i][int(N/2):])/(N/2))
    plt.title('(VMD)amplitude frequency of the modes{}'.format(i + 1))
plt.tight_layout();plt.show()

# 5 各IMF的中心频率
plt.figure(figsize=(12, 7), dpi=80)
for i in range(K):
    plt.subplot(K, 1, i + 1)
    plt.plot(omega[:,i]) # X轴为迭代次数，y轴为中心频率
    plt.title('mode center-frequencies{}'.format(i + 1))
plt.tight_layout();plt.show()

plt.figure(figsize=(10,7))
plt.plot(t,np.sum(u,axis=0))
plt.title('reconstructed signal')
