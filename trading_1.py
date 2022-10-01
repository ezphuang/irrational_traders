import pandas as pd
import random

df = pd.read_csv(
        f"./rnnresult1.csv",
        names=["price", "predict"],)
real=df.price
pred=df.predict
m=1000
m_hold=1000


n=0
n_hold=0


val=1000
v_hold=1000


holding=[]

cash=[]

value=[]
value_hold=[]


v=0.5
u=0.5


#naive
for i in range(len(pred)):
    value.append(val/1000-1)
    a=0
    if i>=1:
        if pred[i] < real[i - 1]:
            a=1
        elif pred[i] > real[i - 1]:
            a=2
        val = m + n * real[i-1]
        if a ==1:
            if n>0:
                m=m+real[i-1]*n*u
                n=n*(1-u)
        if a ==2:
            if m>0:
                n=n+m*v/real[i-1]
                m=m*(1-v)
    holding.append(n)
    cash.append(m)

#buy and hold
for i in range(len(pred)):
    if i == 1:
        v_hold = m_hold + n_hold * real[i - 1]
        n_hold=m_hold/real[i - 1]
        m_hold=0
    elif i>1:
        v_hold = m_hold + n_hold * real[i - 1]
    value_hold.append(v_hold/1000-1)

