import matplotlib.pyplot as plt

def plot_voltage(X,Y,V):
    mesh = plt.pcolormesh(X,Y,V)
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Voltage Heatmap")
    plt.colorbar(mesh)
    plt.savefig("voltage_heatmap.png")
    plt.show()