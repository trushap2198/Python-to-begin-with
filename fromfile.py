import matplotlib.pyplot as plt
import numpy as np
"""
import csv as cs
x=[]
y=[]
with open('file.txt','r') as csf:
	plot=cs.reader(csf,delimiter=',');#prints each ',' seprated values as a list and finally creates a final list
	#so in short it creates a list of lists
	for row in plot:
		x.append(row[0]);#1,2,3,4,5 are row[0]
		y.append(row[1]);#12,13,14,15,16 are row[1]
		#each row has one list of two elements
	print(list(plot));
plt.plot(x,y,label="sdhfjh")
plt.show()
"""
x,y=np.loadtxt('file.txt',delimiter=',',unpack=True);
plt.plot(x,y,label="sjahg");
plt.show()