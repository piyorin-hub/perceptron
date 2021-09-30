import numpy as np
import matplotlib.pylab as plt 

# ステップ関数
def step_func(x):
    # xの配列の各要素に対し、ステップ関数を実行、boolからintへ直す
    
    return np.array(x > 0, dtype=np.int)


# シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1) # -5.0~5.0を0.1刻みでnumpy 配列生成

y1 = step_func(x)
plt.plot(x, y1)
plt.ylim(-0.1, 1.1) #y軸の範囲指定

y2 = sigmoid(x)
plt.plot(x, y2)
plt.ylim(-0.1, 1.1) #y軸の範囲指定

plt.show()

