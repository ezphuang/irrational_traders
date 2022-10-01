import pandas as pd
import random
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib import rcParams

plt.rcParams['axes.unicode_minus'] = False
rcParams['font.family'] = 'STIXGeneral'
rcParams['legend.fontsize'] = 'large'
rcParams['ytick.labelsize'] = 'large'
rcParams['axes.labelsize'] = 'large'
df = pd.read_csv(
        f"./uv_error.csv",
        names=['X','Y','Z','D'],)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=cm.coolwarm, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, orientation='horizontal')

ax.set_ylabel("Buy")
ax.set_xlabel("Sell")
ax.set_zlabel("z")
plt.savefig(f"./figures/return.png",dpi=450,bbox_inches = 'tight')


fig1 = plt.figure()
ax = fig1.gca(projection='3d')
surf=ax.plot_trisurf(df['Y'], df['X'], df['D'], cmap=plt.cm.viridis, linewidth=0.2)
fig1.colorbar(surf, shrink=0.5, orientation='horizontal')
ax.set_ylabel("Buy")
ax.set_xlabel("Sell")
ax.set_zlabel("Standard Deviation")
plt.savefig(f"./figures/std.png",dpi=450,bbox_inches = 'tight')
plt.show()  # 展示图片

from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

