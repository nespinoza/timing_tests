import numpy as np
from timeit import default_timer as timer
nsim = 10000

def get_mad_sigma(x):
    return np.median(np.abs(x-np.median(x)))*1.4826
    
# Create large arrays of zeros:
n = 100000
x = np.zeros(n)
# Create arrays that will save the times:
vals1,vals2 = np.ones(nsim),np.ones(nsim)
# Now check if copying or creating new zero-arrays is faster.
for i in range(nsim):
    # Define variables that will host the copies:
    v1,v2 = 0.,0.
    start = timer()
    # Copy the zero-array:
    v1 = np.copy(x)
    end = timer()
    vals1[i] = end-start
    start = timer()
    # Create the zero array:
    v2 = np.zeros(n)
    end = timer()
    vals2[i] = end-start
d = vals1/vals2
vals1 = vals1*1e6
vals2 = vals2*1e6
print('Copying zero array takes: ',np.median(vals1),'+-',get_mad_sigma(vals1),' micro-seconds')
print('Creating zero array takes: ',np.median(vals2),'+-',get_mad_sigma(vals2),' micro-seconds')
print('Copying arrays takes ',np.median(d),'+-',get_mad_sigma(d),' times more than creating them')
print('Creating arrays takes ',np.median(1./d),'+-',get_mad_sigma(1./d),' times more than copying them')
