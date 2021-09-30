import numpy as np
import matplotlib.pylab as plt 

# シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1) # -5.0~5.0を0.1刻みでnumpy 配列生成
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y軸の範囲指定
plt.show()