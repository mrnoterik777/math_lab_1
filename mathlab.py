import numpy as np
import matplotlib.pyplot as plt
import math
import json
from random import randint
from random import uniform as random


def y(x):
    return [math.cos(2*y) for y in x]

def E(a,b,t):
    return [round(x/10**t,t) for x in range(int(a*(10**t)),int(b*10**t)+1)]

def func(x,y):
    plt.plot(x, y, color="red")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y=cos(2x) на отрезке [0, pi]')
    plt.grid(True)

def list_of_n(x,n):
    s=np.array_split(x,n)
    t=[s[0][0]]
    for i in s:
        t.append(i[-1])
    return t

def figure_with_Darbu(x,y,n,choise):
    #func(x,y)
    #plt.savefig("cos2x.png")
    
    func(x,y)   
    result=0
    s=list_of_n(x,n)
    if choise==1:
        down_sum_of_Darbu=0    
        for i in range(len(s)-1):
            h=min(math.cos(2*s[i]),math.cos(2*s[i+1]))
            if s[i]<math.pi/2 and math.pi/2<s[i+1]:
                h=min(y)
            plt.fill_between([s[i],s[i+1]], h, color="skyblue",  alpha=0.7)
            down_sum_of_Darbu+=(s[i+1]-s[i])*h
        plt.title(f"y=cos(2x) на [0,pi]\nНижняя сумма Дарбу при n={n}")
       # plt.savefig(f"cos2x_with_down_Darbu(n={n}).png")
        if show==False:
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()
        elif show==True:
            plt.show()
            plt.clf()
        
        func(x,y)
        result=down_sum_of_Darbu
    elif choise==2:
        up_sum_of_Darbu=0

        for i in range(len(s)-1):
            h=max(math.cos(2*s[i]),math.cos(2*s[i+1]))
            plt.fill_between([s[i],s[i+1]], h, color="skyblue",  alpha=0.7)
            up_sum_of_Darbu+=(s[i+1]-s[i])*h
        plt.title(f"y=cos(2x) на [0,pi]\nВерхняя сумма Дарбу при n={n}")
        #plt.savefig(f"cos2x_with_up_Darbu(n={n}).png")
        if show==False:
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()
        elif show==True:
            plt.show()
            plt.clf()
        
        result=up_sum_of_Darbu
    elif choise==3:
        sum_under_figure=0
        for i in range(len(s)-1):
            h=math.cos((s[i]+s[i+1]))
            plt.fill_between([s[i],s[i+1]], h, color="skyblue",  alpha=0.7)
            sum_under_figure+=(s[i+1]-s[i])*h
        plt.title(f"y=cos(2x) на [0,pi]\nСреднее оснащение при n={n}")
        #plt.savefig(f"cos2x_with_sr_osn(n={n}).png")
        if show==False:
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()
        elif show==True:
            plt.show()
            plt.clf()
        
        result=sum_under_figure
    elif choise==4:
        sum_under_figure=0
        for i in range(len(s)-1):
            h=math.cos(2*(random(s[i],s[i+1])))
            plt.fill_between([s[i],s[i+1]], h, color="skyblue",  alpha=0.7)
            sum_under_figure+=(s[i+1]-s[i])*h
        plt.title(f"y=cos(2x) на [0,pi]\nСлучайное оснащение при n={n}")
       # plt.savefig(f"cos2x_with_sr_osn(n={n}).png")
        if show==False:
            plt.show(block=False)
            plt.pause(0.001)
            plt.clf()
        elif show==True:
            plt.show()
            plt.clf()
        result=sum_under_figure
    else:
        print("Неверное значение оснащения!")
        exit()

    print(f"Сумма под графиком при n={n}: {result}")

    return result


N=list(map(str,input("Выберите способ разбиений n:\nВручную - введите значения через запятую\nСлучайно - оставьте поле пустым\nПо возрастанию введите '-'\nВвод:").split(",")))
choise=int(input("Выберите способ оснащения:\n1.Нижние\n2.Верхние\n3.Средние\n4.Случайные\nВвод:"))
flag=0
global show
show=True
if len(N)==1 and N[0]=='':
    N[0]=randint(2,100)
elif N[0]=="-" and len(N)==1:
    N=[i for i in range(2,101)]
    flag=len(N)
    show=False
else:
    N=[int(x) for x in N]
a,b=0,np.pi
if max(N)>1000:
    t=len(str(max(N)))
else:
    t=3
x=E(a,b,t)# область определения
fy=y(x)
result=[]
for n in N[:-1]:
    result.append(figure_with_Darbu(x,fy,n, choise))
show=True
result.append(figure_with_Darbu(x,fy,N[-1], choise))
if flag!=0:
    plt.plot([x for x in range(flag)],result)
    plt.show(block=False)
    plt.pause(0.001)
    
