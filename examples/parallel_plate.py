from electrostatics.grid import make_grid
from electrostatics.geometry import set_plates
from electrostatics.visualize import plot_voltage

X, Y, V, mask = make_grid(50, 50)
V, mask = set_plates(V, mask, 100)
plot_voltage(X, Y, V)