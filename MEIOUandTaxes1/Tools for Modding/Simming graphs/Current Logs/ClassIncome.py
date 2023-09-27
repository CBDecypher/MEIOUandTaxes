from matplotlib import pyplot as plt
import pandas as pd

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
        
        sfwealth = get_data(t, 'Peasant Income Total')
        nmwealth = get_data(t, 'Nomad Income Total')
        rewealth = get_data(t, 'Resident Income Total')
        nowealth = get_data(t, 'Noble Income Total')
        bgwealth = get_data(t, 'Burgher Income Total')
        clwealth = get_data(t, 'Clergy Income Total')
        itr = range(1, len(sfwealth) + 1)

        #plt.plot(itr, wage, label="Total")
        plt.plot(itr, sfwealth, label="Peasant")
        plt.plot(itr, nmwealth, label="Nomad")
        plt.plot(itr, rewealth, label="Resident")
        plt.plot(itr, nowealth, label="Noble")
        plt.plot(itr, bgwealth, label="Burgher")
        plt.plot(itr, clwealth, label="Clergy")

        plt.legend(loc=2, ncol=2)

        plt.show()
