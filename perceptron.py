import numpy as np

def AND(x1, x2):
    w1, w2, theata = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theata:
        return 0
    elif tmp > theata:
        return 1

print("ANDゲート")
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))


# 重みとバイアスによる実装
def bias_and(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) #重み
    b = -0.7 #バイアス 
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1