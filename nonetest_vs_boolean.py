import numpy as np
from timeit import default_timer as timer
nsim = 1000

# Create large array:
n = 10000
x = np.linspace(-100,100,n)
boolean = True
# Now operate on them separately and time it several times, print average and standard deviation:
vals1 = np.zeros(nsim)
vals2 = np.zeros(nsim)
for i in range(nsim):
    # First check if not None:
    start = timer()
    if x is not None:
        a1 = 1.
    end = timer()
    vals1[i] = end-start
    # Now simply check the boolean:
    start = timer()
    if boolean:
        a1 = 1.
    end = timer()
    vals2[i] = end-start
vals1 = vals1*1e9
vals2 = vals2*1e9
print vals1
print vals2
print('None test takes: ',np.median(vals1),'+-',np.sqrt(np.var(vals1)),' nano-seconds')
print('Boolean test takes: ',np.median(vals2),'+-',np.sqrt(np.var(vals2)),' nano-seconds')
