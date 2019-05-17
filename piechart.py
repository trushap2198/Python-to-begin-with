import matplotlib.pyplot as plt
slices=[3,4,6,2,5,4];
activities=['ride','ride','jump','eat','play','study']
cols=['g','b','c','m','k','w']
plt.pie(slices,labels=activities,colors=cols)
plt.show()