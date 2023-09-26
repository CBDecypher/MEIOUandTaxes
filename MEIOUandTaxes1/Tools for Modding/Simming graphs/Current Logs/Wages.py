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

if __name__ == '__main__':
    with open('game.log') as f:
        t = f.read()
        
        food1 = get_data(t, 'Rural Wage')
        food2 = get_data(t, 'Nomad Wage')
        food3 = get_data(t, 'Urban Wage')
        itr = range(1, len(food1) + 1)

        plt.plot(itr, food1, label="Rural")
        plt.plot(itr, food2, label="Nomad")
        plt.plot(itr, food3, label="Urban")

        plt.legend(loc=2, ncol=2)

        plt.show()
