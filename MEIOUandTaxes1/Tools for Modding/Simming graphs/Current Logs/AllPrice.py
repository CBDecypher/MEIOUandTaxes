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
        
        food = get_data(t, 'Global Food Price')
        salt = get_data(t, 'Global Salt Price')
        fiber = get_data(t, 'Global Fiber Price')
        fuel = get_data(t, 'Global Fuel Price')
        raw = get_data(t, 'Global Raw Material Price')
        delicacies = get_data(t, 'Global Delicacies Price')
        exotic = get_data(t, 'Global Exotics Price')
        consumer = get_data(t, 'Global Consumer Product Price')
        military = get_data(t, 'Global Military Product Price')
        naval = get_data(t, 'Global Naval Product Price')
        industrial = get_data(t, 'Global Industrial Product Price')
        luxury = get_data(t, 'Global Luxury Product Price')
        knowledge = get_data(t, 'Global Knowledge Price')
        itr = range(1, len(food) + 1)

        plt.plot(itr, food, label="Food")
        plt.plot(itr, salt, label="Salt")
        plt.plot(itr, fiber, label="Fiber")
        plt.plot(itr, fuel, label="Fuel")
        plt.plot(itr, raw, label="Raw")
        plt.plot(itr, delicacies, label="Delicacies")
        plt.plot(itr, exotic, label="Exotics")
        plt.plot(itr, consumer, label="Consumer")
        plt.plot(itr, military, label="Military")
        plt.plot(itr, naval, label="Naval")
        plt.plot(itr, industrial, label="Industrial")
        plt.plot(itr, luxury, label="Luxury")
        plt.plot(itr, knowledge, label="Knowledge")

        plt.legend(loc=2, ncol=2)

        plt.show()
