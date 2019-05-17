import matplotlib.pyplot as plt
pop=[12,12,454,23,65,23,89,12,4,23,65,23,54,72,56,91,14,54,2,1234,543,2,2,2,2,2,2,2,2,2]
id=[x for x in range(len(pop))]
for i in range(len(id)):
	id[i]=id[i]+i*9
print(id)
plt.hist(pop,id,histtype='bar',rwidth=0.2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()