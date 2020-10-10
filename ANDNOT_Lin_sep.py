import numpy as np
import matplotlib.pyplot as plt

# Inputs
X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
Y = np.array([-1, -1, 1, -1])


def check(X, Y, m, c):
    up = 0
    down = 0

    for i in range(4):
        y = m*X[i, 0] + c
        if (X[i, 1] < y):
            if down == 0:
                down = Y[i]
            elif down != Y[i]:
                return False
        if (X[i, 1] >= y):
            if up == 0:
                up = Y[i]
            elif up != Y[i]:
                return False
    return [up, down]

colmap = ["#ff0000", "#ff0000", "#00ff00", "#ff0000"]
plt.scatter(X[:, 0], X[:, 1], c=colmap)
plt.title("Points given")
plt.show()

mvals = [-1, 0, 1]
cvals = [-1, 0, 1]

for m in mvals:
    for c in cvals:
        v = check(X, Y, m, c)
        if v:
            mul = v[0]
            print(f"Line FOUND, Weights are: w1= {-m*mul}, w2 = {mul}, b = {-c*mul}")
            print(f"Activation function is: For Yin>=0, Y = {1}")
            print(f"                        For Yin<0, Y = {-1}")
            plt.scatter(X[:, 0], X[:, 1], c=colmap)
            plt.plot([-1, 1], [-m+c, m+c], label = f"m={m}, c={c}")
            plt.legend()
            plt.title(f"Linear seperability by all lines (Solid line is correct)")
            plt.show()
            quit()
            
        else:
            print(f"It is NOT linearly seperabel by m = {m}, c = {c}")
            plt.scatter(X[:, 0], X[:, 1], c=colmap)
            plt.plot([-1, 1], [-m+c, m+c], "--", label = f"m={m}, c={c}")