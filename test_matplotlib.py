import matplotlib
print("Current backend:", matplotlib.get_backend())
print("Interactive mode:", matplotlib.is_interactive())

# Try to set a GUI backend that should work
try:
    matplotlib.use('TkAgg')
    print("Set backend to TkAgg")
except:
    try:
        matplotlib.use('Qt5Agg')  
        print("Set backend to Qt5Agg")
    except:
        print("Could not set GUI backend")

import numpy as np

# Simple test plot
plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo-')
plt.title('Test Plot - If you see this window, matplotlib GUI is working!')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)

print("Attempting to show plot...")
plt.show(block=True)
print("Plot window closed.")