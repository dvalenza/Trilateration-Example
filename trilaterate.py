import math
import numpy
import turtle
import time
import matplotlib.pyplot as plt


def getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC):
    #configure plot
    fig=plt.figure(1)
    plt.axis([-100,190,-100,190])
    ax=fig.add_subplot(1,1,1)
    plt.ion()
    plt.show()   
    circa=plt.Circle((xA,yA), radius=zA, color='k', fill=False)
    circb=plt.Circle((xB,yB), radius=zB, color='k', fill=False)
    circc=plt.Circle((xC,yC), radius=zC, color='k', fill=False)
    circax=plt.Circle((xA,yA), radius=2, color='k', fill=True)
    circbx=plt.Circle((xB,yB), radius=2, color='k', fill=True)
    circcx=plt.Circle((xC,yC), radius=2, color='k', fill=True)
    ax.cla()#clears screen
    ax.add_patch(circa)
    ax.add_patch(circb)
    ax.add_patch(circc)
    ax.add_patch(circax)
    ax.add_patch(circbx)
    ax.add_patch(circcx)
    plt.draw()
    
    #calculate the center
    A1 = (-(xA)*2)
    B1 = ((xA)**2)
    C1 = (-(yA)*2)
    D1 = ((yA)**2)
    E1 = ((zA)**2)
    print A1, B1, C1, D1, E1
    
    A2 = (-(xB)*2)
    B2 = ((xB)**2)
    C2 = (-(yB)*2)
    D2 = ((yB)**2)
    E2 = ((zB)**2)
    print A2, B2, C2, D2, E2
    
    A3 = (-(xC)*2)
    B3 = ((xC)**2)
    C3 = (-(yC)*2)
    D3 = ((yC)**2)
    E3 = ((zC)**2)
    print A3, B3, C3, D3, E3
    
    print A1-A2, B1-B2, C1-C2, D1-D2, E1-E2
    A=A1-A2
    B=B1-B2
    C=C1-C2
    D=D1-D2
    E=E1-E2
    E-=B
    E-=D
    A=-A
    E=E/float(C)
    A=A/float(C)
    print "y1",A, E 
    
    
    A2=A2-A3
    B2=B2-B3
    C2=C2-C3
    D2=D2-D3
    E2=E2-E3
    E2-=B2
    E2-=D2
    A2=-A2
    E2=E2/float(C2)
    A2=A2/float(C2)
    print "y2",A2, E2 
    
    A5=E2-E
    B5=abs(A2)+A 
    x=A5/B5
    print B5,A5
    print "x=",x
    
    y=(A2*x)+E2
    print "y=",y
    
    #draw resulting point
    circd=plt.Circle((x,y), radius=2, color='b', fill=True)
    ax.text(x+5, y, "x="+str(int(x))+"\ny="+str(int(y)))

    ax.add_patch(circd)
    plt.draw()
     
    

def main():
    #starting x,y, and z(radius is the RSSI of beacon) locations of circles
    xA = 30
    yA = 130
    zA = 70
    xB = 30
    yB = 10
    zB = 80
    xC = 150
    yC = 30
    zC = 100

    #simulate movement of an object by increasing or decreasing radius of the three beacons
    for i in range(1,20):
        zA+=1
        zB-=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,20):
        zA+=1
        zB-=1
        zC+=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,20):
        zA-=1
        zB+=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,30):
        zA+=1
        zB+=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,15):
        #zA+=1
        zB+=1
        #zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,5):
        #zA+=1
        zB+=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    for i in range(1,15):
        #zA+=1
        zB+=1
        zC+=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print "i=",i
    time.sleep(40)
main()
