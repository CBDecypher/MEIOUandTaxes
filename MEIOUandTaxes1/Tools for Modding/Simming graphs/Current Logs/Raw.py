from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def get_data(t, i):
    lst = []
    loc = 0

    while True:
        loc = t.find(i, loc)

        if loc != -1:
            end = t.find('\n', loc)
            lst.append(float(t[loc:end].strip().split(':')[1].strip()))
            loc = end
        else:
            break

    return lst

if __name__ == '__main__':
    with open('game.log') as f:
        t = f.read()
        
        Fuelp = np.array(get_data(t, 'Raw Material Production'))
        Fueld = np.array(get_data(t, 'Raw Material Demand'))
        itr = range(1, len(Fuelp) + 1)

        plt.plot(itr, Fuelp, label="Production")
        plt.plot(itr, Fueld, label="Demand")

        plt.legend(loc=2, ncol=2)

        plt.show()
