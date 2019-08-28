import numpy as np
from timeit import default_timer as timer
nsim = 1000

# Create large array:
n = 10000
x = np.linspace(-100,100,n)
# Divide in four in an array and in a dict:
idx1,idx2,idx3,idx4 = range(0,n/4),range(n/4,n/2),range(n/2,n/2 + n/4),range(n/2 + n/4,n)
d = {}
d['1'] = x[idx1]
d['2'] = x[idx2]
d['3'] = x[idx3]
d['4'] = x[idx4]
# Now operate on them separately and time it several times, print average and standard deviation:
vals1 = np.zeros(nsim)
vals2 = np.zeros(nsim)
for i in range(nsim):
    # First operate on the arrays:
    start = timer()
    a1 = x[idx1]**2
    b1 = x[idx2]**2
    c1 = x[idx3]**2
    d1 = x[idx4]**2
    end = timer()
    vals1[i] = end-start
    # Now operate on the dictionary:
    start = timer()
    a2 = d['1']**2
    b2 = d['2']**2
    c2 = d['3']**2
    d2 = d['4']**2
    end = timer()
    vals2[i] = end-start
vals1 = vals1*1e6
vals2 = vals2*1e6
print('Arrays take: ',np.median(vals1),'+-',np.sqrt(np.var(vals1)),' micro-seconds')
print('Dictionaries take: ',np.median(vals2),'+-',np.sqrt(np.var(vals2)),' micro-seconds')
