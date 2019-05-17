g=[[1,2,3],
   [4,5,6],
   [7,8,9],]
diags=[]
for col,row in enumerate(reversed(range(len(g)))):
	diags.append(g[row][col])
	print(row,col)
	print(list(reversed(range(len(g)))))
	print(list(enumerate(reversed(range(len(g))))))
	
print(diags)
diags2=[]
for ix in range(len(g)):
	diags2.append(g[ix][ix])
print(diags2)

ver=[]
for col in range(len(g)):
	for row in g:
		ver.append[col]
	if ver.count(ver[0])==len(g) and ver[0]!=0:
	
		