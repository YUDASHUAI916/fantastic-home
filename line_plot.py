#coding:GBK

import matplotlib.pyplot as plt	#pyplot是matplotlib的子模块
import numpy as np	#通过numpy制作数据

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(3,figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')

plt.xlim((-1, 2))		#窗口限定坐标轴范围
plt.ylim((-2, 3))
plt.xlabel("I am x")
plt.ylabel("I am y")

new_ticks = np.linspace(-1, 2, 5)		#设置新的x轴坐标
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad\ \alpha$', '$bad$', '$normal$', '$good$', '$really\ good$'])

ax = plt.gca()		#gca = get current axis
ax.spines['right'].set_color('none')		#spines = 边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))		#x轴放在y轴的-1（normal）位置上
ax.spines['left'].set_position(('data', 0))		#y轴放在x轴的0位置上

plt.show()
