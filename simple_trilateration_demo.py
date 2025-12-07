import math
import numpy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

def calculate_trilateration(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    """
    Calculate the trilateration position using the same algorithm as the main script
    """
    # Convert circle equations to standard form coefficients
    A1 = -2 * xA
    B1 = xA**2
    C1 = -2 * yA
    D1 = yA**2
    E1 = zA**2
    
    A2 = -2 * xB
    B2 = xB**2
    C2 = -2 * yB
    D2 = yB**2
    E2 = zB**2
    
    A3 = -2 * xC
    B3 = xC**2
    C3 = -2 * yC
    D3 = yC**2
    E3 = zC**2
    
    # Create linear system by subtracting equations
    A = A1 - A2
    B = B1 - B2
    C = C1 - C2
    D = D1 - D2
    E = E1 - E2
    E -= B
    E -= D
    A = -A
    
    # Convert first equation to slope-intercept form
    E = E / float(C)
    A = A / float(C)
    
    # Second equation
    A2_new = A2 - A3
    B2_new = B2 - B3
    C2_new = C2 - C3
    D2_new = D2 - D3
    E2_new = E2 - E3
    E2_new -= B2_new
    E2_new -= D2_new
    A2_new = -A2_new
    
    # Convert second equation to slope-intercept form
    E2_new = E2_new / float(C2_new)
    A2_new = A2_new / float(C2_new)
    
    # Find intersection of two lines
    A5 = E2_new - E
    B5 = abs(A2_new) + A
    x = A5 / B5
    
    # Calculate y using one of the line equations
    y = (A2_new * x) + E2_new
    
    return x, y

def create_trilateration_plot():
    # Example beacon positions and radii (well-separated triangle formation)
    xA, yA, zA = 10, 100, 85   # Beacon A (top-left)
    xB, yB, zB = 40, 10, 75    # Beacon B (bottom-center)  
    xC, yC, zC = 140, 60, 70   # Beacon C (right-middle)
    
    # Calculate actual trilateration position
    x, y = calculate_trilateration(xA, yA, zA, xB, yB, zB, xC, yC, zC)
    print(f"Calculated position: ({x:.2f}, {y:.2f})")
    
    # Create the plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(-100, 190)
    ax.set_ylim(-100, 190)
    
    # Draw beacon circles (detection range)
    circa = plt.Circle((xA, yA), radius=zA, color='red', fill=False, linewidth=2, label=f'Beacon A (r={zA})')
    circb = plt.Circle((xB, yB), radius=zB, color='green', fill=False, linewidth=2, label=f'Beacon B (r={zB})')
    circc = plt.Circle((xC, yC), radius=zC, color='blue', fill=False, linewidth=2, label=f'Beacon C (r={zC})')
    
    # Draw beacon positions
    ax.plot(xA, yA, 'ro', markersize=8, label='Beacon A')
    ax.plot(xB, yB, 'go', markersize=8, label='Beacon B')
    ax.plot(xC, yC, 'bo', markersize=8, label='Beacon C')
    
    # Draw calculated position
    ax.plot(x, y, 'ko', markersize=10, label=f'Calculated Position ({x}, {y})')
    
    # Add circles to plot
    ax.add_patch(circa)
    ax.add_patch(circb) 
    ax.add_patch(circc)
    
    # Add labels
    ax.text(xA+5, yA+5, f'A({xA},{yA})', fontsize=10)
    ax.text(xB+5, yB+5, f'B({xB},{yB})', fontsize=10)
    ax.text(xC+5, yC+5, f'C({xC},{yC})', fontsize=10)
    ax.text(x+5, y+5, f'Target({x},{y})', fontsize=10, fontweight='bold')
    
    plt.title('Trilateration Example\nThree circles intersect to determine position')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')
    plt.axis('equal')
    
    # Save the plot
    plt.savefig('trilateration_example.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("Trilateration visualization saved as 'trilateration_example.png'")
    print(f"Three beacons at A({xA},{yA}), B({xB},{yB}), C({xC},{yC})")
    print(f"With detection radii {zA}, {zB}, {zC} respectively")
    print(f"Calculate target position: ({x}, {y})")

if __name__ == "__main__":
    create_trilateration_plot()