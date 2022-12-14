import pandas as pd
import random
from matplotlib import pyplot as plt

import numpy as np
from mpl_toolkits.mplot3d import Axes3D



df = pd.read_csv(
        f"./rnnresult1.csv",
        names=["price", "predict"],)
real=df.price
pred=df.predict

m_s1=1000
n_s1=0
v_s1=1000

value_final=[]
uu=[]
vv=[]
SD=[]

for u in range(0,100,1):
    u=u/100
    for v in range(0,100,1):
        v=v/100
        m_s1 = 1000
        n_s1 = 0
        v_s1 = 1000
        holding_s1 = []
        cash_s1 = []
        value_s1 = []
        for i in range(len(pred)):
            value_s1.append(v_s1)
            a=0
            if i>=2:
                if pred[i] < real[i - 1] :
                    a=1
                elif pred[i] > real[i - 1]:
                    a=2
                else:
                    a=0
                v_s1 = m_s1 + n_s1 * real[i-1]
                if a ==1:
                    if n_s1>0:
                        m_s1=m_s1+real[i-1]*n_s1*u
                        n_s1=n_s1*(1-u)
                elif a ==2:
                    if m_s1>0:
                        n_s1=n_s1+m_s1*v/real[i-1]
                        m_s1=m_s1*(1-v)

            holding_s1.append(n_s1)
            cash_s1.append(m_s1)
        g=(v_s1/1000)-1
        std = np.array(value_s1).std()
        uu.append(u)
        vv.append(v)
        value_final.append(g)
        SD.append(std)
        print((u,v,g))


df1=pd.DataFrame({'X': uu, 'Y': vv, 'Z': value_final,'D':SD})
df1.to_csv('uv.csv')
fig = plt.figure()
ax = fig.gca(projection='3d')
surf=ax.plot_trisurf(df1['Y'], df1['X'], df1['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)

ax.set_xlabel("xlabel")
ax.set_ylabel("ylabel")
ax.set_zlabel("z")

plt.show()  # 展示图片











