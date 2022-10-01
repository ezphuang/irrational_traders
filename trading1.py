import pandas as pd
import random

df = pd.read_csv(
        f"./rnnresult1.csv",
        names=["price", "predict"],)
real=df.price
pred=df.predict
m=1000
m_hold=1000
m_ran=1000
m_s1=1000
m_s2=1000
m_s0=1000
m_s4=1000
n=0
n_hold=0
n_ran=0
n_s1=0
n_s0=0
n_s4=0
val=1000
v_hold=1000
v_ran=1000
v_s1=1000
v_s0=1000
v_s4=1000
holding=[]
holding_ran=[]
holding_s1=[]
holding_s0=[]
cash=[]
cash_ran=[]
cash_s1=[]
cash_s0=[]
value=[]
value_hold=[]
value_ran=[]
value_s1=[]
value_s0=[]
value_s4=[]
v=0.5
u=0.5
b=1
#naive-without predicton
for i in range(len(pred)):
    value_s0.append(v_s0/1000-1)
    a=0
    if i>=2:
        if real[i-1] < real[i - 2]:
            a=1
        elif real[i-1] > real[i - 2]:
            a=2
        v_s0 = m_s0 + n_s0 * real[i-1]
        if a ==1:
            if n>0:
                m_s0=m_s0+real[i-1]*n_s0*u
                n=n*(1-u)
        if a ==2:
            if m_s0>0:
                n_s0=n_s0+m_s0*v/real[i-1]
                m_s0=m_s0*(1-v)
    holding.append(n_s0)
    cash.append(m_s0)

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
#random
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
    holding_ran.append(n_ran)
    cash_ran.append(m_ran)
    value_ran.append(v_ran/1000-1)
#trust
for i in range(len(pred)):
    value_s1.append(v_s1/1000-1)
    a=999
    t=999
    if i>=2:
        if pred[i-1] < real[i - 2] and real[i-1] < real[i - 2]:
            t=1
        elif pred[i-1] > real[i - 2] and real[i-1] > real[i - 2]:
            t=1
        elif pred[i-1] == real[i - 2] and real[i-1] == real[i - 2]:
            t=1
        else:
            t=0

    if i>=2:
        if pred[i] < real[i - 1] and t==1:
            a=1
        elif pred[i] > real[i - 1] and t==1:
            a=2
        else:
            a=0
        v_s1 = m_s1 + n_s1 * real[i-1]
        if a ==1:
            if n_s1>0:
                m_s1=m_s1+real[i-1]*n_s1*u
                n_s1=n_s1*(1-u)
        if a ==2:
            if m_s1>0:
                n_s1=n_s1+m_s1*u/real[i-1]
                m_s1=m_s1*(1-u)
    holding_s1.append(n_s1)
    cash_s1.append(m_s1)

#Conceide
for j in range(5):
    value_s4=[]
    v_s4=1000
    m_s4=1000
    n_s4=0
    for i in range(len(pred)):
        value_s4.append(v_s4/1000-1)
        a=999
        t=999
        if i>=2:
            if pred[i-1] < real[i - 2] and real[i-1] < real[i - 2]:
                t=1
            elif pred[i-1] > real[i - 2] and real[i-1] > real[i - 2]:
                t=1
            elif pred[i-1] == real[i - 2] and real[i-1] == real[i - 2]:
                t=1
            else:
                t=0

        if i>=2:
            if pred[i] < real[i - 1] and t==1:
                a=1
            elif pred[i] > real[i - 1] and t==1:
                a=2
            else:
                a=random.randrange(0, 3, 1)
            v_s4 = m_s4 + n_s4 * real[i-1]
            if a ==1:
                if n_s4>0:
                    m_s4=m_s4+real[i-1]*n_s4*u
                    n_s4=n_s4*(1-u)
            if a ==2:
                if m_s4>0:
                    n_s4=n_s4+m_s4*u/real[i-1]
                    m_s4=m_s4*(1-u)
    locals()[f'ce_{j}']= pd.Series(value_s4)


##smart error
m_s3 = 1000
n_s3 = 0
v_s3 = 1000
holding_s3 = []
cash_s3 = []
value_s3 = []


stop=0
for i in range(len(pred)):
    value_s3.append(v_s3/1000-1)
    t=999
    a=999
    if i>=2 and stop==0:
        if abs(pred[i-1] - real[i -2])/real[i -2] <= 0.009:
            t=1
        else:
            t=3
            stop=1
    elif i>=2 and stop!=0:
         if abs(pred[i-1] - real[i -1])/real[i -1] <= 0.009:
            stop=stop-1
            t=1
         else:
            t=3
    if i>=2:
        if pred[i] < real[i - 1] and t==1 :
            a=1
        elif pred[i] > real[i - 1] and t==1:
            a=2
        else:
            a=0
        v_s3 = m_s3 + n_s3 * real[i-1]
        if a ==1:
            if n_s1>0:
                m_s3=m_s3+real[i-1]*n_s3*u
                n_s3=n_s3*(1-u)
        elif a ==2:
            if m_s1>0:
                n_s3=n_s3+m_s3*v/real[i-1]
                m_s3=m_s3*(1-v)
        elif t ==3:
            if n_s1 > 0:
                m_s3 = m_s3 + real[i - 1] * n_s3*b
                n_s3 = n_s3*(1-b)
    holding_s3.append(n_s3)
    cash_s3.append(m_s3)



import matplotlib.pyplot as plt
from matplotlib import rcParams


plt.rcParams['axes.unicode_minus'] = False
rcParams['font.family'] = 'STIXGeneral'

an = pd.Series(value)    #naive
a0 = pd.Series(value_s0)
ah = pd.Series(value_hold)
a1 = pd.Series(value_s1) #trust
a2 = pd.Series(value_s3) #smart


#plt.plot(ce_0, label="Conceited 1", color="green",ls='--')
#plt.plot(ce_1, label="Conceited 2", color="green",ls='--')
#plt.plot(ce_2, label="Conceited 3", color="green",ls='--')
#plt.plot(ce_3, label="Conceited 4", color="green",ls='--')
#plt.plot(ce_4, label="Conceited 5", color="green",ls='--')

plt.plot(ah, label="Buy and Hold", color="grey",ls='--')
plt.plot(an, label="Naive with Prediction", color="green")
#plt.plot(a0, label="Naive without Prediction", color="red")
plt.plot(a1, label="Drift with Tide", color="blue")
#plt.plot(a2, label="Expert", color="orange")
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.xlabel("Trading Period")
plt.ylabel("Net Profit")
plt.title(f" ")
plt.savefig(f"./figures/t5.png",dpi=450,bbox_inches = 'tight')
plt.show()












