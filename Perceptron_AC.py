import numpy as np

A = """
.*.
***
*.*
"""

C = """
***
*..
***
"""

Inputs = [C, A]
Y = [1, -1]

theta = 0.2
alpha = 1

def st_to_arr(s):
    res= []
    for e in s:
        if e == '*':
            res.append(1)
        elif e == '.':
            res.append(-1)
    return np.array(res)

X = []
for inp in Inputs:
    X.append(st_to_arr(inp))

def AF(x):
    if x<-theta:
        return -1
    elif x>theta:
        return 1
    return 0

AF = np.vectorize(AF)

X = np.array(X)

W = np.zeros(shape=(9))
b = 0

def get_y(x, w, b):
    y = np.sum(x*w) + b
    return AF(y)

#max 100 epochs
for epc in range(1,101):
    for i in range(2):
        x = X[i]
        y = get_y(x, W, b)

        if y != Y[i]:
            #weight updations
            deltaW = x*alpha * Y[i]
            W += deltaW
            deltab = Y[i]*alpha
            b += deltab
        
    # Checking Output
    ypred = np.zeros(shape=(2))
    for i in range(2):
        x = X[i]
        y = get_y(x, W, b)

        ypred[i] = y
    if np.all(ypred == Y):
        print(f"Correctly classified after {epc} epochs, W = {W}, b = {b}")
        break

for inp in Inputs:
    y = get_y(st_to_arr(inp), W, b)
    print(f"\nFor {inp} y = {y}")