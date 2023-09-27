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

import os
def read_and_concatenate_old_logs(directory='.'):
    concatenated_text = ''
    for file_name in sorted(os.listdir(directory)):
        if file_name.startswith('game_') and file_name.endswith('.log') and file_name != 'game.log':
            with open(file_name, 'r') as f:
                concatenated_text += f.read()
    return concatenated_text

if __name__ == '__main__':
    with open('game.log') as f:
        t = read_and_concatenate_old_logs()
        t += f.read()
        
        Saltp = np.array(get_data(t, 'Salt Production'))
        Saltd = np.array(get_data(t, 'Salt Demand'))
        Salte = np.array(get_data(t, 'Salt DirectBuy'))
        Saltf = Saltd + Salte
        Saltj = Saltp + Salte
        itr = range(1, len(Saltp) + 1)

        plt.plot(itr, Saltp, label="Production")
        plt.plot(itr, Saltd, label="Market Demand")
        plt.plot(itr, Salte, label="Direct Buy")
        plt.plot(itr, Saltf, label="Total Demand")
        plt.plot(itr, Saltj, label="Total Production")

        plt.legend(loc=2, ncol=2)

        plt.show()
