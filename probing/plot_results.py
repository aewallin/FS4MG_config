
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

d = np.loadtxt('2026-11-07_toolsetter_test.txt', usecols=(1,))
print(d)

plt.figure()
plt.subplot(1,2,1)
mu = np.mean(d)
plt.plot(d-mu,'.',label='N=%d repeats, mean %.3f mm, stdev %.3f mm'%(len(d), np.mean(d-mu), np.std(d-mu)))
plt.ylabel('Z-coordinate-mean / mm')
plt.xlabel('repeat number')

plt.title('2026-11-07 Toolsetter repeated probing test')
plt.grid()
plt.legend()
plt.subplot(1,2,2)
plt.hist(d-mu, density=True,)
npdf = stats.Normal(mu=np.mean(d-mu), sigma=np.std(d-mu))
npdf.plot()
plt.xlabel('Z-coordinate / mm')
plt.ylabel('count')
plt.grid()




plt.show()
