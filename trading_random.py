import pandas as pd
import random
from matplotlib import rcParams

df = pd.read_csv(
        f"./rnnresult1.csv",
        names=["price", "predict"],)
real=df.price
pred=df.predict

m_ran=1000
n_ran=1000
v_ran=1000
holding_ran=[]
cash_ran=[]
value_ran=[]
for j in range(1000):
    m_ran = 1000
    n_ran = 0
    v_ran = 1000
    for i in range(len(pred)):
        a = random.randrange(0, 3, 1)
        if i>=1:
            v_ran = m_ran + n_ran * real[i-1]
            if a==1:
                if n_ran>0:
                   m_ran=real[i-1]*n_ran
                   n_ran=0
            elif a==2:
                if m_ran>0:
                    n_ran=m_ran/real[i-1]
                    m_ran=0
    value_ran.append((v_ran/1000-1)*100)

import pandas as pd  # pandas是一个强大的分析结构化数据的工具集
import numpy as np  # numpy是Python中科学计算的核心库
import matplotlib.pyplot as plt  # matplotlib数据可视化神器


def normfun(x, mu, sigma):

    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf



data = pd.DataFrame(value_ran, columns=['value'])
#data = pd.read_csv('length.csv')  # 载入数据文件
length = data['value']  # 获得长度数据集
mean = length.mean()  # 获得数据集的平均值
std = length.std()  # 获得数据集的标准差
# 设定X轴：前两个数字是X轴的起止范围，第三个数字表示步长
# 步长设定得越小，画出来的正态分布曲线越平滑
x = np.arange(-10,10, 0.01)
# 设定Y轴，载入刚才定义的正态分布函数
y = normfun(x, mean, std)
# 绘制数据集的正态分布曲线
plt.rcParams['axes.unicode_minus'] = False
rcParams['font.family'] = 'STIXGeneral'
rcParams['legend.fontsize'] = 'large'
rcParams['ytick.labelsize'] = 'large'
rcParams['axes.labelsize'] = 'large'
plt.plot(x, y)
# 绘制数据集的直方图
plt.hist(length, bins=20, rwidth=0.9, density=True)
plt.title('Net Return Distribution')
plt.xlabel('Net Return/%')
plt.ylabel('Probability')
 # 输出正态分布曲线和直方图
plt.savefig(f"./figures/random.png",dpi=450,bbox_inches = 'tight')
plt.close()


