import os

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv',
                      delimiter=',', skiprows=2)

# slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# plot ipgt vs gfp
plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('IPTG Titration - semilog X')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4,15)
plt.show()

# slice out error
sem = data_txt[:,2]

# plot ipgt vs gfp with error bars
plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('IPTG Titration - semilog X with error bars')
plt.ylim(-0.02, 1.1)
plt.xlim(8e-4,15)
plt.xscale('log')
plt.show()

# Practice exercise 3: eCDF

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

plt.plot(x_high, y_high, marker='.', linestyle='none', markersize='20', alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize='20', alpha=0.5)
plt.xlabel('Cross sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')
plt.show()
