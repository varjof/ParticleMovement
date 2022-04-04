# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:23:49 2020

@author: John
"""
import matplotlib.pyplot as plt

g=9.8
m=1
k=0.1
dt=0.1

#Condiciones iniciales
t=0
xo=10
yo=10
vxo=10
vyo=0


x=xo
y=yo
vx=vxo
vy=vyo

bola,=plt.plot(x,y,'o')

plt.axis([0,20,0,20])
plt.grid()

for i in range(120):
    t=t+dt
    vx=(-k/m*vx*dt)+vx
    vy=((-k/m*vy-g)*dt)+vy
    x=vx*dt+x
    y=vy*dt+y
    if vy*dt+y<0 or vy*dt+y>20:
        vy=-vy
    if vx*dt+x>20:
        vx=-vx
    if vx*dt+x<0:
        vx=-vx

    bola.set_xdata(x)
    bola.set_ydata(y)
    plt.pause(0.1)
    
    
    
    
