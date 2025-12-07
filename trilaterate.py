import math
import numpy
import turtle
import time
import matplotlib
matplotlib.use('TkAgg')  # Force TkAgg backend
import matplotlib.pyplot as plt


def getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC):
    """
    TRILATERATION ALGORITHM - Mathematical Explanation:
    
    Given three beacons at known positions (xA,yA), (xB,yB), (xC,yC) with
    measured distances zA, zB, zC to an unknown target point (x,y):
    
    Each beacon defines a circle: (x-xA)² + (y-yA)² = zA²
    The target is at the intersection of all three circles.
    
    We solve by converting to linear equations:
    Circle equations: x² - 2xA*x + xA² + y² - 2yA*y + yA² = zA²
    Rearranging: x² + y² - 2xA*x - 2yA*y = zA² - xA² - yA²
    
    Subtracting pairs eliminates x² + y² terms, giving linear system
    that can be solved for x and y coordinates.
    """
    #configure plot
    fig=plt.figure(1)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlim([-100,190])
    ax.set_ylim([-100,190])
    
    # Create circles
    circa=plt.Circle((xA,yA), radius=zA, color='r', fill=False, linewidth=2)
    circb=plt.Circle((xB,yB), radius=zB, color='g', fill=False, linewidth=2)
    circc=plt.Circle((xC,yC), radius=zC, color='b', fill=False, linewidth=2)
    circax=plt.Circle((xA,yA), radius=2, color='r', fill=True)
    circbx=plt.Circle((xB,yB), radius=2, color='g', fill=True)
    circcx=plt.Circle((xC,yC), radius=2, color='b', fill=True)
    
    # Add circles to plot
    ax.add_patch(circa)
    ax.add_patch(circb)
    ax.add_patch(circc)
    ax.add_patch(circax)
    ax.add_patch(circbx)
    ax.add_patch(circcx)
    plt.draw()
    
    # STEP 1: Convert circle equations to standard form
    # Each circle: (x-xi)² + (y-yi)² = ri²
    # Expanded: x² + y² - 2xi*x - 2yi*y + xi² + yi² = ri²
    # Rearranged: x² + y² - 2xi*x - 2yi*y = ri² - xi² - yi²
    # Standard form: x² + y² + Ai*x + Ci*y = Ei - Bi - Di
    # Where: Ai = -2xi, Bi = xi², Ci = -2yi, Di = yi², Ei = ri²
    
    # Coefficients for beacon A
    A1 = (-(xA)*2)  # -2*xA coefficient for x term
    B1 = ((xA)**2)  # xA² constant term  
    C1 = (-(yA)*2)  # -2*yA coefficient for y term
    D1 = ((yA)**2)  # yA² constant term
    E1 = ((zA)**2)  # zA² distance squared
    print(A1, B1, C1, D1, E1)
    
    # Coefficients for beacon B
    A2 = (-(xB)*2)  # -2*xB coefficient for x term
    B2 = ((xB)**2)  # xB² constant term
    C2 = (-(yB)*2)  # -2*yB coefficient for y term  
    D2 = ((yB)**2)  # yB² constant term
    E2 = ((zB)**2)  # zB² distance squared
    print(A2, B2, C2, D2, E2)
    
    # Coefficients for beacon C
    A3 = (-(xC)*2)  # -2*xC coefficient for x term
    B3 = ((xC)**2)  # xC² constant term
    C3 = (-(yC)*2)  # -2*yC coefficient for y term
    D3 = ((yC)**2)  # yC² constant term
    E3 = ((zC)**2)  # zC² distance squared
    print(A3, B3, C3, D3, E3)
    
    # STEP 2: Create linear system by subtracting circle equations
    # Equation A - Equation B eliminates x² + y² terms:
    # (A1-A2)*x + (C1-C2)*y = (E1-B1-D1) - (E2-B2-D2)
    # Simplifying: (A1-A2)*x + (C1-C2)*y = (E1-E2) - (B1-B2) - (D1-D2)
    
    print(A1-A2, B1-B2, C1-C2, D1-D2, E1-E2)
    A=A1-A2      # Coefficient of x in first linear equation
    B=B1-B2      # xA² - xB² term
    C=C1-C2      # Coefficient of y in first linear equation  
    D=D1-D2      # yA² - yB² term
    E=E1-E2      # zA² - zB² term
    E-=B         # Subtract (xA² - xB²) from right side
    E-=D         # Subtract (yA² - yB²) from right side
    A=-A         # Make coefficient positive for easier solving
    
    # Convert to slope-intercept form: y = mx + b
    # From Ax + Cy = E, we get y = (-A/C)x + (E/C)
    E=E/float(C) # y-intercept of first line
    A=A/float(C) # slope of first line (note: A is now -A/C)
    print("y1",A, E )
    
    
    # STEP 3: Create second linear equation (B - C)
    # Equation B - Equation C also eliminates x² + y² terms:
    # (A2-A3)*x + (C2-C3)*y = (E2-B2-D2) - (E3-B3-D3)
    
    A2=A2-A3     # Coefficient of x in second linear equation
    B2=B2-B3     # xB² - xC² term
    C2=C2-C3     # Coefficient of y in second linear equation
    D2=D2-D3     # yB² - yC² term
    E2=E2-E3     # zB² - zC² term
    E2-=B2       # Subtract (xB² - xC²) from right side
    E2-=D2       # Subtract (yB² - yC²) from right side
    A2=-A2       # Make coefficient positive
    
    # Convert second equation to slope-intercept form: y = mx + b
    # From A2x + C2y = E2, we get y = (-A2/C2)x + (E2/C2)
    E2=E2/float(C2) # y-intercept of second line
    A2=A2/float(C2) # slope of second line (note: A2 is now -A2/C2)
    print("y2",A2, E2 )
    
    # STEP 4: Find intersection of two lines
    # Line 1: y = A*x + E  (slope A, y-intercept E)
    # Line 2: y = A2*x + E2 (slope A2, y-intercept E2)
    # Set equal: A*x + E = A2*x + E2
    # Solve for x: (A2-A)*x = E-E2
    # Therefore: x = (E-E2)/(A2-A)
    
    A5=E2-E        # Difference in y-intercepts (E2-E)
    B5=abs(A2)+A   # Difference in slopes |A2-A| (using abs for numerical stability)
    x=A5/B5        # x-coordinate of intersection point
    print(B5,A5)
    print("x=",x)
    
    # Substitute x back into either line equation to get y
    # Using line 2: y = A2*x + E2
    y=(A2*x)+E2    # y-coordinate of intersection point
    print("y=",y)
    
    # STEP 5: Visualize the solution
    # The calculated (x,y) point is where all three circles intersect
    # This represents the estimated position of the target object
    circd=plt.Circle((x,y), radius=3, color='black', fill=True)
    ax.add_patch(circd)
    ax.text(x+5, y, "x="+str(int(x))+"\ny="+str(int(y)), fontsize=8, color='black')
    
    # Add labels for beacons
    ax.text(xA+3, yA+3, 'A', fontsize=10, color='red')
    ax.text(xB+3, yB+3, 'B', fontsize=10, color='green')
    ax.text(xC+3, yC+3, 'C', fontsize=10, color='blue')
    
    plt.title('Trilateration - Real Time')
    plt.grid(True, alpha=0.3)
    plt.draw()
    plt.pause(0.01)  # Brief pause for display update

def main():
    """
    TRILATERATION SIMULATION:
    
    This simulation models a real-world scenario where:
    - Three beacons (A, B, C) are at fixed, known positions
    - Each beacon measures the distance to a moving target object
    - Distance measurements change over time (simulating movement)
    - The trilateration algorithm calculates the target's position
    
    In practice, distances might come from:
    - WiFi/Bluetooth signal strength (RSSI)
    - Time-of-flight measurements (ultrasonic, radar)
    - GPS satellite distances
    """
    # BEACON POSITIONS AND INITIAL DISTANCE MEASUREMENTS:
    # Beacon A: position (30, 130), initial distance 70 units
    xA = 30   # x-coordinate of beacon A
    yA = 130  # y-coordinate of beacon A  
    zA = 70   # measured distance from beacon A to target
    # Beacon B: position (30, 10), initial distance 80 units
    xB = 30   # x-coordinate of beacon B
    yB = 10   # y-coordinate of beacon B
    zB = 80   # measured distance from beacon B to target
    
    # Beacon C: position (150, 30), initial distance 100 units  
    xC = 150  # x-coordinate of beacon C
    yC = 30   # y-coordinate of beacon C
    zC = 100  # measured distance from beacon C to target

    # SIMULATION: Model target movement by changing distance measurements
    # In reality, as an object moves, the measured distances to each beacon change
    # This simulation artificially modifies the distances to show how trilateration
    # tracks a moving target in real-time
    
    # Movement pattern 1: Target moving away from A, closer to B, closer to C
    for i in range(1,20):
        zA+=1
        zB-=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    # Movement pattern 2: Different trajectory
    for i in range(1,20):
        zA+=1   # Distance to A increases (moving away from A)
        zB-=1   # Distance to B decreases (moving toward B) 
        zC+=1   # Distance to C increases (moving away from C)
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
        
    # Movement pattern 3: Another trajectory
    for i in range(1,20):
        zA-=1   # Distance to A decreases (moving toward A)
        zB+=1   # Distance to B increases (moving away from B)
        zC-=1   # Distance to C decreases (moving toward C) 
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    for i in range(1,30):
        zA+=1
        zB+=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    for i in range(1,15):
        #zA+=1
        zB+=1
        #zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    for i in range(1,5):
        #zA+=1
        zB+=1
        zC-=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    for i in range(1,15):
        #zA+=1
        zB+=1
        zC+=1
        getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC)
        print("i=",i)
    
    print("\nTrilateration simulation complete!")
    print("The animation showed how trilateration continuously tracks")
    print("a moving target using distance measurements from three beacons.")
    print("Close the matplotlib window to exit.")
    plt.show(block=True)  # Keep window open until manually closed
    
# Run the trilateration simulation
main()
