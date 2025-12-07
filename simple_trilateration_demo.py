import math
import numpy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

def create_trilateration_plot():
    # Example beacon positions and radii
    xA, yA, zA = 30, 130, 70  # Beacon A
    xB, yB, zB = 30, 10, 80   # Beacon B  
    xC, yC, zC = 150, 30, 100 # Beacon C
    
    # Calculate trilateration (simplified from original)
    x, y = 72, 55  # Example calculated position
    
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