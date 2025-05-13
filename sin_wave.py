import numpy as np
import matplotlib.pyplot as plt

# 0から2πまでを100等分したデータを作成
x = np.linspace(0, 2 * np.pi, 100)

# xのサイン値を計算
y = np.sin(x)

# グラフの作成
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

# グラフを画面に表示
plt.show()
