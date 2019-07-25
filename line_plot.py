#coding:GBK

import matplotlib.pyplot as plt	#pyplot��matplotlib����ģ��
import numpy as np	#ͨ��numpy��������

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(3,figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')

plt.xlim((-1, 2))		#�����޶������᷶Χ
plt.ylim((-2, 3))
plt.xlabel("I am x")
plt.ylabel("I am y")

new_ticks = np.linspace(-1, 2, 5)		#�����µ�x������
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad\ \alpha$', '$bad$', '$normal$', '$good$', '$really\ good$'])

ax = plt.gca()		#gca = get current axis
ax.spines['right'].set_color('none')		#spines = �߿�
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))		#x�����y���-1��normal��λ����
ax.spines['left'].set_position(('data', 0))		#y�����x���0λ����

plt.show()
