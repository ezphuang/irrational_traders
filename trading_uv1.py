import pandas as pd
import random

df = pd.read_csv(
        f"./rnnresult1.csv",
        names=["price", "predict"],)
real=df.price
pred=df.predict
m=1000
n=0

val=1000

holding=[]

cash=[]

value=[]

v=1
u=0
for i in range(len(pred)):
    value.append(val)
    a=0
    t = 1
    if i >= 2:
        if pred[i - 1] < real[i - 2] and real[i - 1] < real[i - 2]:
            t == 1
        if pred[i - 1] > real[i - 2] and real[i - 1] > real[i - 2]:
            t == 1
        if pred[i - 1] == real[i - 2] and real[i - 1] == real[i - 2]:
            t == 1
        else:
            t == 0

        if i>=1:
            if pred[i] < real[i - 1]  and t==1:
                a=1
            elif pred[i] > real[i - 1] and t==1:
                a=2
            val = m + n * real[i - 1]
            if a == 1:
                if n>0:
                    m=m+real[i-1]*n*u
                    n=n*(1-u)
            if a == 2:
                if m>0:
                    n = n + (m * v)/real[i-1]
                    print(m)
                    print(v)
                    print((m * v)/real[i-1])
                    m=m*(1-v)
                    print((1-v))
    holding.append(n)
    cash.append(m)