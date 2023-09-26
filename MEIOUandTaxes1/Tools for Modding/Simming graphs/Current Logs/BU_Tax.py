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
        
        Direct = get_data(t, 'BUTax Direct')
        Indirect = get_data(t, 'BUTax Indirect')
        Revenue = get_data(t, 'BUTax Revenue')
        #Total = get_data(t, 'BUTax Total')
        Fees = get_data(t, 'BUTax Fees')
        Rents = get_data(t, 'BUTax Rents')
        Obligations = get_data(t, 'BUTax Obligations')
        Poll = get_data(t, 'BUTax Poll')
        Land = get_data(t, 'BUTax Land')
        PropertyBU = get_data(t, 'BUTax PropertyBU')
        Chattel = get_data(t, 'BUTax Chattel')
        Inheritance = get_data(t, 'BUTax Inheritance')
        TollBU = get_data(t, 'BUTax TollBU')
        SaltBU = get_data(t, 'BUTax SaltBU')
        SubstancesBU = get_data(t, 'BUTax SubstancesBU')
        TimberBU = get_data(t, 'BUTax TimberBU')
        AlcoholBU = get_data(t, 'BUTax AlcoholBU')
        ForestBU = get_data(t, 'BUTax ForestBU')
        Corruption = get_data(t, 'BUTax Corruption')
        Farming = get_data(t, 'BUTax Farming')
        Special = get_data(t, 'BUTax Special')
        Commerce = get_data(t, 'BUTax Commerce')
        BUProperty = get_data(t, 'BUTax BUProperty')
        itr = range(1, len(Poll) + 1)

        plt.plot(itr, Direct, label="Direct")
        plt.plot(itr, Indirect, label="Indirect")
        plt.plot(itr, Revenue, label="Revenue")
        #plt.plot(itr, Total, label="Total")
        plt.plot(itr, Obligations, label="Elite Obligations")
        plt.plot(itr, BUProperty, label="Property Income")
        plt.plot(itr, Farming, label="Rev Farming", linestyle='--')
        plt.plot(itr, Corruption, label="Corruption", linestyle='--')

        plt.legend(loc=2, ncol=2)

        plt.show()
