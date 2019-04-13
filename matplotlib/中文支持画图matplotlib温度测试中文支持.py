from matplotlib import pyplot as plt
import random


#中文支持matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）


a = [random.randint(20,25) for i in range(120)]
plt.figure(figsize=(12,8),dpi=90)
plt.plot(range(120),a)

#调整x轴的刻度
x_t = ['10点{}分'.format(i) for i in range(60)]
x_t += ['11点{}分'.format(i) for i in range(60)]

#设置x刻度并旋转角度
plt.xticks(range(1,120,3),x_t,rotation=85)

#x,y轴的标签
plt.xlabel('时间,')
plt.ylabel('温度,')
plt.title("sfsa")



plt.show()